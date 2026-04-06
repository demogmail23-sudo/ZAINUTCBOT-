import os
import sys
import subprocess
import threading
import time
import requests
import sqlite3
from datetime import datetime, timedelta
from flask import Flask, render_template, request, jsonify, session, redirect, url_for, render_template_string
from flask_socketio import SocketIO

# Buffering off for real-time logs
os.environ['PYTHONUNBUFFERED'] = '1'

app = Flask(__name__)
app.secret_key = "bot_secret_access_key_2026_99" 
socketio = SocketIO(app, cors_allowed_origins="*", async_mode='threading')

# --- DATABASE SETUP ---
DB_NAME = "users.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    # Create users table
    cursor.execute('''CREATE TABLE IF NOT EXISTS users 
                      (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                       username TEXT UNIQUE, 
                       password TEXT)''')
    # Default admin account
    cursor.execute("SELECT count(*) FROM users WHERE username='admin'")
    if cursor.fetchone()[0] == 0:
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", ('admin', 'changeme123'))
    conn.commit()
    conn.close()

init_db()

user_sessions = {} 
ADMIN_CONFIG = "admin_config.txt"

# --- LOGIN & SIGNUP HTML ---
AUTH_HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Bot Access</title>
    <style>
        body { background-color: #0d0d0d; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; color: #fff; }
        .login-card { background-color: #1a1a1a; padding: 35px; border-radius: 20px; width: 340px; border: 1px solid #2a2a2a; box-shadow: 0 15px 35px rgba(0,0,0,0.6); }
        .logo-section { display: flex; align-items: center; justify-content: center; gap: 10px; margin-bottom: 30px; }
        .logo-icon { background-color: #ff6b35; padding: 6px 10px; border-radius: 8px; font-weight: bold; font-size: 18px; }
        .logo-text { letter-spacing: 3px; font-weight: bold; font-size: 22px; }
        .input-group { margin-bottom: 20px; }
        .label { font-size: 12px; font-weight: bold; text-transform: uppercase; margin-bottom: 8px; display: flex; align-items: center; gap: 8px; color: #999; }
        input { width: 100%; padding: 14px; background-color: #0a0a0a; border: 1px solid #333; border-radius: 12px; color: #fff; box-sizing: border-box; transition: 0.3s; }
        input:focus { border-color: #ff6b35; outline: none; box-shadow: 0 0 8px rgba(255, 107, 53, 0.3); }
        .login-btn { background-color: #ff6b35; color: white; border: none; width: 100%; padding: 14px; border-radius: 12px; font-weight: bold; cursor: pointer; display: flex; align-items: center; justify-content: center; gap: 10px; text-transform: uppercase; font-size: 15px; margin-top: 10px; }
        .toggle-link { text-align: center; margin-top: 20px; font-size: 13px; color: #777; cursor: pointer; }
        .toggle-link span { color: #ff6b35; font-weight: bold; text-decoration: underline; }
        #msg { color: #ff4444; font-size: 13px; text-align: center; margin-bottom: 15px; display: none; }
    </style>
</head>
<body>
    <div class="login-card">
        <div class="logo-section">
            <div class="logo-icon">🎮</div>
            <div class="logo-text" id="form-title">LOGIN</div>
        </div>
        <div id="msg"></div>
        <div class="input-group">
            <div class="label">👤 Username</div>
            <input type="text" id="u" placeholder="Enter username">
        </div>
        <div class="input-group">
            <div class="label">🔒 Password</div>
            <input type="password" id="p" placeholder="Enter password">
        </div>
        <button class="login-btn" id="submit-btn" onclick="handleSubmit()">➜ LOGIN</button>
        
        <div class="toggle-link" id="toggle-area" onclick="toggleForm()">
            New user? <span>Create Account</span>
        </div>
    </div>

    <script>
        let isLoginMode = true;

        function toggleForm() {
            isLoginMode = !isLoginMode;
            document.getElementById('form-title').innerText = isLoginMode ? 'LOGIN' : 'SIGNUP';
            document.getElementById('submit-btn').innerText = isLoginMode ? '➜ LOGIN' : '➜ SIGNUP';
            document.getElementById('toggle-area').innerHTML = isLoginMode ? 
                'New user? <span>Create Account</span>' : 
                'Already have an account? <span>Login</span>';
        }

        async function handleSubmit() {
            const u = document.getElementById('u').value;
            const p = document.getElementById('p').value;
            const msg = document.getElementById('msg');
            
            const endpoint = isLoginMode ? '/api/login_auth' : '/api/signup_auth';
            
            const resp = await fetch(endpoint, {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({username: u, password: p})
            });
            const data = await resp.json();

            if(data.status === 'success') {
                if(isLoginMode) {
                    window.location.href = '/';
                } else {
                    alert("Account created successfully! Now Login.");
                    toggleForm();
                }
            } else {
                msg.innerText = data.message;
                msg.style.display = 'block';
                setTimeout(() => { msg.style.display = 'none'; }, 3000);
            }
        }
    </script>
</body>
</html>
"""

def get_config():
    conf = {"pass": "admin123", "duration": 120}
    if os.path.exists(ADMIN_CONFIG):
        with open(ADMIN_CONFIG, 'r') as f:
            for line in f:
                if '=' in line:
                    parts = line.strip().split('=')
                    if len(parts) == 2:
                        key, val = parts
                        if key == 'admin_password': conf['pass'] = val
                        if key == 'global_duration': conf['duration'] = int(val)
    return conf

def save_config(password, duration):
    with open(ADMIN_CONFIG, 'w') as f:
        f.write(f"admin_password={password}\nglobal_duration={duration}\n")

def login_required(f):
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        return redirect(url_for('login'))
    wrap.__name__ = f.__name__
    return wrap

def expiry_monitor():
    while True:
        now = datetime.now()
        for name, data in list(user_sessions.items()):
            if data['running'] and data['end_time'] != "unlimited":
                if now > data['end_time']:
                    if data['proc']:
                        data['proc'].terminate()
                    user_sessions[name]['running'] = False
                    socketio.emit('status_update', {'running': False, 'user': name})
        time.sleep(2)

threading.Thread(target=expiry_monitor, daemon=True).start()

def stream_logs(proc, name):
    try:
        for line in iter(proc.stdout.readline, ''):
            if line:
                socketio.emit('new_log', {'data': line.strip(), 'user': name})
        proc.stdout.close()
    except Exception as e:
        print(f"Logging error for {name}: {e}")

# --- ROUTES ---

@app.route('/login')
def login():
    if 'logged_in' in session:
        return redirect(url_for('index'))
    return render_template_string(AUTH_HTML)

@app.route('/api/signup_auth', methods=['POST'])
def signup_auth():
    data = request.json
    u, p = data.get('username'), data.get('password')
    if not u or not p:
        return jsonify({"status": "error", "message": "Fill all fields!"})
    
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (u, p))
        conn.commit()
        conn.close()
        return jsonify({"status": "success"})
    except sqlite3.IntegrityError:
        return jsonify({"status": "error", "message": "Username already exists!"})

@app.route('/api/login_auth', methods=['POST'])
def login_auth():
    data = request.json
    u, p = data.get('username'), data.get('password')
    
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (u, p))
    user = cursor.fetchone()
    conn.close()
    
    if user:
        session['logged_in'] = True
        session['user_name'] = u
        return jsonify({"status": "success"})
    return jsonify({"status": "error", "message": "Invalid Username or Password!"})

@app.route('/')
@login_required
def index():
    return render_template('index.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

@app.route('/api/check_status', methods=['POST'])
@login_required
def check_status():
    data = request.json
    name = data.get('name')
    if name in user_sessions and user_sessions[name]['running']:
        info = user_sessions[name]
        rem_sec = -1 if info['end_time'] == "unlimited" else int((info['end_time'] - datetime.now()).total_seconds())
        return jsonify({"running": True, "rem_sec": max(0, rem_sec)})
    return jsonify({"running": False})

@app.route('/api/control', methods=['POST'])
@login_required
def bot_control():
    data = request.json
    action, name, uid, pw = data.get('action'), data.get('name'), data.get('uid'), data.get('password')
    conf = get_config()

    if action == 'start':
        if not uid or not pw:
            return jsonify({"status": "error", "message": "UID/PW required!"})
        if name in user_sessions and user_sessions[name]['running']:
            return jsonify({"status": "error", "message": "ALREADY RUNNING!"})
        try:
            with open("bot.txt", "w") as f: f.write(f"uid={uid}\npassword={pw}")
            proc = subprocess.Popen(
                [sys.executable, '-u', 'main.py'], 
                stdout=subprocess.PIPE, 
                stderr=subprocess.STDOUT, 
                text=True, 
                bufsize=1, 
                universal_newlines=True
            )
            end_time = "unlimited" if conf['duration'] == -1 else datetime.now() + timedelta(minutes=conf['duration'])
            user_sessions[name] = {'proc': proc, 'end_time': end_time, 'running': True}
            threading.Thread(target=stream_logs, args=(proc, name), daemon=True).start()
            rem_sec = (conf['duration'] * 60 if conf['duration'] != -1 else -1)
            return jsonify({"status": "success", "running": True, "rem_sec": rem_sec})
        except Exception as e: 
            return jsonify({"status": "error", "message": str(e)})

    elif action == 'stop':
        if name in user_sessions and user_sessions[name]['running']:
            if user_sessions[name]['proc']: 
                user_sessions[name]['proc'].terminate()
            user_sessions[name]['running'] = False
            return jsonify({"status": "success", "running": False})
    return jsonify({"status": "error", "message": "FAILED"})

@app.route('/api/admin', methods=['POST'])
@login_required
def admin_api():
    data = request.json
    conf = get_config()
    if data.get('password') != conf['pass']: return jsonify({"status": "error", "message": "Wrong Passkey!"})
    action = data.get('action')
    if action == 'login':
        active_users = []
        for n, i in user_sessions.items():
            if i['running']:
                rem_m = -1 if i['end_time'] == "unlimited" else max(0, int((i['end_time'] - datetime.now()).total_seconds() / 60))
                active_users.append({"name": n, "rem_min": rem_m})
        return jsonify({"status": "success", "duration": conf['duration'], "users": active_users})
    elif action == 'save_global':
        save_config(conf['pass'], int(data.get('duration', 120)))
        return jsonify({"status": "success"})
    return jsonify({"status": "error"})

@app.route('/api/proxy_guild')
@login_required
def proxy_guild():
    t, gid, reg, uid, pw = request.args.get('type'), request.args.get('guild_id'), request.args.get('region'), request.args.get('uid'), request.args.get('password')
    base_url = "https://guild-info-danger.vercel.app"
    urls = {
        'info': f"{base_url}/guild?guild_id={gid}&region={reg}",
        'join': f"{base_url}/join?guild_id={gid}&uid={uid}&password={pw}",
        'members': f"{base_url}/members?guild_id={gid}&uid={uid}&password={pw}",
        'leave': f"{base_url}/leave?guild_id={gid}&uid={uid}&password={pw}"
    }
    try:
        resp = requests.get(urls.get(t), timeout=15)
        return jsonify(resp.json())
    except: return jsonify({"error": "API Error"})

if __name__ == '__main__':
    socketio.run(app)
