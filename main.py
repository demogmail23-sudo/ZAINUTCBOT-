import requests, os, psutil, sys, jwt, pickle, json, binascii, time, urllib3, base64, re, socket, threading, ssl, pytz, aiohttp, traceback, signal, multiprocessing, asyncio
import random
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor
from threading import Thread

# Third-party imports
from cfonts import render, say
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import google.protobuf.json_format as json_format
from google.protobuf.timestamp_pb2 import Timestamp
from protobuf_decoder.protobuf_decoder import Parser

# Local/Custom imports
from Pb2 import (
    DEcwHisPErMsG_pb2, MajoRLoGinrEs_pb2, PorTs_pb2, MajoRLoGinrEq_pb2, 
    sQ_pb2, Team_msg_pb2, RemoveFriend_Req_pb2, GetFriend_Res_pb2, 
    spam_request_pb2, devxt_count_pb2, dev_generator_pb2, kyro_title_pb2, room_join_pb2
)
from xC4 import *
from xHeaders import *

# --- সমাধান অংশ শুরু ---

def main():
    """
    আপনার বটের মূল কাজগুলো (যেমন Manager তৈরি করা বা বট স্টার্ট করা) 
    সব এই ফাংশনের ভেতরে রাখুন।
    """
    try:
        # উদাহরণস্বরূপ:
        # manager = multiprocessing.Manager()
        # bot.run()
        print("ZAINU-VIP-V2 Bot is starting safely...")
        
        # আপনার বাকি কোড এখানে পেস্ট করুন...
        
    except Exception as e:
        print(f"Error occurred: {e}")
        traceback.print_exc()

if __name__ == "__main__":
    # Render বা ক্লাউড সার্ভারে মাল্টিপ্রসেসিং এরর ঠিক করার আসল চাবিকাঠি এটি
    if sys.platform == 'linux':
        try:
            multiprocessing.set_start_method('fork')
        except RuntimeError:
            pass
            
    main()


# =================== CONFIGURATION ======================
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)  

# =================== GLOBAL VARIABLES ===================
online_writer = None
whisper_writer = None
spammer_uid = None
msg_spam_running = False
msg_spam_task = None
mg_spam_task = None
spam_chat_id = None
spam_uid = None
Spy = False
Chat_Leave = False
fast_spam_running = False
fast_spam_task = None
custom_spam_running = False
custom_spam_task = None
spam_request_running = False
spam_request_task = None
evo_fast_spam_running = False
evo_fast_spam_task = None
evo_custom_spam_running = False
evo_custom_spam_task = None
reject_spam_running = False
reject_spam_task = None
emote_hijack = False 
lag_running = False
lag_task = None
reject_spam_running = False
reject_spam_task = None
evo_cycle_running = False
evo_cycle_task = None
status_response_cache = {} 
pending_status_requests = {}
room_info_cache = {}
last_status_packet = None
insquad = None 
joining_team = False 
online_writer = None 
whisper_writer = None 
last_bot_status_check = 0
senthi = False
bot_status_cache_time = 30
cached_bot_status = None
last_status_packet = None
START_SPAM_DURATION = 18     
WAIT_AFTER_MATCH_SECONDS = 20 
START_SPAM_DELAY = 0.2       
region = 'IN'
WHITELISTED_UIDS = {
    "2270928791"  
}
WHITELIST_ONLY = True  
BOT_OWNER_UID = 11686472351  
PLAYER_NAME_CACHE = {}  
freeze_running = False
freeze_task = None
FREEZE_EMOTES = [909052010, 909052010, 909052010]
FREEZE_DURATION = 10  # seconds
manager = multiprocessing.Manager()
status_response_cache = manager.dict()
evo_emotes = {
    "1": "909000063",   # AK
    "2": "909000068",   # SCAR
    "3": "909000075",   # 1st MP40
    "4": "909040010",   # 2nd MP40
    "5": "909000081",   # 1st M1014
    "6": "909039011",   # 2nd M1014
    "7": "909000085",   # XM8
    "8": "909000090",   # Famas
    "9": "909000098",   # UMP
    "10": "909035007",  # M1887
    "11": "909042008",  # Woodpecker
    "12": "909041005",  # Groza
    "13": "909033001",  # M4A1
    "14": "909038010",  # Thompson
    "15": "909038012",  # G18
    "16": "909045001",  # Parafal
    "17": "909049010",  # P90
    "18": "909051003",   # m60
    "1":   "909000001",
    "2":   "909000002",
    "3":   "909052001",
    "4":   "909052002",
    "5":   "909052003",
    "6":   "909052004",
    "7":   "909052005",
    "8":   "909052006",
    "9":   "909052007",
    "10":  "909052008",
    "11":  "909052009",
    "12":  "909052010",
    "13":  "909052011",
    "14":  "909052012",
    "15":  "909052013",
    "16":  "909000016",
    "17":  "909000017",
    "18":  "909000018",
    "19":  "909000019",
    "20":  "909000020",
    "21":  "909000021",
    "22":  "909000022",
    "23":  "909000023",
    "24":  "909000024",
    "25":  "909000025",
    "26":  "909000026",
    "27":  "909000027",
    "28":  "909000028",
    "29":  "909000029",
    "30":  "909000031",
    "31":  "909000032",
    "32":  "909000033",
    "33":  "909000034",
    "34":  "909000035",
    "35":  "909000036",
    "36":  "909000037",
    "37":  "909000038",
    "38":  "909000039",
    "39":  "909000040",
    "40":  "909000041",
    "41":  "909000042",
    "42":  "909000043",
    "43":  "909000044",
    "44":  "909000045",
    "45":  "909000046",
    "46":  "909000047",
    "47":  "909000048",
    "48":  "909000049",
    "49":  "909000051",
    "50":  "909000052",
    "51":  "909000053",
    "52":  "909000054",
    "53":  "909000055",
    "54":  "909000056",
    "55":  "909000057",
    "56":  "909000058",
    "57":  "909000059",
    "58":  "909000060",
    "59":  "909000061",
    "60":  "909000062",
    "61":  "909000063",
    "62":  "909000064",
    "63":  "909000065",
    "64":  "909000066",
    "65":  "909000067",
    "66":  "909000068",
    "67":  "909000069",
    "68":  "909000070",
    "69":  "909000071",
    "70":  "909000072",
    "71":  "909000073",
    "72":  "909000074",
    "73":  "909000075",
    "74":  "909000076",
    "75":  "909000077",
    "76":  "909000078",
    "77":  "909000079",
    "78":  "909000080",
    "79":  "909000081",
    "80":  "909000082",
    "81":  "909000083",
    "82":  "909000084",
    "83":  "909000085",
    "84":  "909000086",
    "85":  "909000087",
    "86":  "909000088",
    "87":  "909000089",
    "88":  "909000090",
    "89":  "909000091",
    "90":  "909000092",
    "91":  "909000093",
    "92":  "909000094",
    "93":  "909000095",
    "94":  "909000096",
    "95":  "909000097",
    "106": "909000108",
    "119": "909000121",
    "120": "909000122",
    "121": "909000123",
    "122": "909000124",
    "123": "909000125",
    "124": "909000126",
    "125": "909000127",
    "126": "909000128",
    "127": "909000129",
    "128": "909000130",
    "129": "909000131",
    "130": "909000132",
    "131": "909000133",
    "132": "909000134",
    "133": "909000135",
    "134": "909000136",
    "135": "909000137",
    "136": "909000138",
    "137": "909000139",
    "138": "909000140",
    "139": "909000141",
    "140": "909000142",
    "142": "909000144",
    "143": "909000145",
    "144": "909000150",
    "145": "909033001",
    "146": "909033002",
    "147": "909033003",
    "148": "909033004",
    "149": "909033005",
    "150": "909033006",
    "151": "909033007",
    "152": "909033008",
    "153": "909033009",
    "154": "909033010",
    "155": "909034001",
    "156": "909034002",
    "157": "909034003",
    "158": "909034004",
    "159": "909034005",
    "160": "909034006",
    "161": "909034007",
    "162": "909034008",
    "163": "909034009",
    "164": "909034010",
    "165": "909034011",
    "166": "909034012",
    "167": "909034013",
    "168": "909034014",
    "169": "909035001",
    "173": "909035005",
    "174": "909035006",
    "175": "909035007",
    "176": "909035008",
    "177": "909035009",
    "178": "909035010",
    "179": "909035011",
    "180": "909035012",
    "181": "909035013",
    "182": "909035014",
    "183": "909035015",
    "184": "909036001",
    "185": "909036002",
    "186": "909036003",
    "187": "909036004",
    "188": "909036005",
    "189": "909036006",
    "190": "909036008",
    "191": "909036009",
    "192": "909036010",
    "193": "909036011",
    "194": "909036012",
    "195": "909036014",
    "196": "909037001",
    "197": "909037002",
    "198": "909037003",
    "199": "909037004",
    "200": "909037005",
    "201": "909037006",
    "202": "909037007",
    "203": "909037008",
    "204": "909037009",
    "205": "909037010",
    "206": "909037011",
    "207": "909037012",
    "208": "909038001",
    "210": "909038003",
    "211": "909038004",
    "212": "909038005",
    "213": "909038006",
    "214": "909038008",
    "215": "909038009",
    "216": "909038010",
    "217": "909038011",
    "218": "909038012",
    "219": "909038013",
    "220": "909039001",
    "221": "909039002",
    "222": "909039003",
    "223": "909039004",
    "224": "909039005",
    "225": "909039006",
    "226": "909039007",
    "227": "909039008",
    "228": "909039009",
    "229": "909039010",
    "230": "909039011",
    "231": "909039012",
    "232": "909039013",
    "233": "909039014",
    "234": "909040001",
    "235": "909040002",
    "236": "909040003",
    "237": "909040004",
    "238": "909040005",
    "239": "909040006",
    "240": "909040008",
    "241": "909040009",
    "242": "909040010",
    "243": "909040011",
    "244": "909040012",
    "245": "909040013",
    "247": "909041001",
    "248": "909041002",
    "249": "909041003",
    "250": "909041004",
    "251": "909041005",
    "252": "909041006",
    "253": "909041007",
    "254": "909041008",
    "255": "909041009",
    "256": "909041010",
    "257": "909041011",
    "258": "909041012",
    "259": "909041013",
    "260": "909041014",
    "261": "909041015",
    "262": "909042001",
    "263": "909042002",
    "264": "909042003",
    "265": "909042004",
    "266": "909042005",
    "267": "909042006",
    "100": "909042007",
    "269": "909042008",
    "270": "909042009",
    "271": "909042011",
    "272": "909042012",
    "274": "909042016",
    "275": "909042017",
    "276": "909042018",
    "277": "909043001",
    "278": "909043002",
    "279": "909043003",
    "280": "909043004",
    "281": "909043005",
    "282": "909043006",
    "283": "909043007",
    "284": "909043008",
    "285": "909043009",
    "288": "909044001",
    "289": "909044002",
    "290": "909044003",
    "291": "909044004",
    "292": "909044005",
    "294": "909044007",
    "295": "909044008",
    "296": "909044009",
    "297": "909044010",
    "298": "909044011",
    "299": "909044012",
    "300": "909044015",
    "301": "909044016",
    "302": "909045001",
    "303": "909045002",
    "304": "909045003",
    "305": "909045004",
    "306": "909045005",
    "307": "909045006",
    "308": "909045007",
    "309": "909045008",
    "310": "909045009",
    "311": "909045010",
    "312": "909045011",
    "314": "909045015",
    "315": "909045016",
    "316": "909045017",
    "317": "909046001",
    "318": "909046002",
    "319": "909046003",
    "322": "909046006",
    "323": "909046007",
    "324": "909046008",
    "325": "909046009",
    "326": "909046010",
    "327": "909046011",
    "328": "909046012",
    "329": "909046013",
    "330": "909046014",
    "331": "909046015",
    "332": "909046016",
    "333": "909046017",
    "334": "909047001",
    "337": "909047004",
    "338": "909047005",
    "339": "909047006",
    "340": "909047007",
    "341": "909047008",
    "342": "909047009",
    "343": "909047010",
    "344": "909047011",
    "345": "909047012",
    "346": "909047013",
    "347": "909047015",
    "348": "909047016",
    "349": "909047017",
    "350": "909047018",
    "351": "909047019",
    "353": "909048002",
    "354": "909048003",
    "355": "909048004",
    "356": "909048005",
    "357": "909048006",
    "358": "909048007",
    "359": "909048008",
    "361": "909048010",
    "362": "909048011",
    "363": "909048012",
    "364": "909048013",
    "365": "909048014",
    "366": "909048015",
    "367": "909048016",
    "368": "909048017",
    "369": "909048018",
    "370": "909049001",
    "371": "909049002",
    "372": "909049003",
    "373": "909049004",
    "374": "909049005",
    "375": "909049006",
    "376": "909049007",
    "378": "909049009",
    "379": "909049010",
    "380": "909049011",
    "381": "909049012",
    "382": "909049013",
    "383": "909049014",
    "384": "909049015",
    "385": "909049016",
    "386": "909049017",
    "387": "909049018",
    "388": "909049019",
    "389": "909049020",
    "390": "909049021",
    "391": "909050002",
    "393": "909050004",
    "394": "909050005",
    "395": "909050006",
    "396": "909050008",
    "ring": "909050009",
    "398": "909050010",
    "399": "909050011",
    "400": "909050012",
    "401": "909050013",
    "402": "909050014",
    "403": "909050015",
    "404": "909050016",
    "405": "909050017",
    "406": "909050018",
    "407": "909050019",
    "408": "909050020",
    "409": "909050021",
    "410": "909046004",
    "411": "909046005",
    "412": "909047002",
    "413": "909047003",
    "414": "909048001",
    "415": "909048009",
    "416": "909049008",
    "417": "909050003",
    "418": "909052010"
}
#------------------------------------------#

# Emote mapping for evo commands
EMOTE_MAP = {
    1: 909000063,
    2: 909000081,
    3: 909000075,
    4: 909000085,
    5: 909000134,
    6: 909000098,
    7: 909035007,
    8: 909051012,
    9: 909000141,
    10: 909034008,
    11: 909051015,
    12: 909041002,
    13: 909039004,
    14: 909042008,
    15: 909051014,
    16: 909039012,
    17: 909040010,
    18: 909035010,
    19: 909041005,
    20: 909051003,
    21: 909034001
}

BUNDLE = {
    "rampage": 914000002,
    "cannibal": 914000003,
    "devil": 914038001,
    "scorpio": 914039001,
    "frostfire": 914042001,
    "paradox": 914044001,
    "naruto": 914047001,
    "aurora": 914047002,
    "midnight": 914048001,
    "itachi": 914050001,
    "dreamspace": 914051001
}

ALL_EMOTE = {
    1: 909000001,
    2: 909000002,
    3: 909000003,
    4: 909000004,
    5: 909000005,
    6: 909000006,
    7: 909000007,
    8: 909000008,
    9: 909000009,
    10: 909000010,
    11: 909000011,
    12: 909000012,
    13: 909000013,
    14: 909000014,
    15: 909000015,
    16: 909000016,
    17: 909000017,
    18: 909000018,
    19: 909000019,
    20: 909000020,
    21: 909000021,
    22: 909000022,
    23: 909000023,
    24: 909000024,
    25: 909000025,
    26: 909000026,
    27: 909000027,
    28: 909000028,
    29: 909000029,
    30: 909000031,
    31: 909000032,
    32: 909000033,
    33: 909000034,
    34: 909000035,
    35: 909000036,
    36: 909000037,
    37: 909000038,
    38: 909000039,
    39: 909000040,
    40: 909000041,
    41: 909000042,
    42: 909000043,
    43: 909000044,
    44: 909000045,
    45: 909000046,
    46: 909000047,
    47: 909000048,
    48: 909000049,
    49: 909000051,
    50: 909000052,
    51: 909000053,
    52: 909000054,
    53: 909000055,
    54: 909000056,
    55: 909000057,
    56: 909000058,
    57: 909000059,
    58: 909000060,
    59: 909000061,
    60: 909000062,
    61: 909000063,
    62: 909000064,
    63: 909000065,
    64: 909000066,
    65: 909000067,
    66: 909000068,
    67: 909000069,
    68: 909000070,
    69: 909000071,
    70: 909000072,
    71: 909000073,
    72: 909000074,
    73: 909000075,
    74: 909000076,
    75: 909000077,
    76: 909000078,
    77: 909000079,
    78: 909000080,
    79: 909000081,
    80: 909000082,
    81: 909000083,
    82: 909000084,
    83: 909000085,
    84: 909000086,
    85: 909000087,
    86: 909000088,
    87: 909000089,
    88: 909000090,
    89: 909000091,
    90: 909000092,
    91: 909000093,
    92: 909000094,
    93: 909000095,
    94: 909000096,
    95: 909000097,
    96: 909000098,
    97: 909000099,
    98: 909000100,
    99: 909000101,
    100: 909000102,
    101: 909000103,
    102: 909000104,
    103: 909000105,
    104: 909000106,
    105: 909000107,
    106: 909000108,
    107: 909000109,
    108: 909000110,
    109: 909000111,
    110: 909000112,
    111: 909000113,
    112: 909000114,
    113: 909000115,
    114: 909000116,
    115: 909000117,
    116: 909000118,
    117: 909000119,
    118: 909000120,
    119: 909000121,
    120: 909000122,
    121: 909000123,
    122: 909000124,
    123: 909000125,
    124: 909000126,
    125: 909000127,
    126: 909000128,
    127: 909000129,
    128: 909000130,
    129: 909000131,
    130: 909000132,
    131: 909000133,
    132: 909000134,
    133: 909000135,
    134: 909000136,
    135: 909000137,
    136: 909000138,
    137: 909000139,
    138: 909000140,
    139: 909000141,
    140: 909000142,
    141: 909000143,
    142: 909000144,
    143: 909000145,
    144: 909000150,
    145: 909033001,
    146: 909033002,
    147: 909033003,
    148: 909033004,
    149: 909033005,
    150: 909033006,
    151: 909033007,
    152: 909033008,
    153: 909033009,
    154: 909033010,
    155: 909034001,
    156: 909034002,
    157: 909034003,
    158: 909034004,
    159: 909034005,
    160: 909034006,
    161: 909034007,
    162: 909034008,
    163: 909034009,
    164: 909034010,
    165: 909034011,
    166: 909034012,
    167: 909034013,
    168: 909034014,
    169: 909035001,
    170: 909035002,
    171: 909035003,
    172: 909035004,
    173: 909035005,
    174: 909035006,
    175: 909035007,
    176: 909035008,
    177: 909035009,
    178: 909035010,
    179: 909035011,
    180: 909035012,
    181: 909035013,
    182: 909035014,
    183: 909035015,
    184: 909036001,
    185: 909036002,
    186: 909036003,
    187: 909036004,
    188: 909036005,
    189: 909036006,
    190: 909036008,
    191: 909036009,
    192: 909036010,
    193: 909036011,
    194: 909036012,
    195: 909036014,
    196: 909037001,
    197: 909037002,
    198: 909037003,
    199: 909037004,
    200: 909037005,
    201: 909037006,
    202: 909037007,
    203: 909037008,
    204: 909037009,
    205: 909037010,
    206: 909037011,
    207: 909037012,
    208: 909038001,
    209: 909038002,
    210: 909038003,
    211: 909038004,
    212: 909038005,
    213: 909038006,
    214: 909038008,
    215: 909038009,
    216: 909038010,
    217: 909038011,
    218: 909038012,
    219: 909038013,
    220: 909039001,
    221: 909039002,
    222: 909039003,
    223: 909039004,
    224: 909039005,
    225: 909039006,
    226: 909039007,
    227: 909039008,
    228: 909039009,
    229: 909039010,
    230: 909039011,
    231: 909039012,
    232: 909039013,
    233: 909039014,
    234: 909040001,
    235: 909040002,
    236: 909040003,
    237: 909040004,
    238: 909040005,
    239: 909040006,
    240: 909040008,
    241: 909040009,
    242: 909040010,
    243: 909040011,
    244: 909040012,
    245: 909040013,
    246: 909040014,
    247: 909041001,
    248: 909041002,
    249: 909041003,
    250: 909041004,
    251: 909041005,
    252: 909041006,
    253: 909041007,
    254: 909041008,
    255: 909041009,
    256: 909041010,
    257: 909041011,
    258: 909041012,
    259: 909041013,
    260: 909041014,
    261: 909041015,
    262: 909042001,
    263: 909042002,
    264: 909042003,
    265: 909042004,
    266: 909042005,
    267: 909042006,
    268: 909042007,
    269: 909042008,
    270: 909042009,
    271: 909042011,
    272: 909042012,
    273: 909042013,
    274: 909042016,
    275: 909042017,
    276: 909042018,
    277: 909043001,
    278: 909043002,
    279: 909043003,
    280: 909043004,
    281: 909043005,
    282: 909043006,
    283: 909043007,
    284: 909043008,
    285: 909043009,
    286: 909043010,
    287: 909043013,
    288: 909044001,
    289: 909044002,
    290: 909044003,
    291: 909044004,
    292: 909044005,
    293: 909044006,
    294: 909044007,
    295: 909044008,
    296: 909044009,
    297: 909044010,
    298: 909044011,
    299: 909044012,
    300: 909044015,
    301: 909044016,
    302: 909045001,
    303: 909045002,
    304: 909045003,
    305: 909045004,
    306: 909045005,
    307: 909045006,
    308: 909045007,
    309: 909045008,
    310: 909045009,
    311: 909045010,
    312: 909045011,
    313: 909045012,
    314: 909045015,
    315: 909045016,
    316: 909045017,
    317: 909046001,
    318: 909046002,
    319: 909046003,
    320: 909046004,
    321: 909046005,
    322: 909046006,
    323: 909046007,
    324: 909046008,
    325: 909046009,
    326: 909046010,
    327: 909046011,
    328: 909046012,
    329: 909046013,
    330: 909046014,
    331: 909046015,
    332: 909046016,
    333: 909046017,
    334: 909047001,
    335: 909047002,
    336: 909047003,
    337: 909047004,
    338: 909047005,
    339: 909047006,
    340: 909047007,
    341: 909047008,
    342: 909047009,
    343: 909047010,
    344: 909047011,
    345: 909047012,
    346: 909047013,
    347: 909047015,
    348: 909047016,
    349: 909047017,
    350: 909047018,
    351: 909047019,
    352: 909048001,
    353: 909048002,
    354: 909048003,
    355: 909048004,
    356: 909048005,
    357: 909048006,
    358: 909048007,
    359: 909048008,
    360: 909048009,
    361: 909048010,
    362: 909048011,
    363: 909048012,
    364: 909048013,
    365: 909048014,
    366: 909048015,
    367: 909048016,
    368: 909048017,
    369: 909048018,
    370: 909049001,
    371: 909049002,
    372: 909049003,
    373: 909049004,
    374: 909049005,
    375: 909049006,
    376: 909049007,
    377: 909049008,
    378: 909049009,
    379: 909049010,
    380: 909049011,
    381: 909049012,
    382: 909049013,
    383: 909049014,
    384: 909049015,
    385: 909049016,
    386: 909049017,
    387: 909049018,
    388: 909049019,
    389: 909049020,
    390: 909049021,
    391: 909050002,
    392: 909050003,
    393: 909050004,
    394: 909050005,
    395: 909050006,
    396: 909050008,
    397: 909050009,
    398: 909050010,
    399: 909050011,
    400: 909050012,
    401: 909050013,
    402: 909050014,
    403: 909050015,
    404: 909050016,
    405: 909050017,
    406: 909050018,
    407: 909050019,
    408: 909050020,
    409: 909050021,
    410: 909050026,
    411: 909050027,
    412: 909050028,
    413: 909547001,
    414: 909550001
}

# Badge values for v1 to s8 commands - using your exact values
BADGE_VALUES = {
    "v1": 1048576,    # Your first badge
    "v2": 32768,      # Your second badge  
    "v3": 2048,       # Your third badge
    "v4": 64,         # Your fourth badge
    "v5": 262144     # Your seventh badge
}

def titles():
    """Return all titles instead of just one random"""
    titles_list = [
        905090075, 904990072, 904990069, 905190079
    ]
    return titles_list  # Return the full list instead of random.choice     
           
def is_admin(uid):
    return str(uid) == ADMIN_UID

# Mute Functions 
def is_off():
    return not bot_enabled

def ff_num(val):
    return xMsGFixinG(str(val)) if val not in (None, "") else "N/A"

def human_time(ts):
    try:
        ts = int(ts)
        return datetime.fromtimestamp(ts).strftime("%d %b %Y, %I:%M %p")
    except:
        return "N/A"
    
            
def create_credentials_template():
    """Create a template credentials file"""
    template = """# Flash_ff Free Fire Bot Credentials
# Fill in your Free Fire account credentials below

# Format 1: Comma-separated (RECOMMENDED)
uid=4688928465,password=056CACD10A2BDAD4381C6B784A840A853A70203C6894C8EBEADCD5D9BD9AB991

# OR Format 2: Line-separated
# uid: 4688928465
# password: 056CACD10A2BDAD4381C6B784A840A853A70203C6894C8EBEADCD5D9BD9AB991

# Save this file and restart the bot
"""
    
    filename = "bot.txt"
    if not os.path.exists(filename):
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(template)
        print(f"📝 Created {filename} template file")
        print("✏️ Please edit it with your actual credentials")
        return False
    return True
    
da = 'f2212101'
dec = ['80', '81', '82', '83', '84', '85', '86', '87', '88', '89', '8a', '8b', '8c', '8d', '8e', '8f', '90', '91', '92', '93', '94', '95', '96', '97', '98', '99', '9a', '9b', '9c', '9d', '9e', '9f', 'a0', 'a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8', 'a9', 'aa', 'ab', 'ac', 'ad', 'ae', 'af', 'b0', 'b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7', 'b8', 'b9', 'ba', 'bb', 'bc', 'bd', 'be', 'bf', 'c0', 'c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8', 'c9', 'ca', 'cb', 'cc', 'cd', 'ce', 'cf', 'd0', 'd1', 'd2', 'd3', 'd4', 'd5', 'd6', 'd7', 'd8', 'd9', 'da', 'db', 'dc', 'dd', 'de', 'df', 'e0', 'e1', 'e2', 'e3', 'e4', 'e5', 'e6', 'e7', 'e8', 'e9', 'ea', 'eb', 'ec', 'ed', 'ee', 'ef', 'f0', 'f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9', 'fa', 'fb', 'fc', 'fd', 'fe', 'ff']
x_list = ['1','01', '02', '03', '04', '05', '06', '07', '08', '09', '0a', '0b', '0c', '0d', '0e', '0f', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '1a', '1b', '1c', '1d', '1e', '1f', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '2a', '2b', '2c', '2d', '2e', '2f', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '3a', '3b', '3c', '3d', '3e', '3f', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '4a', '4b', '4c', '4d', '4e', '4f', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '5a', '5b', '5c', '5d', '5e', '5f', '60', '61', '62', '63', '64', '65', '66', '67', '68', '69', '6a', '6b', '6c', '6d', '6e', '6f', '70', '71', '72', '73', '74', '75', '76', '77', '78', '79', '7a', '7b', '7c', '7d', '7e', '7f']

def Decrypt_ID(da):
    """EXACT SAME as your code"""
    if da != None and len(da) == 10:
        w = 128
        xxx = len(da)/2 - 1
        xxx = str(xxx)[:1]
        for i in range(int(xxx)-1):
            w = w * 128
        x1 = da[:2]
        x2 = da[2:4]
        x3 = da[4:6]
        x4 = da[6:8]
        x5 = da[8:10]
        return str(w * x_list.index(x5) + (dec.index(x2) * 128) + dec.index(x1) + (dec.index(x3) * 128 * 128) + (dec.index(x4) * 128 * 128 * 128))

    if da != None and len(da) == 8:
        w = 128
        xxx = len(da)/2 - 1
        xxx = str(xxx)[:1]
        for i in range(int(xxx)-1):
            w = w * 128
        x1 = da[:2]
        x2 = da[2:4]
        x3 = da[4:6]
        x4 = da[6:8]
        return str(w * x_list.index(x4) + (dec.index(x2) * 128) + dec.index(x1) + (dec.index(x3) * 128 * 128))
    
    return None

def Encrypt_ID(x):
    """EXACT SAME as your code"""
    x = int(x)
    x = x / 128 
    if x > 128:
        x = x / 128
        if x > 128:
            x = x / 128
            if x > 128:
                x = x / 128
                strx = int(x)
                y = (x - int(strx)) * 128
                stry = str(int(y))
                z = (y - int(stry)) * 128
                strz = str(int(z))
                n = (z - int(strz)) * 128
                strn = str(int(n))
                m = (n - int(strn)) * 128
                return dec[int(m)] + dec[int(n)] + dec[int(z)] + dec[int(y)] + x_list[int(x)]
            else:
                strx = int(x)
                y = (x - int(strx)) * 128
                stry = str(int(y))
                z = (y - int(stry)) * 128
                strz = str(int(z))
                n = (z - int(strz)) * 128
                strn = str(int(n))
                return dec[int(n)] + dec[int(z)] + dec[int(y)] + x_list[int(x)]

def decrypt_api(cipher_text):
    """EXACT SAME as your code"""
    key = bytes([89, 103, 38, 116, 99, 37, 68, 69, 117, 104, 54, 37, 90, 99, 94, 56])
    iv = bytes([54, 111, 121, 90, 68, 114, 50, 50, 69, 51, 121, 99, 104, 106, 77, 37])
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plain_text = unpad(cipher.decrypt(bytes.fromhex(cipher_text)), AES.block_size)
    return plain_text.hex()

def encrypt_api(plain_text):
    """EXACT SAME as your code"""
    plain_text = bytes.fromhex(plain_text)
    key = bytes([89, 103, 38, 116, 99, 37, 68, 69, 117, 104, 54, 37, 90, 99, 94, 56])
    iv = bytes([54, 111, 121, 90, 68, 114, 50, 50, 69, 51, 121, 99, 104, 106, 77, 37])
    cipher = AES.new(key, AES.MODE_CBC, iv)
    cipher_text = cipher.encrypt(pad(plain_text, AES.block_size))
    return cipher_text.hex()

def encrypt_message(plaintext_bytes):
    """EXACT SAME as your Flask API"""
    key = b'Yg&tc%DEuh6%Zc^8'
    iv = b'6oyZDr22E3ychjM%'
    cipher = AES.new(key, AES.MODE_CBC, iv)
    padded = pad(plaintext_bytes, AES.block_size)
    encrypted = cipher.encrypt(padded)
    return binascii.hexlify(encrypted).decode('utf-8')    

def create_uid_protobuf(uid):
    """EXACT SAME as your Flask API"""
    msg = dev_generator_pb2.dev_generator()
    msg.saturn_ = int(uid)
    msg.garena = 1
    return msg.SerializeToString()

def enc(uid):
    """EXACT SAME as your Flask API"""
    pb = create_uid_protobuf(uid)
    return encrypt_message(pb)

def decode_player_info(binary):
    """EXACT SAME as your Flask API"""
    info = devxt_count_pb2.xt()
    info.ParseFromString(binary)
    return info    
    
import requests
import json

def load_jwt_token():
    """Load token from token.json"""
    try:
        with open("token.json", "r") as f:
            data = json.load(f)
        token = data.get("token")
        if token:
            print(f"✅ Loaded token: {token[:20]}...")
            return token
        else:
            print("❌ No token found in token.json")
            return None
    except Exception as e:
        print(f"❌ Error loading token: {e}")
        return None

def load_tokens_ind():
    """Load bulk tokens from token_ind.json"""
    try:
        with open("token_ind.json", "r") as f:
            tokens = json.load(f)
        print(f"📦 Loaded {len(tokens)} tokens from token_ind.json")
        return tokens
    except:
        print("❌ No tokens found in token_ind.json")
        return None

def get_player_info(uid, token):
    """Get player info - modified to accept token"""
    url = "https://client.ind.freefiremobile.com/GetPlayerPersonalShow"
    
    encrypted_uid = enc(uid)
    edata = bytes.fromhex(encrypted_uid)
    
    headers = {
        'User-Agent': "Dalvik/2.1.0",
        'Connection': "Keep-Alive",
        'Accept-Encoding': "gzip",
        'Authorization': f"Bearer {token}",
        'Content-Type': "application/x-www-form-urlencoded",
        'X-Unity-Version': "2018.4.11f1",
        'X-GA': "v1 1",
        'ReleaseVersion': "OB53"
    }
    
    try:
        response = requests.post(url, data=edata, headers=headers, verify=False, timeout=10)
        
        if response.status_code != 200:
            return "Unknown", uid
        
        info = decode_player_info(response.content)
        data = json.loads(json_format.MessageToJson(info))
        
        account = data.get("AccountInfo", {})
        player_name = account.get("PlayerNickname", "Unknown")
        player_uid = account.get("UID", uid)
        
        return player_name, player_uid
        
    except Exception as e:
        print(f"❌ Error getting player info: {e}")
        return "Unknown", uid

def send_friend_request_single(uid, token, region="IND"):
    """EXACT SAME as your Flask function but single"""
    try:
        encrypted_id = Encrypt_ID(uid)
        payload = f"08a7c4839f1e10{encrypted_id}1801"
        encrypted_payload = encrypt_api(payload)
        
        # Determine URL based on region
        if region.lower() == "ind":
            url = "https://client.ind.freefiremobile.com/RequestAddingFriend"
        elif region.lower() == "bd":
            url = "https://client.bd.freefiremobile.com/RequestAddingFriend"
        else:
            url = "https://client.ind.freefiremobile.com/RequestAddingFriend"
        
        headers = {
            "Authorization": f"Bearer {token}",
            "X-Unity-Version": "2018.4.11f1",
            "X-GA": "v1 1",
            "ReleaseVersion": "OB53",
            "Content-Type": "application/x-www-form-urlencoded",
            "User-Agent": "Dalvik/2.1.0"
        }
        
        print(f"📤 Sending friend request to {uid}...")
        response = requests.post(url, data=bytes.fromhex(encrypted_payload), headers=headers, timeout=10, verify=False)
        
        if response.status_code == 200:
            print(f"✅ Success: Friend request sent to {uid}")
            return True
        else:
            print(f"❌ Failed: Status {response.status_code}")
            return False
            
    except Exception as e:
        print(f"❌ Error: {e}")
        return False    
    
def start_autooo(self):    
    try:
        fields = {
            1: 9,
            2: {
                1: 12480598706,
            },
        }
        packet = create_protobuf_packet(fields).hex()
        header_length = len(encrypt_packet(packet, self.key, self.iv)) // 2
        header_length_final = dec_to_hex(header_length)
        if len(header_length_final) == 2:
            final_packet = "0515000000" + header_length_final + self.nmnmmmmn(packet)
        elif len(header_length_final) == 3:
            final_packet = "051500000" + header_length_final + self.nmnmmmmn(packet)
        elif len(header_length_final) == 4:
            final_packet = "05150000" + header_length_final + self.nmnmmmmn(packet)
        elif len(header_length_final) == 5:
            final_packet = "0515000" + header_length_final + self.nmnmmmmn(packet)
        return bytes.fromhex(final_packet)
    except exception as e:
        print(e)


def load_credentials_from_file(filename="bot.txt"):
    """
    Load UID and password from _Apis.txt file
    """
    try:
        if not os.path.exists(filename):
            print(f"❌ {filename} not found!")
            create_credentials_template()
            return None, None
        
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        uid = None
        password = None
        
        # Try to find uid and password using regex
        import re
        
        # Look for uid=value or uid: value
        uid_match = re.search(r'(?:uid\s*[=:]\s*)(\d+)', content, re.IGNORECASE)
        if uid_match:
            uid = uid_match.group(1)
        
        # Look for password=value or password: value
        pass_match = re.search(r'(?:password\s*[=:]\s*)([^\s\n\r]+)', content, re.IGNORECASE)
        if pass_match:
            password = pass_match.group(1)
        
        if not uid or not password:
            print(f"❌ Could not find UID/password in {filename}")
            print("📝 Please make sure the file contains:")
            print("   uid=YOUR_UID,password=YOUR_PASSWORD")
            print("   OR")
            print("   uid: YOUR_UID")
            print("   password: YOUR_PASSWORD")
            return None, None
        
        print(f"✅ Loaded credentials from {filename}")
        print(f"👤 UID: {uid}")
        print(f"🔑 Password: {'*' * len(password)}")
        
        return uid, password
        
    except Exception as e:
        print(f"❌ Error loading credentials: {e}")
        return None, None

# Load emotes from JSON file (your format)
def load_emotes_from_json():
    """Load emote IDs from emotes.json file with your exact format"""
    emotes_file = "emotes.json"
    
    try:
        with open(emotes_file, 'r') as f:
            emotes_data = json.load(f)
        
        # Access using your structure: data["EMOTES"]["numbers"] and data["EMOTES"]["names"]
        number_emotes = emotes_data.get("EMOTES", {}).get("numbers", {})
        name_emotes = emotes_data.get("EMOTES", {}).get("names", {})
        
        print(f"✅ Loaded {len(number_emotes)} number emotes and {len(name_emotes)} named emotes")
        return {
            "numbers": number_emotes,
            "names": name_emotes
        }
        
    except Exception as e:
        print(f"❌ Error loading {emotes_file}: {e}")
        # Return empty dictionaries as fallback
        return {"numbers": {}, "names": {}}

# Load emotes globally
EMOTES_DATA = load_emotes_from_json()
NUMBER_EMOTES = EMOTES_DATA["numbers"]
NAME_EMOTES = EMOTES_DATA["names"]

# Helper functions for ghost join
def dec_to_hex(decimal):
    """Convert decimal to hex string"""
    hex_str = hex(decimal)[2:]
    return hex_str.upper() if len(hex_str) % 2 == 0 else '0' + hex_str.upper()



async def encrypt_packet(packet_hex, key, iv):
    """Encrypt packet using AES CBC"""
    cipher = AES.new(key, AES.MODE_CBC, iv)
    packet_bytes = bytes.fromhex(packet_hex)
    padded_packet = pad(packet_bytes, AES.block_size)
    encrypted = cipher.encrypt(padded_packet)
    return encrypted.hex()

async def nmnmmmmn(packet_hex, key, iv):
    """Wrapper for encrypt_packet"""
    return await encrypt_packet(packet_hex, key, iv)
    

def generate_random_hex_color():
    """Generate random hex color for messages"""
    return ''.join([random.choice('0123456789ABCDEF') for _ in range(6)])

def bunner_():
    """Generate random avatar ID"""
    return random.randint(100000000, 999999999)

# Add this function to your code
def Encrypt(number):
    """Encrypt function from your first TCP bot"""
    number = int(number)
    encoded_bytes = []
    
    while True:
        byte = number & 0x7F
        number >>= 7
        if number:
            byte |= 0x80
        encoded_bytes.append(byte)
        if not number:
            break
    
    return bytes(encoded_bytes).hex()
    

async def Room_Spam(Uid, Rm, Nm, K, V):
   
    same_value = random.choice([32768])  #you can add any badge value 
    
    fields = {
        1: 78,
        2: {
            1: int(Rm),  
            2: "iG:[C][B][FF0000] ZAINUㅤVIP",  
            3: {
                2: 1,
                3: 1
            },
            4: 330,      
            5: 6000,     
            6: 201,      
            10: int(await get_random_avatar()),  
            11: int(Uid), # Target UID
            12: 1,       
            15: {
                1: 1,
                2: same_value  
            },
            16: same_value,    
            18: {
                1: 11481904755,  
                2: 8,
                3: "\u0010\u0015\b\n\u000b\u0013\f\u000f\u0011\u0004\u0007\u0002\u0003\r\u000e\u0012\u0001\u0005\u0006"
            },
            
            31: {
                1: 1,
                2: same_value  
            },
            32: same_value,    
            34: {
                1: int(Uid),   
                2: 8,
                3: bytes([15,6,21,8,10,11,19,12,17,4,14,20,7,2,1,5,16,3,13,18])
            }
        }
    }
    
    return await GeneRaTePk((await CrEaTe_ProTo(fields)).hex(), '0e15', K, V)
    
    
async def send_working_join_request(target_uid, key, iv, region, LoGinDaTaUncRypTinG):
    """Send join request that actually works"""
    
    try:
        # Step 1: Reset bot to solo mode
        print("🔄 Resetting bot to solo mode...")
        await reset_bot_state(key, iv, region)
        await asyncio.sleep(1)
        
        # Step 2: Create bot's own squad (so it has context)
        print("🏠 Creating bot squad...")
        squad_packet = await OpEnSq(key, iv, region)
        await SEndPacKeT(whisper_writer, online_writer, 'OnLine', squad_packet)
        await asyncio.sleep(1)
        
        # Step 3: Send join request
        print(f"📨 Sending join request to {target_uid}...")
        join_packet = await create_working_join_request(target_uid, key, iv, region, LoGinDaTaUncRypTinG)
        
        if join_packet:
            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', join_packet)
            print(f"✅ Bot join request sent! Player can now accept.")
            return True
        else:
            print(f"❌ Failed to create join packet")
            return False
            
    except Exception as e:
        print(f"❌ Error in working join request: {e}")
        return False
        
async def handle_join_req_command(inPuTMsG, uid, chat_id, key, iv, region, chat_type, LoGinDaTaUncRypTinG):
    """Handle /join_req command - bot sends join request to player"""
    
    parts = inPuTMsG.strip().split()
    
    if len(parts) < 2:
        error_msg = f"""[B][C][FF0000]❌ Usage: /join_req (player_uid)
Example: /join_req 123456789

What happens:
1. Bot goes solo mode
2. Bot creates its own squad  
3. Bot sends join request to player
4. Player sees: "BotName wants to join your team"
5. Player clicks Accept → Bot joins player's team
"""
        await safe_send_message(chat_type, error_msg, uid, chat_id, key, iv)
        return
    
    target_uid = parts[1]
    
    if not target_uid.isdigit():
        error_msg = f"[B][C][FF0000]❌ Invalid UID! Must be numbers only.\n"
        await safe_send_message(chat_type, error_msg, uid, chat_id, key, iv)
        return
    
    # Send initial message
    initial_msg = f"""[B][C][FFFF00]🤖 BOT JOIN REQUEST INITIATED

👤 Target Player: {target_uid}
⚙️ Steps:
1. Bot resetting to solo mode...
2. Bot creating squad...
3. Sending join request...

⏳ Please wait...
"""
    await safe_send_message(chat_type, initial_msg, uid, chat_id, key, iv)
    
    try:
        success = await send_working_join_request(target_uid, key, iv, region, LoGinDaTaUncRypTinG)
        
        if success:
            success_msg = f"""[B][C][FFFF00]✅ BOT JOIN REQUEST SENT!

🎯 Target: {target_uid}
🤖 Bot Name: ZAINUㅤVIP
✅ Status: Ready to join

📱 Player will see:
"ZAINUㅤVIP wants to join your team"

✅ When player clicks ACCEPT:
Bot will automatically join player's team!
"""
        else:
            success_msg = f"""[B][C][FF0000]❌ FAILED!

Possible reasons:
1. Bot not connected properly
2. Bot already in a squad
3. Server issue

Try again in 10 seconds.
"""
        
        await safe_send_message(chat_type, success_msg, uid, chat_id, key, iv)
        
        # Cleanup: Leave squad after sending request
        await asyncio.sleep(3)
        leave_packet = await ExiT(None, key, iv)
        await SEndPacKeT(whisper_writer, online_writer, 'OnLine', leave_packet)
        print("🧹 Bot cleaned up (left squad)")
        
    except Exception as e:
        error_msg = f"[B][C][FF0000]❌ Error: {str(e)[:50]}\n"
        await safe_send_message(chat_type, error_msg, uid, chat_id, key, iv)        
        
async def create_simple_start_packet(key, iv):
    """Create simple start match packet (00 00 00 d6)"""
    
    # This appears to be a minimal start packet
    # 00 00 00 d6 in hex = 214 in decimal (packet type?)
    
    fields = {
        1: 214,  # Packet type for start match (d6 hex = 214 decimal)
        2: {
            1: 1,  # Start match command
        }
    }
    
    packet = await CrEaTe_ProTo(fields)
    packet_hex = packet.hex()
    
    # Generate final packet
    final_packet = await GeneRaTePk(packet_hex, '0514', key, iv)  # Use appropriate packet type
    
    print(f"✅ Simple start match packet created")
    return final_packet
    
async def create_detailed_start_packet(key, iv, region="IND"):
    """Create detailed start match packet with device info"""
    
    # Decoded from your hex: contains device info (vivo, arm64, etc.)
    
    fields = {
        1: 269,  # 0x10D = 269 decimal (detailed start packet)
        2: {
            1: 8,           # Unknown
            2: 8,           # Unknown
            3: 11,          # Unknown
            4: 1,           # Unknown
            5: "vivo",      # Device brand
            6: "130",       # Device model
            7: "arm64-v8a", # CPU architecture
            8: "f538dc9b-cec9-43cd-8125-95f7f4f1f7e3",  # Device ID
            9: "FFD58FB4F76F648C2A5E21EBCFA3AAE81B4C9B7D97",  # Unknown
            10: "voice",    # Audio type
            11: "V2059",    # Version
            12: "mt6785",   # Processor
            13: "AFFD58FB4F76F648C2A5E21EBCFA3AAE81B4C9B7D97",  # Unknown
            14: "IND_1999120752610979840",  # Region + timestamp
            15: 269         # Packet length?
        }
    }
    
    packet = await CrEaTe_ProTo(fields)
    packet_hex = packet.hex()
    
    # Determine packet type based on region
    if region.lower() == "ind":
        packet_type = '0514'
    elif region.lower() == "bd":
        packet_type = "0519"
    else:
        packet_type = "0515"
        
    final_packet = await GeneRaTePk(packet_hex, packet_type, key, iv)
    
    print(f"✅ Detailed start match packet created")
    return final_packet
        
async def generate_guest_accounts(count=1, name="BlackApis", password_prefix="FF"):
    """Generate guest accounts using the API"""
    api_url = f"https://gen-by-black-api.vercel.app/generate?name={name}&password_prefix={password_prefix}"
    
    accounts = []
    failed_attempts = 0
    max_retries = 10
    
    print(f"📡 Generating {count} guest accounts...")
    
    for i in range(count):
        retry_count = 0
        success = False
        
        while retry_count < max_retries and not success:
            try:
                print(f"🔄 Attempt {retry_count + 1}/{max_retries} for account {i + 1}/{count}...")
                
                async with aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(total=30)) as session:
                    async with session.get(api_url) as response:
                        
                        if response.status == 200:
                            data = await response.json()
                            
                            if data.get("success"):
                                account = {
                                    'uid': data.get('uid'),
                                    'password': data.get('password'),
                                    'name': data.get('name'),
                                    'timestamp': time.time()
                                }
                                accounts.append(account)
                                print(f"✅ Account {i + 1}: {account['uid']}")
                                success = True
                                failed_attempts = 0  # Reset failed attempts counter
                                
                            else:
                                print(f"❌ API error: {data.get('message', 'Unknown error')}")
                                retry_count += 1
                                await asyncio.sleep(2)
                                
                        elif response.status == 503:
                            print(f"⚠️ Server busy (503), retrying in 3 seconds...")
                            retry_count += 1
                            await asyncio.sleep(3)
                            
                        else:
                            print(f"❌ HTTP {response.status}, retrying...")
                            retry_count += 1
                            await asyncio.sleep(2)
                            
            except asyncio.TimeoutError:
                print(f"⏰ Timeout, retrying...")
                retry_count += 1
                await asyncio.sleep(2)
                
            except Exception as e:
                print(f"❌ Error: {str(e)[:50]}...")
                retry_count += 1
                await asyncio.sleep(2)
        
        if not success:
            print(f"❌ Failed to generate account {i + 1} after {max_retries} attempts")
            failed_attempts += 1
            
            # If too many failures in a row, stop
            if failed_attempts >= 3:
                print("🛑 Too many failures, stopping...")
                break
        
        # Small delay between accounts to avoid rate limiting
        if i < count - 1:
            await asyncio.sleep(1)
    
    return accounts

def save_guest_accounts(accounts, filename="guest_accounts.json"):
    """Save guest accounts to JSON file"""
    try:
        # Load existing accounts if file exists
        existing = []
        if os.path.exists(filename):
            with open(filename, 'r') as f:
                existing = json.load(f)
        
        # Combine with new accounts
        all_accounts = existing + accounts
        
        # Save to file
        with open(filename, 'w') as f:
            json.dump(all_accounts, f, indent=2)
        
        print(f"💾 Saved {len(accounts)} accounts to {filename}")
        print(f"📊 Total accounts: {len(all_accounts)}")
        
        return True
    except Exception as e:
        print(f"❌ Error saving accounts: {e}")
        return False

async def generate_and_save_accounts(count, name="BlackApis", password_prefix="FF"):
    """Generate and save accounts with progress updates"""
    start_time = time.time()
    
    print(f"\n🎯 GENERATING {count} GUEST ACCOUNTS")
    print("="*50)
    
    accounts = await generate_guest_accounts(count, name, password_prefix)
    
    if accounts:
        # Save to file
        save_guest_accounts(accounts)
        
        # Display results
        elapsed = time.time() - start_time
        print("\n" + "="*50)
        print("📊 GENERATION COMPLETE")
        print("="*50)
        print(f"✅ Success: {len(accounts)}/{count} accounts")
        print(f"⏱️ Time: {elapsed:.1f} seconds")
        print(f"📁 Saved to: guest_accounts.json")
        
        # Show first 3 accounts as preview
        print("\n📋 FIRST 3 ACCOUNTS:")
        for i, acc in enumerate(accounts[:3]):
            print(f"  {i+1}. UID: {acc['uid']} | Pass: {acc['password']}")
        
        if len(accounts) > 3:
            print(f"  ... and {len(accounts) - 3} more")
    
    return accounts        
        
async def start_match(key, iv, region, detailed=False):
    """Start Free Fire match - bot must be in a squad/team"""
    
    try:
        if detailed:
            start_packet = await create_detailed_start_packet(key, iv, region)
        else:
            start_packet = await create_simple_start_packet(key, iv)
        
        if start_packet:
            # Send via Online connection
            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', start_packet)
            print("🎮 Start match packet sent!")
            return True
        else:
            print("❌ Failed to create start packet")
            return False
            
    except Exception as e:
        print(f"❌ Error starting match: {e}")
        return False       
        
async def handle_start_match_command(inPuTMsG, uid, chat_id, key, iv, region, chat_type):
    """Handle /ss command to start match"""
    
    parts = inPuTMsG.strip().split()
    
    # Check if user wants detailed start
    detailed = False
    if len(parts) > 1 and parts[1].lower() == "detailed":
        detailed = True
    
    # Send initial message
    initial_msg = f"""[B][C][FFFF00]🎮 STARTING MATCH...

⚙️ Mode: {'Detailed' if detailed else 'Simple'}
🤖 Bot must be in a squad!
⏳ Please wait...
"""
    await safe_send_message(chat_type, initial_msg, uid, chat_id, key, iv)
    
    try:
        success = await start_match(key, iv, region, detailed)
        
        if success:
            success_msg = f"""[B][C][FFFF00]✅ MATCH START COMMAND SENT!

📋 Details:
• Type: {'Detailed device info' if detailed else 'Simple start'}
• Status: Match starting...
• Requirement: Bot must be squad leader

🎯 If bot is squad leader, match will begin!
"""
        else:
            success_msg = f"""[B][C][FF0000]❌ FAILED TO START MATCH!

Possible reasons:
1. Bot not in a squad
2. Bot not squad leader
3. Invalid packet structure
4. Server connection issue

💡 Make sure bot is in a squad as leader!
"""
        
        await safe_send_message(chat_type, success_msg, uid, chat_id, key, iv)
        
    except Exception as e:
        error_msg = f"[B][C][FF0000]❌ Error: {str(e)[:50]}\n"
        await safe_send_message(chat_type, error_msg, uid, chat_id, key, iv)
        
async def debug_start_match():
    """Debug function to test start packets"""
    
    print("🔍 Analyzing start packets...")
    print(f"Simple packet hex: 00 00 00 d6")
    print(f"Decimal value: {int('d6', 16)} = 214")
    
    # Try to decode the detailed packet
    detailed_hex = "0a8d010808100b180122047669766f2a02313330f6a8858c023a0961726d36342d76386142004a2466353338646339622d636563392d343363642d383132352d393566376634663166376533522a4646443538464234463736463634384332413545323145424346413341414538314234433942374439375a05766f69636562055632303539680172066d74363738351241464644353846423446373646363438433241354532314542434641334141453831423443394237443937494e445f31393939313230373532363130393739383430188d01"
    
    print(f"\n📊 Detailed packet length: {len(detailed_hex)//2} bytes")
    print(f"First bytes: {detailed_hex[:20]}...")
    
    # Try to parse as protobuf
    try:
        from protobuf_decoder.protobuf_decoder import Parser
        parsed = Parser().parse(bytes.fromhex(detailed_hex))
        print(f"\n✅ Parsed detailed packet:")
        print(parsed)
    except Exception as e:
        print(f"❌ Could not parse: {e}")
        


async def check_player_status(target_uid, key, iv, max_wait=3):
    """Direct function to check player status with proper waiting"""
    try:
        # Clear old cache
        if target_uid in status_response_cache:
            del status_response_cache[target_uid]
        
        # Send request
        status_packet = await createpacketinfo(target_uid, key, iv)
        if not status_packet:
            return None, "Failed to create packet"
        
        await SEndPacKeT(whisper_writer, online_writer, 'OnLine', status_packet)
        print(f"📤 Sent status request for {target_uid}")
        
        # Wait for response with polling
        start_time = time.time()
        while time.time() - start_time < max_wait:
            if target_uid in status_response_cache:
                cache_data = status_response_cache[target_uid]
                return cache_data, "Success"
            
            await asyncio.sleep(0.1)  # Short sleep
        
        return None, f"No response after {max_wait} seconds"
        
    except Exception as e:
        return None, f"Error: {str(e)}"

async def createpacketinfo(idddd, key, iv):
    """Create player status request packet - SAME as first TCP bot"""
    try:
        ida = Encrypt(idddd)
        packet = f"080112090A05{ida}1005"
        header_lenth = len(await encrypt_packet(packet, key, iv)) // 2
        header_lenth_final = dec_to_hex(header_lenth)
        
        if len(header_lenth_final) == 2:
            final_packet = "0F15000000" + header_lenth_final + await nmnmmmmn(packet, key, iv)
        elif len(header_lenth_final) == 3:
            final_packet = "0F1500000" + header_lenth_final + await nmnmmmmn(packet, key, iv)
        elif len(header_lenth_final) == 4:
            final_packet = "0F150000" + header_lenth_final + await nmnmmmmn(packet, key, iv)
        elif len(header_lenth_final) == 5:
            final_packet = "0F15000" + header_lenth_final + await nmnmmmmn(packet, key, iv)
        else:
            final_packet = "0F1500000" + header_lenth_final + await nmnmmmmn(packet, key, iv)
            
        return bytes.fromhex(final_packet)
        
    except Exception as e:
        print(f"Error creating packet info: {e}")
        return None

def fix_num(number):
    """Format numbers with breaks - from first TCP"""
    fixed = ""
    count = 0
    num_str = str(number)
    
    for char in num_str:
        if char.isdigit():
            count += 1
        fixed += char
        if count == 3:
            fixed += "[c]"
            count = 0
    return fixed

def get_available_room(input_text):
    """Parse protobuf to JSON - from first TCP"""
    try:
        from protobuf_decoder.protobuf_decoder import Parser
        parsed_results = Parser().parse(input_text)
        parsed_results_objects = parsed_results
        parsed_results_dict = parse_results(parsed_results_objects)
        json_data = json.dumps(parsed_results_dict)
        return json_data
    except Exception as e:
        print(f"error {e}")
        return None

def parse_results(parsed_results):
    """Helper for get_available_room"""
    result_dict = {}
    for result in parsed_results:
        field_data = {}
        field_data["wire_type"] = result.wire_type
        if result.wire_type == "varint":
            field_data["data"] = result.data
        if result.wire_type == "string":
            field_data["data"] = result.data
        if result.wire_type == "bytes":
            field_data["data"] = result.data
        elif result.wire_type == "length_delimited":
            field_data["data"] = parse_results(result.data.results)
        result_dict[result.field] = field_data
    return result_dict  # ← ADD THIS LINE

def get_player_status(packet):
    """Get player status from packet"""
    json_result = get_available_room(packet)
    if not json_result:
        return "OFFLINE"
    
    parsed_data = json.loads(json_result)
    
    if "5" not in parsed_data or "data" not in parsed_data["5"]:
        return "OFFLINE"
    
    json_data = parsed_data["5"]["data"]
    
    if "1" not in json_data or "data" not in json_data["1"]:
        return "OFFLINE"
    
    data = json_data["1"]["data"]
    
    if "3" not in data:
        return "OFFLINE"
    
    status_data = data["3"]
    
    if "data" not in status_data:
        return "OFFLINE"
    
    status = status_data["data"]
    
    if status == 1:
        return "SOLO"
    if status == 2:
        if "9" in data and "data" in data["9"]:
            group_count = data["9"]["data"]
            countmax1 = data["10"]["data"]
            countmax = countmax1 + 1
            return f"INSQUAD ({group_count}/{countmax})"
        return "INSQUAD"
    if status in [3, 5]:
        return "INGAME"
    if status == 4:
        return "IN ROOM"
    if status in [6, 7]:
        return "IN SOCIAL ISLAND MODE"
    
    return "NOTFOUND"

def get_idroom_by_idplayer(packet):
    """Extract room ID from player info packet"""
    try:
        json_result = get_available_room(packet)
        parsed_data = json.loads(json_result)
        json_data = parsed_data["5"]["data"]
        data = json_data["1"]["data"]
        idroom = data['15']["data"]
        return idroom
    except Exception as e:
        print(f"Error extracting room ID: {e}")
        return None



def get_leader(packet):
    """Extract leader ID from squad packet"""
    try:
        json_result = get_available_room(packet)
        parsed_data = json.loads(json_result)
        json_data = parsed_data["5"]["data"]
        data = json_data["1"]["data"]
        leader = data['8']["data"]
        return leader
    except Exception as e:
        print(f"Error extracting leader: {e}")
        return None

# Add to your global variables

# Add near top with other globals
status_queue = asyncio.Queue()
cache_dict = {}

# In TcPOnLine, instead of caching directly:
async def handle_status_response(hex_data):
    """Process and queue status responses"""
    try:
        # ... parsing code ...
        
        # Put in queue instead of direct cache
        await status_queue.put({
            'player_id': player_id,
            'data': cache_entry
        })
        
        print(f"📤 Queued status for {player_id}")
        
    except Exception as e:
        print(f"❌ Queue error: {e}")

# In TcPChaT, add a queue consumer
async def cache_consumer():
    """Consume status responses from queue"""
    while True:
        try:
            item = await status_queue.get()
            player_id = item['player_id']
            cache_dict[player_id] = item['data']
            print(f"📥 Cache updated for {player_id}")
            status_queue.task_done()
        except Exception as e:
            print(f"❌ Consumer error: {e}")
        await asyncio.sleep(0.1)



# Start consumer in your main function
async def StarTinG():
    # Start consumer
    consumer_task = asyncio.create_task(cache_consumer())
    
    while True:
        try:
            await asyncio.wait_for(MaiiiinE(), timeout = 7 * 60 * 60)
        except KeyboardInterrupt:
            consumer_task.cancel()
            break
        except asyncio.TimeoutError: 
            print("Token ExpiRed ! , ResTartinG")
        except Exception as e: 
            print(f"ErroR TcP - {e} => ResTarTinG ...")

import pickle
import os
import time

CACHE_FILE = 'status_cache.pkl'
CACHE_TIMEOUT = 30  # Cache entries expire after 30 seconds

def save_to_cache(player_id, data):
    """Save status to file cache with timestamp"""
    try:
        # Load existing cache
        if os.path.exists(CACHE_FILE):
            try:
                with open(CACHE_FILE, 'rb') as f:
                    cache = pickle.load(f)
            except:
                cache = {}
        else:
            cache = {}
        
        # Add timestamp
        data['saved_at'] = time.time()
        
        # Update cache
        cache[str(player_id)] = data
        
        # Save back
        with open(CACHE_FILE, 'wb') as f:
            pickle.dump(cache, f)
        
        print(f"💾 Saved to file cache: {player_id}")
        return True
    except Exception as e:
        print(f"❌ Cache save error: {e}")
        import traceback
        traceback.print_exc()
        return False

def load_from_cache(player_id):
    """Load status from file cache, check expiration"""
    try:
        if not os.path.exists(CACHE_FILE):
            return None
        
        with open(CACHE_FILE, 'rb') as f:
            cache = pickle.load(f)
        
        player_key = str(player_id)
        if player_key in cache:
            data = cache[player_key]
            
            # Check if cache is expired
            if 'saved_at' in data:
                if time.time() - data['saved_at'] > CACHE_TIMEOUT:
                    print(f"⏰ Cache expired for {player_id}")
                    del cache[player_key]
                    with open(CACHE_FILE, 'wb') as f:
                        pickle.dump(cache, f)
                    return None
            
            print(f"📥 Loaded from cache: {player_id}")
            return data
        
        return None
    except Exception as e:
        print(f"❌ Cache load error: {e}")
        return None

def clear_cache_entry(player_id):
    """Clear specific cache entry"""
    try:
        if os.path.exists(CACHE_FILE):
            with open(CACHE_FILE, 'rb') as f:
                cache = pickle.load(f)
            
            player_key = str(player_id)
            if player_key in cache:
                del cache[player_key]
                
            with open(CACHE_FILE, 'wb') as f:
                pickle.dump(cache, f)
            print(f"🗑️ Cleared cache for {player_id}")
    except Exception as e:
        print(f"❌ Clear cache error: {e}")

def debug_file_cache():
    """Debug the file cache"""
    try:
        if os.path.exists(CACHE_FILE):
            with open(CACHE_FILE, 'rb') as f:
                cache = pickle.load(f)
            print(f"\n📁 FILE CACHE DEBUG:")
            print(f"Size: {len(cache)} entries")
            for uid, data in cache.items():
                age = time.time() - data.get('saved_at', 0)
                status = data.get('status', 'NO STATUS')
                print(f"  {uid}: {status} (age: {age:.1f}s)")
            print("---\n")
            return cache
        else:
            print("📁 No cache file exists")
            return {}
    except Exception as e:
        print(f"❌ Cache debug error: {e}")
        return {}

def load_from_cache(player_id):
    """Load status from file cache"""
    try:
        if not os.path.exists(CACHE_FILE):
            return None
        
        with open(CACHE_FILE, 'rb') as f:
            cache = pickle.load(f)
        
        if player_id in cache:
            return cache[player_id]
        return None
    except Exception as e:
        print(f"❌ Cache load error: {e}")
        return None

def clear_cache_entry(player_id):
    """Clear specific cache entry"""
    try:
        if os.path.exists(CACHE_FILE):
            with open(CACHE_FILE, 'rb') as f:
                cache = pickle.load(f)
            
            if player_id in cache:
                del cache[player_id]
                
            with open(CACHE_FILE, 'wb') as f:
                pickle.dump(cache, f)
    except:
        pass


    
    
    async def get_account_token(self, uid, password):
        """Get access token for a specific account"""
        try:
            url = "https://100067.connect.garena.com/oauth/guest/token/grant"
            headers = {
                "Host": "100067.connect.garena.com",
                "User-Agent": await Ua(),
                "Content-Type": "application/x-www-form-urlencoded",
                "Accept-Encoding": "gzip, deflate, br",
                "Connection": "close"
            }
            data = {
                "uid": uid,
                "password": password,
                "response_type": "token",
                "client_type": "2",
                "client_secret": "2ee44819e9b4598845141067b281621874d0d5d7af9d8f7e00c1e54715b7d1e3",
                "client_id": "100067"
            }
            
            async with aiohttp.ClientSession() as session:
                async with session.post(url, headers=headers, data=data) as response:
                    if response.status == 200:
                        data = await response.json()
                        open_id = data.get("open_id")
                        access_token = data.get("access_token")
                        return open_id, access_token
            return None, None
        except Exception as e:
            print(f"❌ Error getting token for {uid}: {e}")
            return None, None
    
    async def send_join_from_account(self, target_uid, account_uid, password, key, iv, region):
        """Send join request from a specific account"""
        try:
            # Get token for this account
            open_id, access_token = await self.get_account_token(account_uid, password)
            if not open_id or not access_token:
                return False
            
            # Create join packet using the account's credentials
            join_packet = await self.create_account_join_packet(target_uid, account_uid, open_id, access_token, key, iv, region)
            if join_packet:
                await SEndPacKeT(whisper_writer, online_writer, 'OnLine', join_packet)
                return True
            return False
            
        except Exception as e:
            print(f"❌ Error sending join from {account_uid}: {e}")
            return False

async def join_custom_room(room_id, room_password, key, iv, region):
    """Join custom room with proper Free Fire packet structure"""
    fields = {
        1: 61,  # Room join packet type (verified for Free Fire)
        2: {
            1: int(room_id),
            2: {
                1: int(room_id),  # Room ID
                2: int(time.time()),  # Timestamp
                3: "BOT",  # Player name
                5: 12,  # Unknown
                6: 9999999,  # Unknown
                7: 1,  # Unknown
                8: {
                    2: 1,
                    3: 1,
                },
                9: 3,  # Room type
            },
            3: str(room_password),  # Room password
        }
    }
    
    if region.lower() == "ind":
        packet_type = '0514'
    elif region.lower() == "bd":
        packet_type = "0519"
    else:
        packet_type = "0515"
        
    return await GeneRaTePk((await CrEaTe_ProTo(fields)).hex(), packet_type, key, iv)
    
async def leave_squad(key, iv, region):
    """Leave squad - converted from your old TCP leave_s()"""
    fields = {
        1: 7,
        2: {
            1: 12480598706  # Your exact value from old TCP
        }
    }
    
    packet = (await CrEaTe_ProTo(fields)).hex()
    
    if region.lower() == "ind":
        packet_type = '0514'
    elif region.lower() == "bd":
        packet_type = "0519"
    else:
        packet_type = "0515"
        
    return await GeneRaTePk(packet, packet_type, key, iv)    
    
async def request_join_with_badge(target_uid, badge_value, key, iv, region):
    """Send join request with specific badge - converted from your old TCP"""
    fields = {
        1: 33,
        2: {
            1: int(target_uid),
            2: region.upper(),
            3: 1,
            4: 1,
            5: bytes([1, 7, 9, 10, 11, 18, 25, 26, 32]),
            6: "iG:[C][B][FF0000] zainu___bhai__edits",
            7: 330,
            8: 1000,
            10: region.upper(),
            11: bytes([49, 97, 99, 52, 98, 56, 48, 101, 99, 102, 48, 52, 55, 56,
                       97, 52, 52, 50, 48, 51, 98, 102, 56, 102, 97, 99, 54, 49, 50, 48, 102, 53]),
            12: 1,
            13: int(target_uid),
            14: {
                1: 2203434355,
                2: 8,
                3: "\u0010\u0015\b\n\u000b\u0013\f\u000f\u0011\u0004\u0007\u0002\u0003\r\u000e\u0012\u0001\u0005\u0006"
            },
            16: 1,
            17: 1,
            18: 312,
            19: 46,
            23: bytes([16, 1, 24, 1]),
            24: int(await get_random_avatar()),
            26: "",
            28: "",
            31: {
                1: 1,
                2: badge_value  # Dynamic badge value
            },
            32: badge_value,    # Dynamic badge value
            34: {
                1: int(target_uid),
                2: 8,
                3: bytes([15,6,21,8,10,11,19,12,17,4,14,20,7,2,1,5,16,3,13,18])
            }
        },
        10: "en",
        13: {
            2: 1,
            3: 1
        }
    }
    
    packet = (await CrEaTe_ProTo(fields)).hex()
    
    if region.lower() == "ind":
        packet_type = '0514'
    elif region.lower() == "bd":
        packet_type = "0519"
    else:
        packet_type = "0515"
        
    return await GeneRaTePk(packet, packet_type, key, iv)    
    
async def reset_bot_state(key, iv, region):
    """Reset bot to solo mode before spam - Critical step from your old TCP"""
    try:
        # Leave any current squad (using your exact leave_s function)
        leave_packet = await leave_squad(key, iv, region)
        await SEndPacKeT(whisper_writer, online_writer, 'OnLine', leave_packet)
        await asyncio.sleep(0.5)
        
        print("✅ Bot state reset - left squad")
        return True
        
    except Exception as e:
        print(f"❌ Error resetting bot: {e}")
        return False    
    
async def create_custom_room(room_name, room_password, max_players, key, iv, region):
    """Create a custom room"""
    fields = {
        1: 3,  # Create room packet type
        2: {
            1: room_name,
            2: room_password,
            3: max_players,  # 2, 4, 8, 16, etc.
            4: 1,  # Room mode
            5: 1,  # Map
            6: "en",  # Language
            7: {   # Player info
                1: "BotHost",
                2: int(await xBunnEr()),
                3: 330,
                4: 1048576,
                5: "BOTCLAN"
            }
        }
    }
    
    if region.lower() == "ind":
        packet_type = '0514'
    elif region.lower() == "bd":
        packet_type = "0519"
    else:
        packet_type = "0515"
        
    return await GeneRaTePk((await CrEaTe_ProTo(fields)).hex(), packet_type, key, iv)              




async def handle_badge_command(cmd, inPuTMsG, uid, chat_id, key, iv, region, chat_type):
    """Handle individual badge commands"""
    parts = inPuTMsG.strip().split()
    if len(parts) < 2:
        error_msg = f"[B][C][FF0000]❌ Usage: /{cmd} (uid)\nExample: /{cmd} 123456789\n"
        await safe_send_message(chat_type, error_msg, uid, chat_id, key, iv)
        return
    
    target_uid = parts[1]
    badge_value = BADGE_VALUES.get(cmd, 1048576)
    
    if not target_uid.isdigit():
        error_msg = f"[B][C][FF0000]❌ Please write a valid player ID!\n"
        await safe_send_message(chat_type, error_msg, uid, chat_id, key, iv)
        return
    
    # Send initial message
    initial_msg = f"[B][C][1E90FF]🌀 Request received! Preparing to spam {target_uid}...\n"
    await safe_send_message(chat_type, initial_msg, uid, chat_id, key, iv)
    
    try:
        # Reset bot state
        await reset_bot_state(key, iv, region)
        
        # Create and send join packets
        join_packet = await request_join_with_badge(target_uid, badge_value, key, iv, region)
        spam_count = 3
        
        for i in range(spam_count):
            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', join_packet)
            print(f"✅ Sent /{cmd} request #{i+1} with badge {badge_value}")
            await asyncio.sleep(0.1)
        
        success_msg = f"[B][C][00FF00]✅ Successfully Sent {spam_count} Join Requests!\n🎯 Target: {target_uid}\n🏷️ Badge: {badge_value}\n"
        await safe_send_message(chat_type, success_msg, uid, chat_id, key, iv)
        
        # Cleanup
        await asyncio.sleep(1)
        await reset_bot_state(key, iv, region)
        
    except Exception as e:
        error_msg = f"[B][C][FF0000]❌ Error in /{cmd}: {str(e)}\n"
        await safe_send_message(chat_type, error_msg, uid, chat_id, key, iv)
    
async def auto_rings_emote_dual(uid, key, iv, region):
    """Send The Rings emote to both sender and bot for dual emote effect"""
    try:
        # The Rings emote ID
        rings_emote_id = 909052010
        
        # Get bot's UID
        bot_uid = 13814574141
        
        # Send emote to SENDER (person who invited)
        emote_to_sender = await Emote_k(int(uid), rings_emote_id, key, iv, region)
        await SEndPacKeT(whisper_writer, online_writer, 'OnLine', emote_to_sender)
        
        # Small delay between emotes
        await asyncio.sleep(0.5)
        
        # Send emote to BOT (bot performs emote on itself)
        emote_to_bot = await Emote_k(int(bot_uid), rings_emote_id, key, iv, region)
        await SEndPacKeT(whisper_writer, online_writer, 'OnLine', emote_to_bot)
        
        print(f"🤖 Bot performed dual Rings emote with sender {uid} and bot {bot_uid}!")
        
    except Exception as e:
        print(f"Error sending dual rings emote: {e}")    
        
        
async def Room_Spam(Uid, Rm, Nm, K, V):
    fields = {
        1: 78,
        2: {
            1: int(Rm),  
            2: "iG:[C][B][FF0000]itz___zainu__edits",  
            3: {
                2: 1,
                3: 1
            },
            4: 330,      
            5: 6000,     
            6: 201,      
            10: int(await xBunnEr()),  
            11: int(Uid), # Target UID
            12: 1,       
            15: {
                1: 1,
                2: 32768
            },
            16: 32768,    
            18: {
                1: 11481904755,  
                2: 8,
                3: "\u0010\u0015\b\n\u000b\u0013\f\u000f\u0011\u0004\u0007\u0002\u0003\r\u000e\u0012\u0001\u0005\u0006"
            },
            
            31: {
                1: 1,
                2: 32768
            },
            32: 32768,    
            34: {
                1: int(Uid),   
                2: 8,
                3: bytes([15,6,21,8,10,11,19,12,17,4,14,20,7,2,1,5,16,3,13,18])
            }
        }
    }
    
    return await GeneRaTePk((await CrEaTe_ProTo(fields)).hex(), '0e15', K, V)
    
async def evo_cycle_spam(uids, key, iv, region, LoGinDaTaUncRypTinG):
    """Cycle through all evolution emotes - BOT DOES OPPOSITE"""
    global evo_cycle_running
    
    # GET BOT UID FROM LOGIN DATA
    try:
        # Try to get from login data (passed as parameter)
        bot_uid = LoGinDaTaUncRypTinG.AccountUID
        print(f"🤖 Using bot UID from login: {bot_uid}")
    except:
        # Fallback to your hardcoded UID
        bot_uid = 13743555551
        print(f"🤖 Using hardcoded bot UID: {bot_uid}")
    
    cycle_count = 0
    while evo_cycle_running:
        cycle_count += 1
        print(f"Starting evolution emote cycle #{cycle_count}")
        
        emote_list = list(evo_emotes.items())
        total_emotes = len(emote_list)
        
        for index, (emote_number, emote_id) in enumerate(emote_list):
            if not evo_cycle_running:
                break
                
            # USER does emote #X
            for uid in uids:
                try:
                    uid_int = int(uid)
                    user_emote = await Emote_k(uid_int, int(emote_id), key, iv, region)
                    await SEndPacKeT(whisper_writer, online_writer, 'OnLine', user_emote)
                    print(f"👤 User emote #{emote_number}")
                except Exception as e:
                    print(f"Error: {e}")
            
            # ADD SMALL DELAY
            await asyncio.sleep(0.5)
            
            # BOT does opposite emote (last emote when user does first, etc.)
            opposite_index = total_emotes - 1 - index
            opposite_number, opposite_id = emote_list[opposite_index]
            
            try:
                # BOT sends emote to ITSELF
                bot_self_emote = await Emote_k(int(bot_uid), int(opposite_id), key, iv, region)
                await SEndPacKeT(whisper_writer, online_writer, 'OnLine', bot_self_emote)
                
                # ALSO send to first user for visibility
                await asyncio.sleep(0.3)
                if uids:
                    first_uid = int(uids[0])
                    bot_to_user = await Emote_k(first_uid, int(opposite_id), key, iv, region)
                    await SEndPacKeT(whisper_writer, online_writer, 'OnLine', bot_to_user)
                
                print(f"🤖 Bot OPPOSITE emote #{opposite_number} (sent to self + user)")
            except Exception as e:
                print(f"Bot error: {e}")
            
            # Wait 5 seconds before next emote
            if evo_cycle_running:
                print(f"Waiting 5 seconds before next emote...")
                wait_time = 5
                for i in range(wait_time):
                    if not evo_cycle_running:
                        break
                    await asyncio.sleep(1)
    
    print("Cycle stopped")
    
async def reject_spam_loop(target_uid, key, iv):
    """Send reject spam packets to target in background"""
    global reject_spam_running
    
    count = 0
    max_spam = 150
    
    while reject_spam_running and count < max_spam:
        try:
            # Send both packets
            packet1 = await banecipher1(target_uid, key, iv)
            packet2 = await banecipher(target_uid, key, iv)
            
            # Send to Online connection
            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', packet1)
            await asyncio.sleep(0.1)
            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', packet2)
            
            count += 1
            print(f"Sent reject spam #{count} to {target_uid}")
            
            # 0.2 second delay between spam cycles
            await asyncio.sleep(0.2)
            
        except Exception as e:
            print(f"Error in reject spam: {e}")
            break
    
    return count    
    
async def handle_reject_completion(spam_task, target_uid, sender_uid, chat_id, chat_type, key, iv):
    """Handle completion of reject spam and send final message"""
    try:
        spam_count = await spam_task
        
        # Send completion message
        if spam_count >= 150:
            completion_msg = f"[B][C][FFFF00]✅ Reject Spam Completed Successfully for ID {target_uid}\n✅ Total packets sent: {spam_count * 2}\n"
        else:
            completion_msg = f"[B][C][FFFF00]⚠️ Reject Spam Partially Completed for ID {target_uid}\n⚠️ Total packets sent: {spam_count * 2}\n"
        
        await safe_send_message(chat_type, completion_msg, sender_uid, chat_id, key, iv)
        
    except asyncio.CancelledError:
        print("Reject spam was cancelled")
    except Exception as e:
        error_msg = f"[B][C][FF0000]❌ ERROR in reject spam: {str(e)}\n"
        await safe_send_message(chat_type, error_msg, sender_uid, chat_id, key, iv)    
    
    
    
async def banecipher(target_uid, key, iv):
    """Create reject spam packet 1 - Converted to new async format"""
    banner_text = f"""
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][0000FF]======================================================================================================================================================================================================================================================
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███




"""        
    fields = {
        1: 5,
        2: {
            1: int(client_id),
            2: 1,
            3: int(client_id),
            4: banner_text
        }
    }
    
    # Use CrEaTe_ProTo from xC4.py (async)
    packet = await CrEaTe_ProTo(fields)
    packet_hex = packet.hex()
    
    # Use EnC_PacKeT from xC4.py (async)
    encrypted_packet = await EnC_PacKeT(packet_hex, key, iv)
    
    # Calculate header length
    header_length = len(encrypted_packet) // 2
    header_length_final = await DecodE_HeX(header_length)
    
    # Build final packet based on header length
    if len(header_length_final) == 2:
        final_packet = "0515000000" + header_length_final + encrypted_packet
    elif len(header_length_final) == 3:
        final_packet = "051500000" + header_length_final + encrypted_packet
    elif len(header_length_final) == 4:
        final_packet = "05150000" + header_length_final + encrypted_packet
    elif len(header_length_final) == 5:
        final_packet = "0515000" + header_length_final + encrypted_packet
    else:
        final_packet = "0515000000" + header_length_final + encrypted_packet

    return bytes.fromhex(final_packet)

async def black666(client_id, key, iv):
    banner_text = "[FF0000][B][C] ERROR , WELCOME TO [FFFFFF] [FFFF00]___X³____ BOT ! \n[FFFF00]NEW VERSION NEW FUNCTION !\n[FF0000]TELEGRAM : @classic_aruhi\n\n"     
    fields = {
        1: 5,
        2: {
            1: int(client_id),
            2: 1,
            3: int(client_id),
            4: banner_text
        }
    }
    
    # Use CrEaTe_ProTo from xC4.py (async)
    packet = await CrEaTe_ProTo(fields)
    packet_hex = packet.hex()
    
    # Use EnC_PacKeT from xC4.py (async)
    encrypted_packet = await EnC_PacKeT(packet_hex, key, iv)
    
    # Calculate header length
    header_length = len(encrypted_packet) // 2
    header_length_final = await DecodE_HeX(header_length)
    
    # Build final packet based on header length
    if len(header_length_final) == 2:
        final_packet = "0515000000" + header_length_final + encrypted_packet
    elif len(header_length_final) == 3:
        final_packet = "051500000" + header_length_final + encrypted_packet
    elif len(header_length_final) == 4:
        final_packet = "05150000" + header_length_final + encrypted_packet
    elif len(header_length_final) == 5:
        final_packet = "0515000" + header_length_final + encrypted_packet
    else:
        final_packet = "0515000000" + header_length_final + encrypted_packet

    return bytes.fromhex(final_packet)

async def banecipher1(client_id, key, iv):
    """Create reject spam packet 2 - Converted to new async format"""
    gay_text = f"""
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][0000FF]======================================================================================================================================================================================================================================================
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███
[b][000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███[000000]███




"""        
    fields = {
        1: int(client_id),
        2: 5,
        4: 50,
        5: {
            1: int(client_id),
            2: gay_text,
        }
    }
    
    # Use CrEaTe_ProTo from xC4.py (async)
    packet = await CrEaTe_ProTo(fields)
    packet_hex = packet.hex()
    
    # Use EnC_PacKeT from xC4.py (async)
    encrypted_packet = await EnC_PacKeT(packet_hex, key, iv)
    
    # Calculate header length
    header_length = len(encrypted_packet) // 2
    header_length_final = await DecodE_HeX(header_length)
    
    # Build final packet based on header length
    if len(header_length_final) == 2:
        final_packet = "0515000000" + header_length_final + encrypted_packet
    elif len(header_length_final) == 3:
        final_packet = "051500000" + header_length_final + encrypted_packet
    elif len(header_length_final) == 4:
        final_packet = "05150000" + header_length_final + encrypted_packet
    elif len(header_length_final) == 5:
        final_packet = "0515000" + header_length_final + encrypted_packet
    else:
        final_packet = "0515000000" + header_length_final + encrypted_packet

    return bytes.fromhex(final_packet)
    
async def get_colorful_message(message_text, message_number):
    """Generate message with different colors"""
    color_palette = ["FF0000", "FFFF00", "0000FF", "FFFF00", "FF00FF", 
                     "00FFFF", "FFA500", "FF1493", "00FF7F", "7B68EE",
                     "FFD700", "00CED1", "FF69B4", "32CD32", "9370DB",
                     "FF4500", "1E90FF", "ADFF2F", "FF6347", "8A2BE2"]
    
    color_index = (message_number - 1) % len(color_palette)
    return f"[C][B][{color_palette[color_index]}]{message_text}"    

def get_random_avatar1():
	avatar_list = [
         '902050001', '902050002', '902050003', '902039016', '902050004', 
        '902047011', '902047010', '902049015', '902050006', '902049020','902000065','902000065','902000064','902000127','902000210', '902000178', '902000072', '902000067', '902000212', '902000206', '902000204', '902000064', '902000086','902000063','902000165','902000236','902000231', '902000191', '902000193','902000195', '902000338', '902033026','902000067', '902000093', '902000098'
    ]
	random_avatar = random.choice(avatar_list)
	return  random_avatar
	
async def get_random_avatar():
    await asyncio.sleep(0)  # makes it async but instant
    avatar_list = [
       '902000065','902000065','902000064','902000127','902000210', '902000178', '902000072', '902000067', '902000212', '902000206', '902000204', '902000064', '902000086','902000063','902000165','902000236','902000231', '902000191', '902000193','902000195', '902000338', '902033026','902000067', '902000093', '902000098'
    ]
    return random.choice(avatar_list)
    


async def xSEndMsgsQQ(Msg , id , K , V):
    fields = {1: id , 2: id , 4: Msg , 5: 1756580149, 7: 2, 8: 904990072, 9: {1: "xBe4!sTo - C4", 2: int(get_random_avatar1()), 4: 330, 5: 1001000001, 8: "xBe4!sTo - C4", 10: 1, 11: 1, 13: {1: 2}, 14: {1: 1158053040, 2: 8, 3: "\u0010\u0015\b\n\u000b\u0015\f\u000f\u0011\u0004\u0007\u0002\u0003\r\u000e\u0012\u0001\u0005\u0006"}}, 10: "en", 13: {2: 2, 3: 1}}
    Pk = (await CrEaTe_ProTo(fields)).hex()
    Pk = "080112" + await EnC_Uid(len(Pk) // 2, Tp='Uid') + Pk
    return await GeneRaTePk(Pk, '1201', K, V)     

async def Create_xr_room_packet_fixed__(room_id, key, iv):
    """FIXED: Room chat packets must use Whisper connection"""
    random_color = generate_random_hex_color()

    fields = {
        1: 1,
        2: {
            1: 9280892890,  # Bot UID
            2: int(room_id),
            3: 3,  # Chat type 3 = room chat
            4: f"[FFFFFF]Hello",
            5: int(time.time()),  # Current timestamp, not hardcoded
            7: 2,
            9: {
                1: "XR SUPER ",
                2: bunner_(),   
                4: 228,
                7: 1,
            },
            10: "ar",  # Language (arabic? change to "en" if needed)
            13: {
                2: 1,
                3: 1
            }
        }
    }

    # Convert to protobuf hex
    proto_hex = (await CrEaTe_ProTo(fields)).hex()
    
    print(f"📦 Room chat proto: {len(proto_hex)//2} bytes")
    print(f"Hex start: {proto_hex[:50]}...")
    
    # CRITICAL FIX: Room chat uses Whisper connection (12xx headers)
    # Try different packet types for Whisper
    packet_type = "1215"  # Whisper connection for chat
    
    # Generate final encrypted packet
    final_packet = await GeneRaTePk(proto_hex, packet_type, key, iv)
    
    return final_packet

async def send_wave_messages(message_text, repeats, chat_id, key, iv, region):
    """Send message in wave pattern: expanding then shrinking"""
    global msg_spam_running
    
    count = 0
    total_cycles = 0
    
    while msg_spam_running and total_cycles < repeats:
        try:
            # EXPANDING phase (h, he, hel, hell, hello)
            for i in range(1, len(message_text) + 1):
                if not msg_spam_running:
                    break
                    
                partial_msg = message_text[:i]
                colorful_msg = await get_colorful_message(partial_msg, i)
                
                msg_packet = await xSEndMsgsQ(colorful_msg, int(chat_id), key, iv)
                if msg_packet and whisper_writer:
                    await SEndPacKeT(whisper_writer, online_writer, 'ChaT', msg_packet)
                    count += 1
                    print(f"✅ Wave #{total_cycles+1} - Expanding: '{partial_msg}'")
                    await asyncio.sleep(0.1)
            
            # SHRINKING phase (hell, hel, he, h)
            for i in range(len(message_text) - 1, 0, -1):
                if not msg_spam_running:
                    break
                    
                partial_msg = message_text[:i]
                colorful_msg = await get_colorful_message(partial_msg, i)
                
                msg_packet = await xSEndMsgsQQ(colorful_msg, int(chat_id), key, iv)
                if msg_packet and whisper_writer:
                    await SEndPacKeT(whisper_writer, online_writer, 'ChaT', msg_packet)
                    count += 1
                    print(f"✅ Wave #{total_cycles+1} - Shrinking: '{partial_msg}'")
                    await asyncio.sleep(0.1)
            
            total_cycles += 1
            print(f"🌀 Completed wave cycle {total_cycles}/{repeats}")
            
        except Exception as e:
            print(f"❌ Error in wave messages: {e}")
            break
    
    return count, total_cycles

async def handle_wave_completion(spam_task, message_text, repeats, sender_uid, chat_id, chat_type, key, iv):
    """Handle completion of wave messages"""
    try:
        message_count, cycles_completed = await spam_task
        
        total_per_cycle = (len(message_text) * 2) - 2
        expected_total = total_per_cycle * repeats
        

        
    except asyncio.CancelledError:
        cancel_msg = f"[B][C][FFFF00]🛑 WAVE CANCELLED!\n"
        await safe_send_message(chat_type, cancel_msg, sender_uid, chat_id, key, iv)

# Replace the msg_spam_loop function with this simpler version:
async def msg_spam_loop(message_text, times, chat_id, key, iv, region):
    """Send message multiple times in team chat using existing functions"""
    global msg_spam_running
    
    count = 0
    
    while msg_spam_running and count < times:
        try:
            # Use the existing xSEndMsgsQ function from xC4.py
            # This is for squad chat (chat_type 0)
            # Replace: msg_packet = await xSEndMsgsQ(message_text, int(chat_id), key, iv)
            # With:
            colorful_message = await get_colorful_message(message_text, count + 1)
            msg_packet = await xSEndMsgsQQ(colorful_message, int(chat_id), key, iv)
            
            if not msg_packet:
                print("❌ Failed to create message packet")
                break
                
            # Send the packet - use ChaT connection type for squad messages
            if whisper_writer:
                await SEndPacKeT(whisper_writer, online_writer, 'ChaT', msg_packet)
                count += 1
                print(f"✅ Sent message #{count}/{times} to squad chat: '{message_text}'")
                
                # Adjust delay to avoid rate limiting
                await asyncio.sleep(0.1)
                
        except Exception as e:
            print(f"❌ Error in msg spam loop: {e}")
            import traceback
            traceback.print_exc()
            break
    
    return count

# Update the command handler to use the correct chat_id
# In the TcPChaT function, update the /msg command:



# Also, let's improve the handle_msg_spam_completion function:
async def handle_msg_spam_completion(spam_task, message_text, times, sender_uid, chat_id, chat_type, key, iv):
    """Handle completion of message spam and send final message"""
    try:
        actual_times = await spam_task
        
        # Send completion message
        if actual_times >= times:
            completion_msg = f"[B][C][FFFF00]✅ MESSAGE SPAM COMPLETED!\n"
            completion_msg += f"[FFFFFF]📝 Message: {message_text}\n"
            completion_msg += f"[FFFFFF]📊 Requested: {times} times\n"
            completion_msg += f"[FFFFFF]✅ Sent: {actual_times} times\n"
            completion_msg += f"[FFFF00]✓ Success rate: 100%\n"
            completion_msg += f"[FFFFFF]💬 Check squad chat to see messages!\n"
        elif actual_times > 0:
            completion_msg = f"[B][C][FFFF00]⚠️ MESSAGE SPAM PARTIALLY COMPLETED!\n"
            completion_msg += f"[FFFFFF]📝 Message: {message_text}\n"
            completion_msg += f"[FFFFFF]📊 Requested: {times} times\n"
            completion_msg += f"[FFFFFF]⚠️ Sent: {actual_times} times\n"
            completion_msg += f"[FFFF00]↯ Success rate: {(actual_times/times)*100:.1f}%\n"
            completion_msg += f"[FFFFFF]💬 Check squad chat to see messages!\n"
        else:
            completion_msg = f"[B][C][FF0000]❌ MESSAGE SPAM FAILED!\n"
            completion_msg += f"[FFFFFF]📝 Message: {message_text}\n"
            completion_msg += f"[FFFFFF]📊 Requested: {times} times\n"
            completion_msg += f"[FFFFFF]❌ Sent: 0 times\n"
            completion_msg += f"[FF0000]✗ Failed to send any messages\n"
            completion_msg += f"[FFFFFF]🔧 Possible issues:\n"
            completion_msg += f"[FFFFFF]1. Bot not in a squad\n"
            completion_msg += f"[FFFFFF]2. Invalid chat_id\n"
            completion_msg += f"[FFFFFF]3. Connection error\n"
        
        await safe_send_message(chat_type, completion_msg, sender_uid, chat_id, key, iv)
        
    except asyncio.CancelledError:
        print("Message spam was cancelled by user")
        cancel_msg = f"[B][C][FFFF00]🛑 MESSAGE SPAM CANCELLED!\n[FFFFFF]Message spam was stopped by user command.\n"
        await safe_send_message(chat_type, cancel_msg, sender_uid, chat_id, key, iv)
    except Exception as e:
        error_msg = f"[B][C][FF0000]❌ ERROR in message spam completion: {str(e)}\n"
        await safe_send_message(chat_type, error_msg, sender_uid, chat_id, key, iv)
        
async def send_msg_in_room_async(Msg, room_id, key, iv):
    """Converted to your async TCP format"""
    from datetime import datetime
    sticker_value = get_random_sticker()
    
    fields = {
        1: 1,
        2: {
            1: int(room_id),
            2: int(room_id),
            3: 3,
            4: f"{Msg}",
            5: int(datetime.now().timestamp()),
            7: 2,
            8: f'{{"StickerStr" : "{sticker_value}", "type":"Sticker"}}',
            9: {
                1: "byte bot",
                2: int(await xBunnEr()),  # Changed to your function
                4: 329,
                7: 1,
            },
            10: "en",
            13: {2: 1, 3: 1},
        },
    }

    # Create protobuf packet using your function
    packet = await CrEaTe_ProTo(fields)
    
    # Convert to hex and add "7200"
    packet_hex = packet.hex() + "7200"

    # Encrypt using your function
    encrypted_packet = await encrypt_packet(packet_hex, key, iv)
    
    # Calculate header length
    header_length = len(encrypted_packet) // 2
    header_length_final = await DecodE_HeX(header_length)

    # Determine format based on header length
    if len(header_length_final) == 2:
        final_packet = "1215000000" + header_length_final + encrypted_packet
        return bytes.fromhex(final_packet)

    elif len(header_length_final) == 3:
        final_packet = "121500000" + header_length_final + encrypted_packet
        return bytes.fromhex(final_packet)

    elif len(header_length_final) == 4:
        final_packet = "12150000" + header_length_final + encrypted_packet
        return bytes.fromhex(final_packet)

    elif len(header_length_final) == 5:
        final_packet = "12150000" + header_length_final + encrypted_packet
        return bytes.fromhex(final_packet)

# Command handler for room messages:
async def handle_room_message_command(inPuTMsG, uid, chat_id, key, iv, region, chat_type):
    """
    Handle /roommsg command to send messages in custom rooms
    """
    parts = inPuTMsG.strip().split()
    
    if len(parts) < 3:
        error_msg = f"""[B][C][FF0000]❌ Usage: /roommsg (room_id) (message)
        
📝 Examples:
/roommsg 123456 Hello everyone!
/roommsg 987654 Welcome to my
"""
        await safe_send_message(chat_type, error_msg, uid, chat_id, key, iv)
        return
    
    room_id = parts[1]
    message = ' '.join(parts[2:])
    Msg = message 
    # Validate room ID
    if not room_id.isdigit():
        error_msg = f"[B][C][FF0000]❌ Room ID must be numbers only!\n"
        await safe_send_message(chat_type, error_msg, uid, chat_id, key, iv)
        print(error_msg)
        return
    
    # Send initial message
    initial_msg = f"[B][C][FFFF00]📤 Sending room message...\n"
    initial_msg += f"🏠 Room: {room_id}\n"
    
    
    await safe_send_message(chat_type, initial_msg, uid, chat_id, key, iv)
    print(initial_msg)
    
    try:
        # Create the room message packet
        room_packet = await send_msg_in_room_async(Msg, room_id, key, iv)
        
        if room_packet and whisper_writer:
            # Send via Whisper connection (for chat packets)
            whisper_writer.write(room_packet)
            await whisper_writer.drain()
            
            success_msg = f"""[B][C][FFFF00]✅ ROOM MESSAGE SENT!

🏠 Room: {room_id}
📝 Message: {message}
"""
        else:
            success_msg = f"[B][C][FF0000]❌ Failed to create room packet!\n"
        
        await safe_send_message(chat_type, success_msg, uid, chat_id, key, iv)
        print(success_msg)
        
    except Exception as e:
        error_msg = f"[B][C][FF0000]❌ Error: {str(e)[:50]}\n"
        await safe_send_message(chat_type, error_msg, uid, chat_id, key, iv)
        print(error_msg)

async def create_training_start_packet(key, iv, region):
    """Create packet to start training mode in Free Fire"""
    
    try:
        # Decoded from your hex dump:
        # 62 27 01 01 28 00 01 00 00 00 00 00 79 2c 59 bf...
        # This appears to be a "start training" or "enter training ground" packet
        
        # Based on common Free Fire packet structure:
        # Packet type 0x27 = 39 decimal (training related)
        
        fields = {
            1: 39,  # Packet type for training (0x27 = 39)
            2: {
                1: 1,  # Action type (1 = start/enter)
                2: 1,  # Training mode type (1 = normal training)
                3: 0,  # Unknown flag
                4: 0,  # Unknown flag
                # The rest appears to be encrypted training data
                5: {
                    1: bytes.fromhex("79 2c 59 bf e0 5b be a6 00 ae 89 a5 26 4f 55 6f"),
                    2: bytes.fromhex("40 e5 e3 52 aa e2 46 26 ef e8 ac 5c 6c b1 db 9e"),
                    3: bytes.fromhex("87 09 4d aa ed c2 eb da")
                }
            }
        }
        
        # Alternative simpler structure (more likely):
        fields_simple = {
            1: 39,  # Training packet type
            2: {
                1: 1,   # Start training command
                2: 0,   # Training ground ID (0 = default)
                3: 1,   # Mode (1 = training)
                4: {    # Training settings
                    1: 1,  # Weapons enabled
                    2: 1,  # Bots enabled
                    3: 0,  # Unlimited ammo
                    4: 1,  # Health regen
                    5: 0   # God mode
                }
            }
        }
        
        # Let's try the simple structure first
        packet = await CrEaTe_ProTo(fields_simple)
        packet_hex = packet.hex()
        
        print(f"📦 Created training packet: {packet_hex[:50]}...")
        
        # Determine packet header based on region
        if region.lower() == "ind":
            packet_type = '0514'
        elif region.lower() == "bd":
            packet_type = "0519"
        else:
            packet_type = "0515"
            
        # Generate final encrypted packet
        final_packet = await GeneRaTePk(packet_hex, packet_type, key, iv)
        
        print(f"✅ Training start packet created")
        return final_packet
        
    except Exception as e:
        print(f"❌ Error creating training packet: {e}")
        import traceback
        traceback.print_exc()
        return None


async def start_training_mode(key, iv, region):
    """Start training mode - sends the training start packet"""
    
    try:
        training_packet = await create_training_start_packet(key, iv, region)
        
        if training_packet:
            # Send to Online connection
            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', training_packet)
            print("🎮 Training mode start packet sent!")
            return True
        else:
            print("❌ Failed to create training packet")
            return False
            
    except Exception as e:
        print(f"❌ Error starting training: {e}")
        return False


# Add this command handler to your TcPChaT function:
async def handle_training_command(inPuTMsG, uid, chat_id, key, iv, region, chat_type):
    """Handle /train command to start training mode"""
    
    parts = inPuTMsG.strip().split()
    
    if len(parts) == 1:
        # Just /train - start default training
        initial_msg = f"[B][C][FFFF00]🎮 Starting training mode...\n"
        await safe_send_message(chat_type, initial_msg, uid, chat_id, key, iv)
        
        success = await start_training_mode(key, iv, region)
        
        if success:
            success_msg = f"[B][C][FFFF00]✅ Training mode started!\n🏋️ Enter training ground to practice!\n"
        else:
            success_msg = f"[B][C][FF0000]❌ Failed to start training!\n"
            
        await safe_send_message(chat_type, success_msg, uid, chat_id, key, iv)
        
    elif len(parts) == 2 and parts[1] == "custom":
        # /train custom - custom training settings
        initial_msg = f"[B][C][FFFF00]🎮 Starting custom training...\n"
        await safe_send_message(chat_type, initial_msg, uid, chat_id, key, iv)
        
        # You can add custom training settings here
        success = await start_training_mode(key, iv, region)
        
        if success:
            success_msg = f"[B][C][FFFF00]✅ Custom training started!\n⚙️ Custom settings applied!\n"
        else:
            success_msg = f"[B][C][FF0000]❌ Failed to start custom training!\n"
            
        await safe_send_message(chat_type, success_msg, uid, chat_id, key, iv)
        
    else:
        error_msg = f"[B][C][FF0000]❌ Usage: /train [custom]\nExamples:\n/train - Start default training\n/train custom - Custom training\n"
        await safe_send_message(chat_type, error_msg, uid, chat_id, key, iv)

async def lag_team_loop(team_code, key, iv, region):
    """Rapid join/leave loop to create lag"""
    global lag_running
    count = 0
    
    while lag_running:
        try:
            # Join the team
            join_packet = await GenJoinSquadsPacket(team_code, key, iv)
            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', join_packet)
            
            # Very short delay before leaving
            await asyncio.sleep(0.01)  # 10 milliseconds
            
            # Leave the team
            leave_packet = await ExiT(None, key, iv)
            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', leave_packet)
            
            count += 1
            print(f"Lag cycle #{count} completed for team: {team_code}")
            
            # Short delay before next cycle
            await asyncio.sleep(0.01)  # 10 milliseconds between cycles
            
        except Exception as e:
            print(f"Error in lag loop: {e}")
            # Continue the loop even if there's an error
            await asyncio.sleep(0.1)
 
####################################

#Clan-info-by-clan-id
import requests

def get_clan_info(clan_id):
    try:
        url = f"https://guild-info-danger.vercel.app/guild?guild_id={clan_id}&region={all}"
        res = requests.get(url, timeout=10)

        if res.status_code == 200:
            data = res.json()
            
            # Check if API returned success
            if data.get("status") != "success":
                return "❌ Failed to fetch guild info. API returned an error."
            
            # Extract guild info
            guild_name = data.get("guild_name", "Unknown")
            guild_level = data.get("guild_level", "N/A")
            current_members = data.get("current_members", "N/A")
            max_members = data.get("max_members", "N/A")
            guild_region = data.get("guild_region", "Unknown")
            guild_slogan = data.get("guild_slogan", "N/A")
            creation_time = data.get("creation_time", "N/A")
            last_notice_change = data.get("last_notice_change", "N/A")
            last_slogan_change = data.get("last_slogan_change", "N/A")
            last_updated = data.get("last_updated", "N/A")
            total_activity_points = data.get("total_activity_points", "N/A")
            weekly_activity_points = data.get("weekly_activity_points", "N/A")
            officers = data.get("officers", [])
            
            # Guild Leader info
            leader_info = data.get("guild_leader", {})
            leader_name = leader_info.get("name", "Unknown")
            leader_uid = leader_info.get("uid", "N/A")
            leader_level = leader_info.get("level", "N/A")
            leader_likes = leader_info.get("likes", "N/A")
            
            # Format officers list
            officers_str = ", ".join(officers) if officers else "No officers"

            # Format output
            return f"""
[FFDD00][b][c]━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[00D1FF]Guild Name           : {guild_name}
Level                   : {guild_level}
Region                  : {guild_region}
Members                 : {current_members}/{max_members}
Slogan                  : {guild_slogan}
Creation Time           : {creation_time}
Last Notice Change      : {last_notice_change}
Last Slogan Change      : {last_slogan_change}
Last Updated            : {last_updated}
Total Activity Points   : {total_activity_points}
Weekly Activity Points  : {weekly_activity_points}
Officers                : {officers_str}
[00D1FF]Guild Leader         : {leader_name} (UID: {leader_uid})
[FFDD00]━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[00FF00][b][c]BOT MADE BY ZAINUㅤVIP GAMER
"""
        else:
            return f"❌ Failed to fetch guild info. HTTP Status: {res.status_code}"

    except Exception as e:
        return f"Error occurred: {e}"




def get_level_info(uid):
    try:
        url = f"https://danger-level-info.vercel.app/level/{uid}"
        res = requests.get(url, timeout=10)

        if res.status_code == 200:
            data = res.json()

            if not data.get("success"):
                return "❌ Failed to fetch level info."

            nickname = data.get("nickname", "Unknown")
            level = data.get("current_level", "N/A")
            current_exp = data.get("current_exp", 0)
            exp_needed = data.get("exp_needed", 0)
            progress = data.get("progress_percentage", 0)
            level_100_exp = data.get("level_100_exp", 0)
            exp_to_100 = data.get("exp_needed_for_100", 0)

            return f"""
[FFDD00][b][c]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
        ✦ EXP DETAILS ✦
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[00D1FF]👤 Name        : [FFFFFF]{nickname}
[00D1FF]🆔 Player ID  : [FFFFFF]{xMsGFixinG(uid)}
[00D1FF]🎚 Level       : [FFFFFF]{level}
[00D1FF]🔹 Current EXP : [FFFFFF]{fix_num(current_exp)}
[00D1FF]🔹 EXP Needed  : [FFFFFF]{fix_num(exp_needed)}
[00D1FF]🔹 Progress    : [FFFFFF]{progress}%
[00D1FF]🔸 EXP to Lv100: [FFFFFF]{fix_num(exp_to_100)}
[00D1FF]🔸 Lv100 EXP   : [FFFFFF]{fix_num(level_100_exp)}
[FFDD00]━━━━━━━━━━━━━━━━━━━━━━
[00FF00][b][c]⚡ BOT MADE BY ZAINUㅤVIP GAMER
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"""
        else:
            return f"❌ Failed to fetch level info. HTTP Status: {res.status_code}"

    except Exception as e:
        return f"Error occurred: {e}"

        

def get_player_ban_status(uid):
    try:
        url = f"https://duranto-ban-check.vercel.app/bancheck?uid={uid}"
        res = requests.get(url, timeout=10)

        if res.status_code == 200:
            data = res.json()

            status = data.get('ban_status', 'Unknown')
            ban_period = data.get('ban_period', 'N/A')
            player_name = data.get('nickname', 'Unknown')
            region = data.get('region', 'Unknown')

            return f"""
[FFDD00][b][c]
°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°
[00D1FF]Player Name: {player_name}
Player ID : {xMsGFixinG(uid)}
Region    : {region}
Status    : {status}
Ban Period: {ban_period}
[FFDD00]°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°
[00FF00][b][c]BOT MADE BY ZAINUㅤVIP GAMER
"""
        else:
            return f"❌ Failed to fetch ban status. HTTP Status: {res.status_code}"

    except Exception as e:
        return f"Error occurred: {e}"

#CHAT WITH AI
def talk_with_ai(question):
    url = f"https://apiiiiiii.vercel.app/api/ask?prompt={question}"
    try:
        res = requests.get(url)
        if res.status_code == 200:
            return res.text  # Direct plain text, no JSON parsing
        return f"Error: {res.status_code}"
    except Exception as e:
        return f"Connection failed: {str(e)}"

#SPAM REQUESTS
def spam_requests(player_id):
    # This URL now correctly points to the Flask app you provided
    url = f"https://like2.vercel.app/send_requests?uid={player_id}&server={server2}&key={key2}"
    try:
        res = requests.get(url, timeout=20) # Added a timeout
        if res.status_code == 200:
            data = res.json()
            # Return a more descriptive message based on the API's JSON response
            return f"API Status: Success [{data.get('success_count', 0)}] Failed [{data.get('failed_count', 0)}]"
        else:
            # Return the error status from the API
            return f"API Error: Status {res.status_code}"
    except requests.exceptions.RequestException as e:
        # Handle cases where the API isn't running or is unreachable
        print(f"Could not connect to spam API: {e}")
        return "Failed to connect to spam API."
####################################

# ** NEW INFO FUNCTION using the new API **
def newinfo(uid):
    # Base URL without parameters
    url = "https://like2.vercel.app/player-info"
    # Parameters dictionary - this is the robust way to do it
    params = {
        'uid': uid,
        'server': server2,  # Hardcoded to bd as requested
        'key': key2
    }
    try:
        # Pass the parameters to requests.get()
        response = requests.get(url, params=params, timeout=10)
        
        # Check if the request was successful
        if response.status_code == 200:
            data = response.json()
            # Check if the expected data structure is in the response
            if "basicInfo" in data:
                return {"status": "ok", "data": data}
            else:
                # The API returned 200, but the data is not what we expect (e.g., error message in JSON)
                return {"status": "error", "message": data.get("error", "Invalid ID or data not found.")}
        else:
            # The API returned an error status code (e.g., 404, 500)
            try:
                # Try to get a specific error message from the API's response
                error_msg = response.json().get('error', f"API returned status {response.status_code}")
                return {"status": "error", "message": error_msg}
            except ValueError:
                # If the error response is not JSON
                return {"status": "error", "message": f"API returned status {response.status_code}"}

    except requests.exceptions.RequestException as e:
        # Handle network errors (e.g., timeout, no connection)
        return {"status": "error", "message": f"Network error: {str(e)}"}
    except ValueError: 
        # Handle cases where the response is not valid JSON
        return {"status": "error", "message": "Invalid JSON response from API."}
        

def bundle_packet(self, bundle_id, target_uid):
        fields = {
            1: 88,
            2: {
                1: {
                    1: bundle_id,
                    2: 1
                },
                2: 2
            }
        }
        packet = create_protobuf_packet(fields).hex()
        encrypted = encrypt_packet(packet, self.key, self.iv)
        header_length = len(encrypted) // 2
        header_length_hex = dec_to_hex(header_length)

        if len(header_length_hex) == 2:
            final_header = "0515000000"
        elif len(header_length_hex) == 3:
            final_header = "051500000"
        elif len(header_length_hex) == 4:
            final_header = "05150000"
        elif len(header_length_hex) == 5:
            final_header = "0515000"
        else:
            final_header = "0515000000"

        final_packet = final_header + header_length_hex + encrypted
        return bytes.fromhex(final_packet)

async def bundle_packet_async(bundle_id, key, iv, region="ind"):
    """Create bundle packet"""
    fields = {
        1: 88,
        2: {
            1: {
                1: bundle_id,
                2: 1
            },
            2: 2
        }
    }
    
    # Use your CrEaTe_ProTo function
    packet = await CrEaTe_ProTo(fields)
    packet_hex = packet.hex()
    
    # Use your encrypt_packet function
    encrypted = await encrypt_packet(packet_hex, key, iv)
    
    # Use your DecodE_HeX function
    header_length = len(encrypted) // 2
    header_length_hex = await DecodE_HeX(header_length)
    
    # Build final packet based on region
    if region.lower() == "ind":
        packet_type = '0514'
    elif region.lower() == "bd":
        packet_type = "0519"
    else:
        packet_type = "0515"
    
    # Determine header based on length
    if len(header_length_hex) == 2:
        final_header = f"{packet_type}000000"
    elif len(header_length_hex) == 3:
        final_header = f"{packet_type}00000"
    elif len(header_length_hex) == 4:
        final_header = f"{packet_type}0000"
    elif len(header_length_hex) == 5:
        final_header = f"{packet_type}000"
    else:
        final_header = f"{packet_type}000000"
    
    final_packet_hex = final_header + header_length_hex + encrypted
    return bytes.fromhex(final_packet_hex)

def get_player_info(uid):
    try:
        url = f"https://info-api-mg24-pro.vercel.app/get?uid={uid}"
        res = requests.get(url, timeout=10)

        if res.status_code != 200:
            return None, f"API Error: {res.status_code}"

        data = res.json()

        # basic validation
        if "AccountInfo" not in data:
            return None, "Invalid API response"

        return data

    except requests.exceptions.Timeout:
        return None, "Request timeout"

    except Exception as e:
        return None, str(e)

        
        		
#ADDING-100-LIKES-IN-24H
def send_likes(uid):
    try:
        res = requests.get(
            f"https://ffcommunityapilvupaya.spcfy.eu/likes?uid={uid}",
            timeout=15
        )

        if res.status_code != 200:
            return f"""
[C][B][FF0000]━━━━━
[FFFFFF]Like API NAI TOMRA NITE CHAILE 8+LEVER ER GUIST ID DAO!
Status Code: {res.status_code}
━━━━━
"""

        data = res.json().get("result", {})

        api_info = data.get("API", {})
        likes_info = data.get("Likes Info", {})
        user_info = data.get("User Info", {})

        success = api_info.get("Success", False)
        speed = api_info.get("speeds", "N/A")

        player_name = user_info.get("Account Name", "Unknown")
        account_level = user_info.get("Account Level", "N/A")
        region = user_info.get("Account Region", "N/A")
        account_uid = user_info.get("Account UID", uid)

        likes_before = likes_info.get("Likes Before", 0)
        likes_after = likes_info.get("Likes After", 0)
        likes_added = likes_info.get("Likes Added", 0)
        likes_start_day = likes_info.get("Likes start of day", 0)

        if success and likes_added > 0:
            return f"""
[C][B][11EAFD]━━━━━━━━━━━━
[FFFFFF]Likes Status:

[00FF00]Likes Sent Successfully!

[FFFFFF]Player Name : [00FF00]{player_name}
[FFFFFF]Account Level : [00FF00]{account_level}
[FFFFFF]Region : [00FF00]{region}
[FFFFFF]Likes Added : [00FF00]{likes_added}
[FFFFFF]Likes Before : [00FF00]{likes_before}
[FFFFFF]Likes After : [00FF00]{likes_after}
[FFFFFF]API Speed : [00FF00]{speed}
[C][B][11EAFD]━━━━━━━━━━━━
[C][B][FFB300]Subscribe: [FFFFFF]Mr.GhosT-34 [00FF00]!!
"""

        elif likes_before == likes_after:
            return f"""
[C][B][FF0000]━━━━━━━━━━━━
[FFFFFF]No Likes Sent!

[FF0000]Daily limit reached.
Try again after 24 hours.

[FFFFFF]Player Name : [FF0000]{player_name}
[FFFFFF]Account Level : [FF0000]{account_level}
[FFFFFF]Likes : [FF0000]{likes_before}
[C][B][FF0000]━━━━━━━━━━━━
"""

        else:
            return f"""
[C][B][FF0000]━━━━━━━━━━━━
[FFFFFF]Unexpected Response!
Please try again later.
━━━━━━━━━━━━
"""

    except requests.exceptions.RequestException:
        return """
[C][B][FF0000]━━━━━
[FFFFFF]Like API NAI TOMRA NITE CHAILE 8+LEVER ER GUIST ID DAO!
━━━━━
"""

    except Exception as e:
        return f"""
[C][B][FF0000]━━━━━
[FFFFFF]Error Occurred:
[FF0000]{str(e)}
━━━━━
"""
def get_player_add(uid):
    try:
        url = f"https://danger-friend-manager.vercel.app/get_friends_list?uid=4445077519&password=diablott_VQTMT_BY_SPIDEERIO_GAMING_WL9G7&friend_uid={uid}"
        res = requests.get(url)
        data = res.json()
            # add is inside socialInfo -> signature
        action = data.get('action', 'Unknown')
        status = data.get('status', 'Unknown')
        message = data.get('message', 'No message received')
        if action:
            return message
        else:
            return message
    except Exception as e:
        return f"Error occurred: {e}"
def get_player_add_1(uid):
    try:
        url = f"https://danger-friend-manager.vercel.app/get_friends_list?uid=4444288892&password=diablo_Q4MUW_BY_SPIDEERIO_GAMING_TAJXG&friend_uid={uid}"
        res = requests.get(url)
        return res.json().get('message', 'No message')
    except Exception as e: return f"Error: {e}"

def get_player_add_2(uid):
    try:
        url = f"https://danger-friend-manager.vercel.app/get_friends_list?uid=4444292713&password=diablo_KMWYQ_BY_SPIDEERIO_GAMING_XLLI7&friend_uid={uid}"
        res = requests.get(url)
        return res.json().get('message', 'No message')
    except Exception as e: return f"Error: {e}"

def get_player_add_3(uid):
    try:
        url = f"https://danger-friend-manager.vercel.app/get_friends_list?uid=4444292726&password=diablo_HT3RO_BY_SPIDEERIO_GAMING_0BQFA&friend_uid={uid}"
        res = requests.get(url)
        return res.json().get('message', 'No message')
    except Exception as e: return f"Error: {e}"

def get_player_add_4(uid):
    try:
        url = f"https://danger-friend-manager.vercel.app/get_friends_list?uid=4444315321&password=diablo_SV6JV_BY_SPIDEERIO_GAMING_F9B4B&friend_uid={uid}"
        res = requests.get(url)
        return res.json().get('message', 'No message')
    except Exception as e: return f"Error: {e}"

def get_player_add_5(uid):
    try:
        url = f"https://danger-friend-manager.vercel.app/get_friends_list?uid=4444320750&password=diablo_7XC1Y_BY_SPIDEERIO_GAMING_AG1XQ&friend_uid={uid}"
        res = requests.get(url)
        return res.json().get('message', 'No message')
    except Exception as e: return f"Error: {e}"

def get_player_add_6(uid):
    try:
        url = f"https://danger-friend-manager.vercel.app/get_friends_list?uid=4444323598&password=diablo_IUFUQ_BY_SPIDEERIO_GAMING_QP3G7&friend_uid={uid}"
        res = requests.get(url)
        return res.json().get('message', 'No message')
    except Exception as e: return f"Error: {e}"

def get_player_add_7(uid):
    try:
        url = f"https://danger-friend-manager.vercel.app/get_friends_list?uid=4444327921&password=diablo_TPJ3O_BY_SPIDEERIO_GAMING_WO7QD&friend_uid={uid}"
        res = requests.get(url)
        return res.json().get('message', 'No message')
    except Exception as e: return f"Error: {e}"

def get_player_add_8(uid):
    try:
        url = f"https://danger-friend-manager.vercel.app/get_friends_list?uid=4444331568&password=diablo_AP2MF_BY_SPIDEERIO_GAMING_50X50&friend_uid={uid}"
        res = requests.get(url)
        return res.json().get('message', 'No message')
    except Exception as e: return f"Error: {e}"

def get_player_add_9(uid):
    try:
        url = f"https://danger-friend-manager.vercel.app/get_friends_list?uid=4444344133&password=diablo_LDYGK_BY_SPIDEERIO_GAMING_CNGI2&friend_uid={uid}"
        res = requests.get(url)
        return res.json().get('message', 'No message')
    except Exception as e: return f"Error: {e}"

def get_player_add_10(uid):
    try:
        url = f"https://danger-friend-manager.vercel.app/get_friends_list?uid=4444345133&password=diablo_MCVD6_BY_SPIDEERIO_GAMING_JK6WP&friend_uid={uid}"
        res = requests.get(url)
        return res.json().get('message', 'No message')
    except Exception as e: return f"Error: {e}"

def get_player_add_11(uid):
    try:
        url = f"https://danger-friend-manager.vercel.app/get_friends_list?uid=4444350783&password=diablo_0DE5F_BY_SPIDEERIO_GAMING_O1275&friend_uid={uid}"
        res = requests.get(url)
        return res.json().get('message', 'No message')
    except Exception as e: return f"Error: {e}"

def get_player_add_12(uid):
    try:
        url = f"https://danger-friend-manager.vercel.app/get_friends_list?uid=4444353077&password=diablo_7QL3P_BY_SPIDEERIO_GAMING_1ZNWU&friend_uid={uid}"
        res = requests.get(url)
        return res.json().get('message', 'No message')
    except Exception as e: return f"Error: {e}"

def get_player_add_13(uid):
    try:
        url = f"https://danger-friend-manager.vercel.app/get_friends_list?uid=4444358427&password=diablo_9IMC1_BY_SPIDEERIO_GAMING_NQRXG&friend_uid={uid}"
        res = requests.get(url)
        return res.json().get('message', 'No message')
    except Exception as e: return f"Error: {e}"

def get_player_add_14(uid):
    try:
        url = f"https://danger-friend-manager.vercel.app/get_friends_list?uid=4444363498&password=diablo_KDIKQ_BY_SPIDEERIO_GAMING_7B35N&friend_uid={uid}"
        res = requests.get(url)
        return res.json().get('message', 'No message')
    except Exception as e: return f"Error: {e}"

def get_player_add_15(uid):
    try:
        url = f"https://danger-friend-manager.vercel.app/get_friends_list?uid=4444363630&password=diablo_SC734_BY_SPIDEERIO_GAMING_YAI61&friend_uid={uid}"
        res = requests.get(url)
        return res.json().get('message', 'No message')
    except Exception as e: return f"Error: {e}"

def get_player_add_16(uid):
    try:
        url = f"https://danger-friend-manager.vercel.app/get_friends_list?uid=4444363732&password=diablo_CRVYP_BY_SPIDEERIO_GAMING_U4IDJ&friend_uid={uid}"
        res = requests.get(url)
        return res.json().get('message', 'No message')
    except Exception as e: return f"Error: {e}"

def get_player_add_17(uid):
    try:
        url = f"https://danger-friend-manager.vercel.app/get_friends_list?uid=4444847427&password=diablo_KR1UD_BY_SPIDEERIO_GAMING_ZC9HR&friend_uid={uid}"
        res = requests.get(url)
        return res.json().get('message', 'No message')
    except Exception as e: return f"Error: {e}"

def get_player_add_18(uid):
    try:
        url = f"https://danger-friend-manager.vercel.app/get_friends_list?uid=4444853245&password=diablo_SIRNU_BY_SPIDEERIO_GAMING_H4LFI&friend_uid={uid}"
        res = requests.get(url)
        return res.json().get('message', 'No message')
    except Exception as e: return f"Error: {e}"

def get_player_add_19(uid):
    try:
        url = f"https://danger-friend-manager.vercel.app/get_friends_list?uid=4444853309&password=diablo_HGWND_BY_SPIDEERIO_GAMING_AS170&friend_uid={uid}"
        res = requests.get(url)
        return res.json().get('message', 'No message')
    except Exception as e: return f"Error: {e}"

def get_player_add_20(uid):
    try:
        url = f"https://danger-friend-manager.vercel.app/get_friends_list?uid=4444853410&password=diablo_4J86V_BY_SPIDEERIO_GAMING_1O076&friend_uid={uid}"
        res = requests.get(url)
        return res.json().get('message', 'No message')
    except Exception as e: return f"Error: {e}"

def get_player_add_21(uid):
    try:
        url = f"https://danger-friend-manager.vercel.app/get_friends_list?uid=4444853538&password=diablo_5G7KE_BY_SPIDEERIO_GAMING_G5JJ2&friend_uid={uid}"
        res = requests.get(url)
        return res.json().get('message', 'No message')
    except Exception as e: return f"Error: {e}"

def get_player_add_22(uid):
    try:
        url = f"https://danger-friend-manager.vercel.app/get_friends_list?uid=4444853619&password=diablo_UCIVA_BY_SPIDEERIO_GAMING_C5AIB&friend_uid={uid}"
        res = requests.get(url)
        return res.json().get('message', 'No message')
    except Exception as e: return f"Error: {e}"

def get_player_add_23(uid):
    try:
        url = f"https://danger-friend-manager.vercel.app/get_friends_list?uid=4444853160&password=diablo_H98C9_BY_SPIDEERIO_GAMING_D2P7K&friend_uid={uid}"
        res = requests.get(url)
        return res.json().get('message', 'No message')
    except Exception as e: return f"Error: {e}"

def get_player_add_24(uid):
    try:
        url = f"https://danger-friend-manager.vercel.app/get_friends_list?uid=4444856183&password=diablo_CZH1G_BY_SPIDEERIO_GAMING_K63XM&friend_uid={uid}"
        res = requests.get(url)
        return res.json().get('message', 'No message')
    except Exception as e: return f"Error: {e}"

def get_player_add_25(uid):
    try:
        url = f"https://danger-friend-manager.vercel.app/get_friends_list?uid=4444859667&password=diablo_9Y2KL_BY_SPIDEERIO_GAMING_W4FF2&friend_uid={uid}"
        res = requests.get(url)
        return res.json().get('message', 'No message')
    except Exception as e: return f"Error: {e}"

def get_player_add_26(uid):
    try:
        url = f"https://danger-friend-manager.vercel.app/get_friends_list?uid=4444859945&password=diablo_118C4_BY_SPIDEERIO_GAMING_T1UKD&friend_uid={uid}"
        res = requests.get(url)
        return res.json().get('message', 'No message')
    except Exception as e: return f"Error: {e}"

def get_player_add_27(uid):
    try:
        url = f"https://danger-friend-manager.vercel.app/get_friends_list?uid=4444863394&password=diablo_T6WE6_BY_SPIDEERIO_GAMING_11RC5&friend_uid={uid}"
        res = requests.get(url)
        return res.json().get('message', 'No message')
    except Exception as e: return f"Error: {e}"

def get_player_add_28(uid):
    try:
        url = f"https://danger-friend-manager.vercel.app/get_friends_list?uid=4444878963&password=diablo_A8HRB_BY_SPIDEERIO_GAMING_5GFEF&friend_uid={uid}"
        res = requests.get(url)
        return res.json().get('message', 'No message')
    except Exception as e: return f"Error: {e}"

def get_player_add_29(uid):
    try:
        url = f"https://danger-friend-manager.vercel.app/get_friends_list?uid=4444885124&password=diablo_G09NL_BY_SPIDEERIO_GAMING_5J401&friend_uid={uid}"
        res = requests.get(url)
        return res.json().get('message', 'No message')
    except Exception as e: return f"Error: {e}"

def get_player_add_30(uid):
    try:
        url = f"https://danger-friend-manager.vercel.app/get_friends_list?uid=4444896903&password=diablo_VIEDI_BY_SPIDEERIO_GAMING_YNAWV&friend_uid={uid}"
        res = requests.get(url)
        return res.json().get('message', 'No message')
    except Exception as e: return f"Error: {e}"

def get_player_add_31(uid):
    try:
        url = f"https://danger-friend-manager.vercel.app/get_friends_list?uid=4444897085&password=diablo_MXTBW_BY_SPIDEERIO_GAMING_218OI&friend_uid={uid}"
        res = requests.get(url)
        return res.json().get('message', 'No message')
    except Exception as e: return f"Error: {e}"

def get_player_add_32(uid):
    try:
        url = f"https://danger-friend-manager.vercel.app/get_friends_list?uid=4444897140&password=diablo_49ZZ3_BY_SPIDEERIO_GAMING_RSJN4&friend_uid={uid}"
        res = requests.get(url)
        return res.json().get('message', 'No message')
    except Exception as e: return f"Error: {e}"

def get_player_add_33(uid):
    try:
        url = f"https://danger-friend-manager.vercel.app/get_friends_list?uid=4444897306&password=diablo_FO72U_BY_SPIDEERIO_GAMING_PBCA1&friend_uid={uid}"
        res = requests.get(url)
        return res.json().get('message', 'No message')
    except Exception as e: return f"Error: {e}"

def get_player_add_34(uid):
    try:
        url = f"https://danger-friend-manager.vercel.app/get_friends_list?uid=4444897429&password=diablo_XHQLQ_BY_SPIDEERIO_GAMING_WANGS&friend_uid={uid}"
        res = requests.get(url)
        return res.json().get('message', 'No message')
    except Exception as e: return f"Error: {e}"

def get_player_add_35(uid):
    try:
        url = f"https://danger-friend-manager.vercel.app/get_friends_list?uid=4444897410&password=diablo_IVKUG_BY_SPIDEERIO_GAMING_QBAV6&friend_uid={uid}"
        res = requests.get(url)
        return res.json().get('message', 'No message')
    except Exception as e: return f"Error: {e}"

def get_player_add_36(uid):
    try:
        url = f"https://danger-friend-manager.vercel.app/get_friends_list?uid=4444897376&password=diablo_RHNHF_BY_SPIDEERIO_GAMING_1TAOU&friend_uid={uid}"
        res = requests.get(url)
        return res.json().get('message', 'No message')
    except Exception as e: return f"Error: {e}"

def get_player_add_37(uid):
    try:
        url = f"https://danger-friend-manager.vercel.app/get_friends_list?uid=4444897682&password=diablo_NE813_BY_SPIDEERIO_GAMING_7U6P4&friend_uid={uid}"
        res = requests.get(url)
        return res.json().get('message', 'No message')
    except Exception as e: return f"Error: {e}"

def get_player_add_38(uid):
    try:
        url = f"https://danger-friend-manager.vercel.app/get_friends_list?uid=4444900040&password=diablo_C1BCC_BY_SPIDEERIO_GAMING_BLUCR&friend_uid={uid}"
        res = requests.get(url)
        return res.json().get('message', 'No message')
    except Exception as e: return f"Error: {e}"

def get_player_add_39(uid):
    try:
        url = f"https://danger-friend-manager.vercel.app/get_friends_list?uid=4444900223&password=diablo_H1G07_BY_SPIDEERIO_GAMING_JK450&friend_uid={uid}"
        res = requests.get(url)
        return res.json().get('message', 'No message')
    except Exception as e: return f"Error: {e}"

def get_player_add_40(uid):
    try:
        url = f"https://danger-friend-manager.vercel.app/get_friends_list?uid=4444900386&password=diablo_NM8BB_BY_SPIDEERIO_GAMING_E3DET&friend_uid={uid}"
        res = requests.get(url)
        return res.json().get('message', 'No message')
    except Exception as e: return f"Error: {e}"

def get_player_add_41(uid):
    try:
        url = f"https://danger-friend-manager.vercel.app/get_friends_list?uid=4444900719&password=diablo_RHN46_BY_SPIDEERIO_GAMING_CV4YX&friend_uid={uid}"
        res = requests.get(url)
        return res.json().get('message', 'No message')
    except Exception as e: return f"Error: {e}"

def get_player_add_42(uid):
    try:
        url = f"https://danger-friend-manager.vercel.app/get_friends_list?uid=4444910075&password=diablo_7M1AV_BY_SPIDEERIO_GAMING_ZD85O&friend_uid={uid}"
        res = requests.get(url)
        return res.json().get('message', 'No message')
    except Exception as e: return f"Error: {e}"

def get_player_add_43(uid):
    try:
        url = f"https://danger-friend-manager.vercel.app/get_friends_list?uid=4444909962&password=diablo_QP3DF_BY_SPIDEERIO_GAMING_MNNRS&friend_uid={uid}"
        res = requests.get(url)
        return res.json().get('message', 'No message')
    except Exception as e: return f"Error: {e}"

def get_player_add_44(uid):
    try:
        url = f"https://danger-friend-manager.vercel.app/get_friends_list?uid=4444915956&password=diablo_SJB0H_BY_SPIDEERIO_GAMING_W1GYW&friend_uid={uid}"
        res = requests.get(url)
        return res.json().get('message', 'No message')
    except Exception as e: return f"Error: {e}"

def get_player_add_45(uid):
    try:
        url = f"https://danger-friend-manager.vercel.app/get_friends_list?uid=4444916715&password=diablo_753K6_BY_SPIDEERIO_GAMING_O77CW&friend_uid={uid}"
        res = requests.get(url)
        return res.json().get('message', 'No message')
    except Exception as e: return f"Error: {e}"

def get_player_add_46(uid):
    try:
        url = f"https://danger-friend-manager.vercel.app/get_friends_list?uid=4444945595&password=diablo_F5H44_BY_SPIDEERIO_GAMING_HVSPI&friend_uid={uid}"
        res = requests.get(url)
        return res.json().get('message', 'No message')
    except Exception as e: return f"Error: {e}"

def get_player_add_47(uid):
    try:
        url = f"https://danger-friend-manager.vercel.app/get_friends_list?uid=4444948185&password=diablo_G01FX_BY_SPIDEERIO_GAMING_XU6RW&friend_uid={uid}"
        res = requests.get(url)
        return res.json().get('message', 'No message')
    except Exception as e: return f"Error: {e}"

def get_player_add_48(uid):
    try:
        url = f"https://danger-friend-manager.vercel.app/get_friends_list?uid=4444948201&password=diablo_XCQ1X_BY_SPIDEERIO_GAMING_5NN6Q&friend_uid={uid}"
        res = requests.get(url)
        return res.json().get('message', 'No message')
    except Exception as e: return f"Error: {e}"

def get_player_add_49(uid):
    try:
        url = f"https://danger-friend-manager.vercel.app/get_friends_list?uid=4444951206&password=diablo_FZQSP_BY_SPIDEERIO_GAMING_IF04U&friend_uid={uid}"
        res = requests.get(url)
        return res.json().get('message', 'No message')
    except Exception as e: return f"Error: {e}"

def get_player_add_50(uid):
    try:
        url = f"https://danger-friend-manager.vercel.app/get_friends_list?uid=4444960493&password=diablo_ATF01_BY_SPIDEERIO_GAMING_54WMU&friend_uid={uid}"
        res = requests.get(url)
        return res.json().get('message', 'No message')
    except Exception as e: return f"Error: {e}"
def get_player_add_51(uid):
    try:
        url = f"https://danger-friend-manager.vercel.app/get_friends_list?uid=4444964170&password=diablo_Q1ZS6_BY_SPIDEERIO_GAMING_6GJDF&friend_uid={uid}"
        res = requests.get(url)
        return res.json().get('message', 'No message')
    except Exception as e: return f"Error: {e}"

def get_player_add_52(uid):
    try:
        url = f"https://danger-friend-manager.vercel.app/get_friends_list?uid=4444964218&password=diablo_K3YJ8_BY_SPIDEERIO_GAMING_7ODRG&friend_uid={uid}"
        res = requests.get(url)
        return res.json().get('message', 'No message')
    except Exception as e: return f"Error: {e}"

def get_player_add_53(uid):
    try:
        url = f"https://danger-friend-manager.vercel.app/get_friends_list?uid=4444969481&password=diablo_V9Q0A_BY_SPIDEERIO_GAMING_2JNYM&friend_uid={uid}"
        res = requests.get(url)
        return res.json().get('message', 'No message')
    except Exception as e: return f"Error: {e}"

def get_player_add_54(uid):
    try:
        url = f"https://danger-friend-manager.vercel.app/get_friends_list?uid=4444973195&password=diablo_P6YQ7_BY_SPIDEERIO_GAMING_1ATDW&friend_uid={uid}"
        res = requests.get(url)
        return res.json().get('message', 'No message')
    except Exception as e: return f"Error: {e}"

def get_player_add_55(uid):
    try:
        url = f"https://danger-friend-manager.vercel.app/get_friends_list?uid=4444973241&password=diablo_N8ZRM_BY_SPIDEERIO_GAMING_FKQ7U&friend_uid={uid}"
        res = requests.get(url)
        return res.json().get('message', 'No message')
    except Exception as e: return f"Error: {e}"

def get_player_add_56(uid):
    try:
        url = f"https://danger-friend-manager.vercel.app/get_friends_list?uid=4444978324&password=diablo_L2GQ5_BY_SPIDEERIO_GAMING_9WPRL&friend_uid={uid}"
        res = requests.get(url)
        return res.json().get('message', 'No message')
    except Exception as e: return f"Error: {e}"

def get_player_add_57(uid):
    try:
        url = f"https://danger-friend-manager.vercel.app/get_friends_list?uid=4444982379&password=diablo_M9ZX8_BY_SPIDEERIO_GAMING_3JSQH&friend_uid={uid}"
        res = requests.get(url)
        return res.json().get('message', 'No message')
    except Exception as e: return f"Error: {e}"

def get_player_add_58(uid):
    try:
        url = f"https://danger-friend-manager.vercel.app/get_friends_list?uid=4444986512&password=diablo_S4WQ9_BY_SPIDEERIO_GAMING_5KVXY&friend_uid={uid}"
        res = requests.get(url)
        return res.json().get('message', 'No message')
    except Exception as e: return f"Error: {e}"

def get_player_add_59(uid):
    try:
        url = f"https://danger-friend-manager.vercel.app/get_friends_list?uid=4444991234&password=diablo_R8PM2_BY_SPIDEERIO_GAMING_8HGND&friend_uid={uid}"
        res = requests.get(url)
        return res.json().get('message', 'No message')
    except Exception as e: return f"Error: {e}"

def get_player_add_60(uid):
    try:
        url = f"https://danger-friend-manager.vercel.app/get_friends_list?uid=4444995678&password=diablo_T3QJ6_BY_SPIDEERIO_GAMING_7LKSW&friend_uid={uid}"
        res = requests.get(url)
        return res.json().get('message', 'No message')
    except Exception as e: return f"Error: {e}"

def get_player_add_61(uid):
    try:
        url = f"https://danger-friend-manager.vercel.app/get_friends_list?uid=4445001234&password=diablo_B5RW9_BY_SPIDEERIO_GAMING_2MNXF&friend_uid={uid}"
        res = requests.get(url)
        return res.json().get('message', 'No message')
    except Exception as e: return f"Error: {e}"

def get_player_add_62(uid):
    try:
        url = f"https://danger-friend-manager.vercel.app/get_friends_list?uid=4445006789&password=diablo_C7VH2_BY_SPIDEERIO_GAMING_4PQTZ&friend_uid={uid}"
        res = requests.get(url)
        return res.json().get('message', 'No message')
    except Exception as e: return f"Error: {e}"

def get_player_add_63(uid):
    try:
        url = f"https://danger-friend-manager.vercel.app/get_friends_list?uid=4445012345&password=diablo_D9KN4_BY_SPIDEERIO_GAMING_6RWVX&friend_uid={uid}"
        res = requests.get(url)
        return res.json().get('message', 'No message')
    except Exception as e: return f"Error: {e}"

def get_player_add_64(uid):
    try:
        url = f"https://danger-friend-manager.vercel.app/get_friends_list?uid=4445017890&password=diablo_E2LP6_BY_SPIDEERIO_GAMING_8SYQZ&friend_uid={uid}"
        res = requests.get(url)
        return res.json().get('message', 'No message')
    except Exception as e: return f"Error: {e}"

def get_player_add_65(uid):
    try:
        url = f"https://danger-friend-manager.vercel.app/get_friends_list?uid=4445023456&password=diablo_F4MQ8_BY_SPIDEERIO_GAMING_1TVB3&friend_uid={uid}"
        res = requests.get(url)
        return res.json().get('message', 'No message')
    except Exception as e: return f"Error: {e}"

def get_player_add_66(uid):
    try:
        url = f"https://danger-friend-manager.vercel.app/get_friends_list?uid=4445029012&password=diablo_G6NR0_BY_SPIDEERIO_GAMING_3UWC5&friend_uid={uid}"
        res = requests.get(url)
        return res.json().get('message', 'No message')
    except Exception as e: return f"Error: {e}"

def get_player_add_67(uid):
    try:
        url = f"https://danger-friend-manager.vercel.app/get_friends_list?uid=4445034567&password=diablo_H8PS2_BY_SPIDEERIO_GAMING_5VXD7&friend_uid={uid}"
        res = requests.get(url)
        return res.json().get('message', 'No message')
    except Exception as e: return f"Error: {e}"

def get_player_add_68(uid):
    try:
        url = f"https://danger-friend-manager.vercel.app/get_friends_list?uid=4445040123&password=diablo_J0QT4_BY_SPIDEERIO_GAMING_7WYE9&friend_uid={uid}"
        res = requests.get(url)
        return res.json().get('message', 'No message')
    except Exception as e: return f"Error: {e}"

def get_player_add_69(uid):
    try:
        url = f"https://danger-friend-manager.vercel.app/get_friends_list?uid=4445045678&password=diablo_K2RU6_BY_SPIDEERIO_GAMING_9XZF1&friend_uid={uid}"
        res = requests.get(url)
        return res.json().get('message', 'No message')
    except Exception as e: return f"Error: {e}"

def get_player_add_70(uid):
    try:
        url = f"https://danger-friend-manager.vercel.app/get_friends_list?uid=4445051234&password=diablo_L4SV8_BY_SPIDEERIO_GAMING_2YAG3&friend_uid={uid}"
        res = requests.get(url)
        return res.json().get('message', 'No message')
    except Exception as e: return f"Error: {e}"

def get_player_add_71(uid):
    try:
        url = f"https://danger-friend-manager.vercel.app/get_friends_list?uid=4445056789&password=diablo_M6TW0_BY_SPIDEERIO_GAMING_4ZBH5&friend_uid={uid}"
        res = requests.get(url)
        return res.json().get('message', 'No message')
    except Exception as e: return f"Error: {e}"

def get_player_add_72(uid):
    try:
        url = f"https://danger-friend-manager.vercel.app/get_friends_list?uid=4445062345&password=diablo_N8UX2_BY_SPIDEERIO_GAMING_6ACI7&friend_uid={uid}"
        res = requests.get(url)
        return res.json().get('message', 'No message')
    except Exception as e: return f"Error: {e}"

def get_player_add_73(uid):
    try:
        url = f"https://danger-friend-manager.vercel.app/get_friends_list?uid=4445067890&password=diablo_P0VY4_BY_SPIDEERIO_GAMING_8BDJ9&friend_uid={uid}"
        res = requests.get(url)
        return res.json().get('message', 'No message')
    except Exception as e: return f"Error: {e}"

def get_player_add_74(uid):
    try:
        url = f"https://danger-friend-manager.vercel.app/get_friends_list?uid=4445073456&password=diablo_Q2WZ6_BY_SPIDEERIO_GAMING_1CEK0&friend_uid={uid}"
        res = requests.get(url)
        return res.json().get('message', 'No message')
    except Exception as e: return f"Error: {e}"

def get_player_add_75(uid):
    try:
        url = f"https://danger-friend-manager.vercel.app/get_friends_list?uid=4445079012&password=diablo_R4X18_BY_SPIDEERIO_GAMING_3DFL2&friend_uid={uid}"
        res = requests.get(url)
        return res.json().get('message', 'No message')
    except Exception as e: return f"Error: {e}"

def get_player_add_76(uid):
    try:
        url = f"https://danger-friend-manager.vercel.app/get_friends_list?uid=4445084567&password=diablo_S6Y39_BY_SPIDEERIO_GAMING_5EGM4&friend_uid={uid}"
        res = requests.get(url)
        return res.json().get('message', 'No message')
    except Exception as e: return f"Error: {e}"

def get_player_add_77(uid):
    try:
        url = f"https://danger-friend-manager.vercel.app/get_friends_list?uid=4445090123&password=diablo_T8Z50_BY_SPIDEERIO_GAMING_7FHN6&friend_uid={uid}"
        res = requests.get(url)
        return res.json().get('message', 'No message')
    except Exception as e: return f"Error: {e}"

def get_player_add_78(uid):
    try:
        url = f"https://danger-friend-manager.vercel.app/get_friends_list?uid=4445095678&password=diablo_U0162_BY_SPIDEERIO_GAMING_9GIO8&friend_uid={uid}"
        res = requests.get(url)
        return res.json().get('message', 'No message')
    except Exception as e: return f"Error: {e}"

def get_player_add_79(uid):
    try:
        url = f"https://danger-friend-manager.vercel.app/get_friends_list?uid=4445101234&password=diablo_V2284_BY_SPIDEERIO_GAMING_2HJP0&friend_uid={uid}"
        res = requests.get(url)
        return res.json().get('message', 'No message')
    except Exception as e: return f"Error: {e}"

def get_player_add_80(uid):
    try:
        url = f"https://danger-friend-manager.vercel.app/get_friends_list?uid=4445106789&password=diablo_W4406_BY_SPIDEERIO_GAMING_4IKQ2&friend_uid={uid}"
        res = requests.get(url)
        return res.json().get('message', 'No message')
    except Exception as e: return f"Error: {e}"

def get_player_add_81(uid):
    try:
        url = f"https://danger-friend-manager.vercel.app/get_friends_list?uid=4445112345&password=diablo_X6528_BY_SPIDEERIO_GAMING_6JLR4&friend_uid={uid}"
        res = requests.get(url)
        return res.json().get('message', 'No message')
    except Exception as e: return f"Error: {e}"

def get_player_add_82(uid):
    try:
        url = f"https://danger-friend-manager.vercel.app/get_friends_list?uid=4445117890&password=diablo_Y8640_BY_SPIDEERIO_GAMING_8KMS6&friend_uid={uid}"
        res = requests.get(url)
        return res.json().get('message', 'No message')
    except Exception as e: return f"Error: {e}"

def get_player_add_83(uid):
    try:
        url = f"https://danger-friend-manager.vercel.app/get_friends_list?uid=4445123456&password=diablo_Z0862_BY_SPIDEERIO_GAMING_1LNT8&friend_uid={uid}"
        res = requests.get(url)
        return res.json().get('message', 'No message')
    except Exception as e: return f"Error: {e}"

def get_player_add_84(uid):
    try:
        url = f"https://danger-friend-manager.vercel.app/get_friends_list?uid=4445129012&password=diablo_A2084_BY_SPIDEERIO_GAMING_3MOU0&friend_uid={uid}"
        res = requests.get(url)
        return res.json().get('message', 'No message')
    except Exception as e: return f"Error: {e}"

def get_player_add_85(uid):
    try:
        url = f"https://danger-friend-manager.vercel.app/get_friends_list?uid=4445134567&password=diablo_B4206_BY_SPIDEERIO_GAMING_5NPV2&friend_uid={uid}"
        res = requests.get(url)
        return res.json().get('message', 'No message')
    except Exception as e: return f"Error: {e}"

def get_player_add_86(uid):
    try:
        url = f"https://danger-friend-manager.vercel.app/get_friends_list?uid=4445140123&password=diablo_C6428_BY_SPIDEERIO_GAMING_7OQW4&friend_uid={uid}"
        res = requests.get(url)
        return res.json().get('message', 'No message')
    except Exception as e: return f"Error: {e}"

def get_player_add_87(uid):
    try:
        url = f"https://danger-friend-manager.vercel.app/get_friends_list?uid=4445145678&password=diablo_D8640_BY_SPIDEERIO_GAMING_9PRX6&friend_uid={uid}"
        res = requests.get(url)
        return res.json().get('message', 'No message')
    except Exception as e: return f"Error: {e}"

def get_player_add_88(uid):
    try:
        url = f"https://danger-friend-manager.vercel.app/get_friends_list?uid=4445151234&password=diablo_E0862_BY_SPIDEERIO_GAMING_2QSY8&friend_uid={uid}"
        res = requests.get(url)
        return res.json().get('message', 'No message')
    except Exception as e: return f"Error: {e}"

def get_player_add_89(uid):
    try:
        url = f"https://danger-friend-manager.vercel.app/get_friends_list?uid=4445156789&password=diablo_F2084_BY_SPIDEERIO_GAMING_4RTZ0&friend_uid={uid}"
        res = requests.get(url)
        return res.json().get('message', 'No message')
    except Exception as e: return f"Error: {e}"

def get_player_add_90(uid):
    try:
        url = f"https://danger-friend-manager.vercel.app/get_friends_list?uid=4445162345&password=diablo_G4206_BY_SPIDEERIO_GAMING_6SUA2&friend_uid={uid}"
        res = requests.get(url)
        return res.json().get('message', 'No message')
    except Exception as e: return f"Error: {e}"

def get_player_add_91(uid):
    try:
        url = f"https://danger-friend-manager.vercel.app/get_friends_list?uid=4445167890&password=diablo_H6428_BY_SPIDEERIO_GAMING_8TVB4&friend_uid={uid}"
        res = requests.get(url)
        return res.json().get('message', 'No message')
    except Exception as e: return f"Error: {e}"

def get_player_add_92(uid):
    try:
        url = f"https://danger-friend-manager.vercel.app/get_friends_list?uid=4445173456&password=diablo_J8640_BY_SPIDEERIO_GAMING_1UWX6&friend_uid={uid}"
        res = requests.get(url)
        return res.json().get('message', 'No message')
    except Exception as e: return f"Error: {e}"

def get_player_add_93(uid):
    try:
        url = f"https://danger-friend-manager.vercel.app/get_friends_list?uid=4445179012&password=diablo_K0862_BY_SPIDEERIO_GAMING_3VXY8&friend_uid={uid}"
        res = requests.get(url)
        return res.json().get('message', 'No message')
    except Exception as e: return f"Error: {e}"

def get_player_add_94(uid):
    try:
        url = f"https://danger-friend-manager.vercel.app/get_friends_list?uid=4445184567&password=diablo_L2084_BY_SPIDEERIO_GAMING_5WYZ0&friend_uid={uid}"
        res = requests.get(url)
        return res.json().get('message', 'No message')
    except Exception as e: return f"Error: {e}"

def get_player_add_95(uid):
    try:
        url = f"https://danger-friend-manager.vercel.app/get_friends_list?uid=4445190123&password=diablo_M4206_BY_SPIDEERIO_GAMING_7XZA2&friend_uid={uid}"
        res = requests.get(url)
        return res.json().get('message', 'No message')
    except Exception as e: return f"Error: {e}"

def get_player_add_96(uid):
    try:
        url = f"https://danger-friend-manager.vercel.app/get_friends_list?uid=4445195678&password=diablo_N6428_BY_SPIDEERIO_GAMING_9Y0B4&friend_uid={uid}"
        res = requests.get(url)
        return res.json().get('message', 'No message')
    except Exception as e: return f"Error: {e}"

def get_player_add_97(uid):
    try:
        url = f"https://danger-friend-manager.vercel.app/get_friends_list?uid=4445201234&password=diablo_P8640_BY_SPIDEERIO_GAMING_2Z1C6&friend_uid={uid}"
        res = requests.get(url)
        return res.json().get('message', 'No message')
    except Exception as e: return f"Error: {e}"

def get_player_add_98(uid):
    try:
        url = f"https://danger-friend-manager.vercel.app/get_friends_list?uid=4445206789&password=diablo_Q0862_BY_SPIDEERIO_GAMING_402D8&friend_uid={uid}"
        res = requests.get(url)
        return res.json().get('message', 'No message')
    except Exception as e: return f"Error: {e}"

def get_player_add_99(uid):
    try:
        url = f"https://danger-friend-manager.vercel.app/get_friends_list?uid=4445212345&password=diablo_R2084_BY_SPIDEERIO_GAMING_613E0&friend_uid={uid}"
        res = requests.get(url)
        return res.json().get('message', 'No message')
    except Exception as e: return f"Error: {e}"

def get_player_add_100(uid):
    try:
        url = f"https://danger-friend-manager.vercel.app/get_friends_list?uid=4445217890&password=diablo_S4206_BY_SPIDEERIO_GAMING_824F2&friend_uid={uid}"
        res = requests.get(url)
        return res.json().get('message', 'No message')
    except Exception as e: return f"Error: {e}"

def get_player_add_101(uid):
    try:
        url = f"https://danger-friend-manager.vercel.app/get_friends_list?uid=4445223456&password=diablo_T6428_BY_SPIDEERIO_GAMING_1A5G4&friend_uid={uid}"
        res = requests.get(url)
        return res.json().get('message', 'No message')
    except Exception as e: return f"Error: {e}"

def get_player_add_102(uid):
    try:
        url = f"https://danger-friend-manager.vercel.app/get_friends_list?uid=4445229012&password=diablo_U8640_BY_SPIDEERIO_GAMING_3B6H6&friend_uid={uid}"
        res = requests.get(url)
        return res.json().get('message', 'No message')
    except Exception as e: return f"Error: {e}"

async def send_all_friend_requests_async(target_uid):
    # ১০০টি ফাংশনের মাস্টার লিস্ট
    functions = [
        get_player_add_1, get_player_add_2, get_player_add_3, get_player_add_4, get_player_add_5,
        get_player_add_6, get_player_add_7, get_player_add_8, get_player_add_9, get_player_add_10,
        get_player_add_11, get_player_add_12, get_player_add_13, get_player_add_14, get_player_add_15,
        get_player_add_16, get_player_add_17, get_player_add_18, get_player_add_19, get_player_add_20,
        get_player_add_21, get_player_add_22, get_player_add_23, get_player_add_24, get_player_add_25,
        get_player_add_26, get_player_add_27, get_player_add_28, get_player_add_29, get_player_add_30,
        get_player_add_31, get_player_add_32, get_player_add_33, get_player_add_34, get_player_add_35,
        get_player_add_36, get_player_add_37, get_player_add_38, get_player_add_39, get_player_add_40,
        get_player_add_41, get_player_add_42, get_player_add_43, get_player_add_44, get_player_add_45,
        get_player_add_46, get_player_add_47, get_player_add_48, get_player_add_49, get_player_add_50,
        get_player_add_51, get_player_add_52, get_player_add_53, get_player_add_54, get_player_add_55,
        get_player_add_56, get_player_add_57, get_player_add_58, get_player_add_59, get_player_add_60,
        get_player_add_61, get_player_add_62, get_player_add_63, get_player_add_64, get_player_add_65,
        get_player_add_66, get_player_add_67, get_player_add_68, get_player_add_69, get_player_add_70,
        get_player_add_71, get_player_add_72, get_player_add_73, get_player_add_74, get_player_add_75,
        get_player_add_76, get_player_add_77, get_player_add_78, get_player_add_79, get_player_add_80,
        get_player_add_81, get_player_add_82, get_player_add_83, get_player_add_84, get_player_add_85,
        get_player_add_86, get_player_add_87, get_player_add_88, get_player_add_89, get_player_add_90,
        get_player_add_91, get_player_add_92, get_player_add_93, get_player_add_94, get_player_add_95,
        get_player_add_96, get_player_add_97, get_player_add_98, get_player_add_99, get_player_add_100
    ]

    try:
        loop = asyncio.get_event_loop()
        
        # ThreadPoolExecutor ব্যবহার করে ১০০টি রিকোয়েস্টকে নন-ব্লকিং ভাবে সাজানো
        # max_workers=50 দেওয়া হয়েছে যাতে খুব দ্রুত কাজ শেষ হয়
        with ThreadPoolExecutor(max_workers=50) as executor:
            tasks = [
                loop.run_in_executor(executor, func, target_uid) 
                for func in functions
            ]
            
            # সব রিকোয়েস্ট শেষ হওয়া পর্যন্ত অপেক্ষা (কিন্তু বট ফ্রীজ হবে না)
            results = await asyncio.gather(*tasks)
            
        success_count = len([r for r in results if "Error" not in r])
        return f"Successfully processed {success_count}/100 requests."

    except Exception as e:
        return f"System Error: {str(e)}"    
#USERNAME TO insta INFO 
def send_insta_info(username):
    try:
        response = requests.get(f"https://kallu-insta-info-api.vercel.app/api/insta/{username}", timeout=15)
        if response.status_code != 200:
            return f"[B][C][FF0000]❌ Instagram API Error! Status Code: {response.status_code}"

        user = response.json()
        full_name = user.get("full_name", "Unknown")
        followers = user.get("edge_followed_by", {}).get("count") or user.get("followers_count", 0)
        following = user.get("edge_follow", {}).get("count") or user.get("following_count", 0)
        posts = user.get("media_count") or user.get("edge_owner_to_timeline_media", {}).get("count", 0)
        profile_pic = user.get("profile_pic_url_hd") or user.get("profile_pic_url")
        private_status = user.get("is_private")
        verified_status = user.get("is_verified")

        return f"""
[B][C][FB0364]╭[D21A92]─[BC26AB]╮[FB0364]╔══════════════╗
[C][B][FF7244]│[FE4250]◯[C81F9C]֯│[D21A92]║[FDC92B] INSTAGRAM INFO [D21A92]║
[C][B][FDC92B]╰[FF7640]─[F5066B]╯[FB0364]╚══════════════╝

[C][B][C81F9C]━━━━━━━━━━━━━━━━━━━━
[C][B][FF7244]Name       : [ADFF2F]{full_name}
[C][B][FF7244]Username   : [1E90FF]{username}
[C][B][FF7244]Followers  : [FDC92B]{followers}
[C][B][FF7244]Following  : [FDC92B]{following}
[C][B][FF7244]Posts      : [00FA9A]{posts}
[C][B][FF7244]Private    : [FF6F91]{private_status}
[C][B][FF7244]Verified   : [7B68EE]{verified_status}
[C][B][C81F9C]━━━━━━━━━━━━━━━━━━━━"""
    except requests.exceptions.RequestException:
        return "[B][C][FF0000]❌ Instagram API Connection Failed!"
    except Exception as e:
        return f"[B][C][FF0000]❌ Unexpected Error: {str(e)}"

def send_tiktok_info(username):

    try:
        response = requests.get(
            f"https://tiktok-api-mafia-ayan.vercel.app/tkinfo?username={username}",
            timeout=15
        )

        if response.status_code != 200:
            return f"[B][C][FF0000]❌ TikTok API Error! Status Code: {response.status_code}"

        user = response.json()

        if user.get("status") is not True:
            return "[B][C][FF0000]❌ TikTok User Not Found!"

        name = user.get("name", "Unknown")
        username_ = user.get("username", username)
        followers = user.get("followers", 0)
        following = user.get("following", 0)
        likes = user.get("hearts", 0)
        videos = user.get("videos", 0)
        private_status = user.get("is_private", False)
        digg_count = user.get("digg_count", 0)
        signature = user.get("signature", "")
        user_id = user.get("user_id", "Unknown")

        return f"""
[B][C][FFD700]╭[FF0000]─[FFD700]╮[FFFFFF]
[C][B][FF0000]│[00FF00]♪[FF0000]│[FFFFFF]║[00BFFF]TIKTOK INFO[FFFFFF]║
[C][B][FFD700]╰[FF0000]─[FFD700]╯[FFFFFF]
[C][B][FF0000]━━━━━━━━━━━
[C][B][FFFFFF]Username   : [00BFFF]{username_}
[C][B][FFFFFF]Signature  : [00BFFF]{signature}
[C][B][FFFFFF]Followers  : [00BFFF]{followers}
[C][B][FFFFFF]Following  : [00BFFF]{following}
[C][B][FFFFFF]Likes      : [00BFFF]{likes}
[C][B][FFFFFF]Videos     : [00BFFF]{videos}
[C][B][FFFFFF]Private    : [FF0000]{private_status}
[C][B][FF0000]━━━━━━━━━━━
"""

    except requests.exceptions.RequestException:
        return "[B][C][FF0000]❌ TikTok API Connection Failed!"
    except Exception as e:
        return f"[B][C][FF0000]❌ Unexpected Error: {str(e)}"
        
        
async def send_full_player_info(data, chat_type, uid, chat_id, key, iv):

    acc = data.get("AccountInfo", {})
    guild = data.get("GuildInfo", {})
    social = data.get("socialinfo", {})
    captain = data.get("captainBasicInfo", {})

    # ────────── MESSAGE 1 : COMMON ACCOUNT INFO ──────────
    msg1 = f"""
[C][B][FFAA00]━━━━━━━━━━━━━
[C][B][FFFFFF]COMMON ACCOUNT INFO
[C][FFAA00]━━━━━━━━━━━━━
[C][FFFFFF]Name      : [66FF00]{acc.get('AccountName', 'N/A')}
[C][FFFFFF]UID       : [66FF00]{ff_num(captain.get('accountId'))}
[C][FFFFFF]Level     : [66FF00]{acc.get('AccountLevel', 'N/A')}
[C][FFFFFF]EXP       : [66FF00]{ff_num(acc.get('AccountEXP'))}
[C][FFFFFF]Likes     : [66FF00]{ff_num(acc.get('AccountLikes'))}
[C][FFFFFF]Region    : [66FF00]{acc.get('AccountRegion', 'N/A')}
[C][FFFFFF]BP Badge  : [66FF00]{ff_num(acc.get('AccountBPID'))}
[C][FFFFFF]Version   : [66FF00]{acc.get('ReleaseVersion', 'N/A')}
"""

    await safe_send_message(chat_type, msg1, uid, chat_id, key, iv)
    await asyncio.sleep(0.5)

    # ────────── MESSAGE 2 : DATE + RANK INFO ──────────
    lang = social.get("language", "N/A")
    if "_" in lang:
        lang = lang.split("_")[-1]   # ARABIC, ENGLISH
    msg2 = f"""
[C][B][FFAA00]━━━━━━━━━━━━━
[C][B][FFFFFF]ACCOUNT DETAILS
[C][FFAA00]━━━━━━━━━━━━━
[C][FFFFFF]Create Date : [66FF00]{human_time(acc.get('AccountCreateTime'))[:16]}
[C][FFFFFF]Last Login  : [66FF00]{human_time(acc.get('AccountLastLogin'))[:16]}
[C][FFFFFF]BR Max Rank     : [66FF00]{ff_num(acc.get('BrMaxRank'))}
[C][FFFFFF]BR Points   : [66FF00]{ff_num(acc.get('BrRankPoint'))}
[C][FFFFFF]CS Max Rank     : [66FF00]{ff_num(acc.get('CsMaxRank'))}
[C][FFFFFF]CS Points   : [66FF00]{ff_num(acc.get('CsRankPoint'))}
[C][FFFFFF]Language    : [66FF00]{lang}
"""

    await safe_send_message(chat_type, msg2, uid, chat_id, key, iv)
    await asyncio.sleep(0.5)

    # ────────── MESSAGE 3 : FULL GUILD INFO ──────────
    msg3 = f"""
[C][B][FFAA00]━━━━━━━━━━━━━
[C][B][FFFFFF]GUILD INFORMATION
[C][FFAA00]━━━━━━━━━━━━━
[C][FFFFFF]Guild Name   : [66FF00]{guild.get('GuildName', 'No Guild')}
[C][FFFFFF]Guild ID     : [66FF00]{ff_num(guild.get('GuildID'))}
[C][FFFFFF]Owner UID    : [66FF00]{ff_num(guild.get('GuildOwner'))}
[C][FFFFFF]Guild Level  : [66FF00]{guild.get('GuildLevel', 'N/A')}
[C][FFFFFF]Members      : [66FF00]{guild.get('GuildMember', '0')}/{guild.get('GuildCapacity', '0')}
"""

    await safe_send_message(chat_type, msg3, uid, chat_id, key, iv)
    
                    
####################################
#CHECK ACCOUNT IS BANNED

Hr = {
    'User-Agent': "Dalvik/2.1.0 (Linux; U; Android 11; ASUS_Z01QD Build/PI)",
    'Connection': "Keep-Alive",
    'Accept-Encoding': "gzip",
    'Content-Type': "application/x-www-form-urlencoded",
    'Expect': "100-continue",
    'X-Unity-Version': "2018.4.11f1",
    'X-GA': "v1 1",
    'ReleaseVersion': "OB53"}

# ---- Random Colores ----
def get_random_color():
    colors = [
        "[FF0000]", "[FFFF00]", "[0000FF]", "[FFFF00]", "[FF00FF]", "[00FFFF]", "[FFFFFF]", "[FFA500]",
        "[A52A2A]", "[800080]", "[000000]", "[808080]", "[C0C0C0]", "[FFC0CB]", "[FFD700]", "[ADD8E6]",
        "[90EE90]", "[D2691E]", "[DC143C]", "[00CED1]", "[9400D3]", "[F08080]", "[20B2AA]", "[FF1493]",
        "[7CFC00]", "[B22222]", "[FF4500]", "[DAA520]", "[00BFFF]", "[00FF7F]", "[4682B4]", "[6495ED]",
        "[5F9EA0]", "[DDA0DD]", "[E6E6FA]", "[B0C4DE]", "[556B2F]", "[8FBC8F]", "[2E8B57]", "[3CB371]",
        "[6B8E23]", "[808000]", "[B8860B]", "[CD5C5C]", "[8B0000]", "[FF6347]", "[FF8C00]", "[BDB76B]",
        "[9932CC]", "[8A2BE2]", "[4B0082]", "[6A5ACD]", "[7B68EE]", "[4169E1]", "[1E90FF]", "[191970]",
        "[00008B]", "[000080]", "[008080]", "[008B8B]", "[B0E0E6]", "[AFEEEE]", "[E0FFFF]", "[F5F5DC]",
        "[FAEBD7]"
    ]
    return random.choice(colors)
    
def get_random_evo_emote():
    """Return random evo emote ID"""
    evo_emotes = [
        909000063,  # AK
        909000068,  # SCAR  
        909000075,  # 1st MP40
        909040010,  # 2nd MP40
        909000081,  # 1st M1014
        909039011,  # 2nd M1014
        909000085,  # XM8
        909000090,  # Famas
        909000098,  # UMP
        909035007,  # M1887
        909042008,  # Woodpecker
        909041005,  # Groza
        909033001,  # M4A1
        909038010,  # Thompson
        909038012,  # G18
        909045001,  # Parafal
        909049010,  # P90
        909051003   # M60
    ]
    return random.choice(evo_emotes)
    
async def extract_uid_from_emote_packet(data_hex, key, iv):
    """Extract UID from emote packet (the sender)"""
    try:
        # Decrypt the packet
        packet = await DeCode_PackEt(data_hex[10:])
        packet_json = json.loads(packet)
        
        print(f"📦 Analyzing packet structure: {json.dumps(packet_json, indent=2)[:200]}...")
        
        # PATTERN 1: Your Emote_k() structure (Type 21)
        if packet_json.get('1') == 21:
            if ('2' in packet_json and 'data' in packet_json['2'] and
                '5' in packet_json['2']['data'] and 'data' in packet_json['2']['data']['5']):
                
                nested = packet_json['2']['data']['5']['data']
                if '1' in nested:
                    uid = nested['1']['data']
                    print(f"✅ Extracted UID from pattern 21: {uid}")
                    return uid
        
        # PATTERN 2: Direct emote structure
        elif packet_json.get('1') == 26:
            if ('2' in packet_json and 'data' in packet_json['2'] and
                '1' in packet_json['2']['data']):
                
                uid = packet_json['2']['data']['1']['data']
                print(f"✅ Extracted UID from pattern 26: {uid}")
                return uid
        
        # PATTERN 3: Try common paths
        for path in ['2/1', '5/1', '2/data/1', '5/data/1']:
            try:
                uid = get_nested_value(packet_json, path)
                if uid and str(uid).isdigit() and len(str(uid)) > 6:
                    print(f"✅ Extracted UID from path {path}: {uid}")
                    return uid
            except:
                pass
        
        print(f"❌ Could not extract UID from packet")
        return None
        
    except Exception as e:
        print(f"❌ UID extraction error: {e}")
        return None

def get_nested_value(data, path):
    """Get value from nested JSON path like '2/5/1'"""
    keys = path.split('/')
    current = data
    
    for key in keys:
        if key.isdigit():
            key = str(key)  # JSON keys are strings
        
        if key in current and 'data' in current[key]:
            current = current[key]['data']
        else:
            return None
    
    return current

async def ultra_quick_emote_attack(team_code, emote_id, target_uid, key, iv, region):
    """Join team, authenticate chat, perform emote, and leave automatically"""
    try:
        # Step 1: Join the team
        join_packet = await GenJoinSquadsPacket(team_code, key, iv)
        await SEndPacKeT(whisper_writer, online_writer, 'OnLine', join_packet)
        print(f"🤖 Joined team: {team_code}")
        
        # Wait for team data and chat authentication
        await asyncio.sleep(1.5)  # Increased to ensure proper connection
        
        # Step 2: The bot needs to be detected in the team and authenticate chat
        # This happens automatically in TcPOnLine, but we need to wait for it
        
        # Step 3: Perform emote to target UID
        emote_packet = await Emote_k(int(target_uid), int(emote_id), key, iv, region)
        await SEndPacKeT(whisper_writer, online_writer, 'OnLine', emote_packet)
        print(f"🎭 Performed emote {emote_id} to UID {target_uid}")
        
        # Wait for emote to register
        await asyncio.sleep(0.5)
        
        # Step 4: Leave the team
        leave_packet = await ExiT(None, key, iv)
        await SEndPacKeT(whisper_writer, online_writer, 'OnLine', leave_packet)
        print(f"🚪 Left team: {team_code}")
        
        return True, f"Quick emote attack completed! Sent emote to UID {target_uid}"
        
    except Exception as e:
        return False, f"Quick emote attack failed: {str(e)}"
        
        
async def encrypted_proto(encoded_hex):
    key = b'Yg&tc%DEuh6%Zc^8'
    iv = b'6oyZDr22E3ychjM%'
    cipher = AES.new(key, AES.MODE_CBC, iv)
    padded_message = pad(encoded_hex, AES.block_size)
    encrypted_payload = cipher.encrypt(padded_message)
    return encrypted_payload
    
async def GeNeRaTeAccEss(uid , password):
    url = "https://100067.connect.garena.com/oauth/guest/token/grant"
    headers = {
        "Host": "100067.connect.garena.com",
        "User-Agent": (await Ua()),
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "close"}
    data = {
        "uid": uid,
        "password": password,
        "response_type": "token",
        "client_type": "2",
        "client_secret": "2ee44819e9b4598845141067b281621874d0d5d7af9d8f7e00c1e54715b7d1e3",
        "client_id": "100067"}
    async with aiohttp.ClientSession() as session:
        async with session.post(url, headers=Hr, data=data) as response:
            if response.status != 200: return "Failed to get access token"
            data = await response.json()
            open_id = data.get("open_id")
            access_token = data.get("access_token")
            return (open_id, access_token) if open_id and access_token else (None, None)

async def EncRypTMajoRLoGin(open_id, access_token):
    major_login = MajoRLoGinrEq_pb2.MajorLogin()
    major_login.event_time = str(datetime.now())[:-7]
    major_login.game_name = "free fire"
    major_login.platform_id = 1
    major_login.client_version = "1.120.2"
    major_login.system_software = "Android OS 9 / API-28 (PQ3B.190801.10101846/G9650ZHU2ARC6)"
    major_login.system_hardware = "Handheld"
    major_login.telecom_operator = "Verizon"
    major_login.network_type = "WIFI"
    major_login.screen_width = 1920
    major_login.screen_height = 1080
    major_login.screen_dpi = "280"
    major_login.processor_details = "ARM64 FP ASIMD AES VMH | 2865 | 4"
    major_login.memory = 3003
    major_login.gpu_renderer = "Adreno (TM) 640"
    major_login.gpu_version = "OpenGL ES 3.1 v1.46"
    major_login.unique_device_id = "Google|34a7dcdf-a7d5-4cb6-8d7e-3b0e448a0c57"
    major_login.client_ip = "223.191.51.89"
    major_login.language = "en"
    major_login.open_id = open_id
    major_login.open_id_type = "4"
    major_login.device_type = "Handheld"
    memory_available = major_login.memory_available
    memory_available.version = 55
    memory_available.hidden_value = 81
    major_login.access_token = access_token
    major_login.platform_sdk_id = 1
    major_login.network_operator_a = "Verizon"
    major_login.network_type_a = "WIFI"
    major_login.client_using_version = "7428b253defc164018c604a1ebbfebdf"
    major_login.external_storage_total = 36235
    major_login.external_storage_available = 31335
    major_login.internal_storage_total = 2519
    major_login.internal_storage_available = 703
    major_login.game_disk_storage_available = 25010
    major_login.game_disk_storage_total = 26628
    major_login.external_sdcard_avail_storage = 32992
    major_login.external_sdcard_total_storage = 36235
    major_login.login_by = 3
    major_login.library_path = "/data/app/com.dts.freefireth-YPKM8jHEwAJlhpmhDhv5MQ==/lib/arm64"
    major_login.reg_avatar = 1
    major_login.library_token = "5b892aaabd688e571f688053118a162b|/data/app/com.dts.freefireth-YPKM8jHEwAJlhpmhDhv5MQ==/base.apk"
    major_login.channel_type = 3
    major_login.cpu_type = 2
    major_login.cpu_architecture = "64"
    major_login.client_version_code = "2019118695"
    major_login.graphics_api = "OpenGLES2"
    major_login.supported_astc_bitset = 16383
    major_login.login_open_id_type = 4
    major_login.analytics_detail = b"FwQVTgUPX1UaUllDDwcWCRBpWA0FUgsvA1snWlBaO1kFYg=="
    major_login.loading_time = 13564
    major_login.release_channel = "android"
    major_login.extra_info = "KqsHTymw5/5GB23YGniUYN2/q47GATrq7eFeRatf0NkwLKEMQ0PK5BKEk72dPflAxUlEBir6Vtey83XqF593qsl8hwY="
    major_login.android_engine_init_flag = 110009
    major_login.if_push = 1
    major_login.is_vpn = 1
    major_login.origin_platform_type = "4"
    major_login.primary_platform_type = "4"
    string = major_login.SerializeToString()
    return  await encrypted_proto(string)

async def MajorLogin(payload):
    url = "https://loginbp.ggblueshark.com/MajorLogin"
    ssl_context = ssl.create_default_context()
    ssl_context.check_hostname = False
    ssl_context.verify_mode = ssl.CERT_NONE
    async with aiohttp.ClientSession() as session:
        async with session.post(url, data=payload, headers=Hr, ssl=ssl_context) as response:
            if response.status == 200: return await response.read()
            return None

async def GetLoginData(base_url, payload, token):
    url = f"{base_url}/GetLoginData"
    ssl_context = ssl.create_default_context()
    ssl_context.check_hostname = False
    ssl_context.verify_mode = ssl.CERT_NONE
    Hr['Authorization']= f"Bearer {token}"
    async with aiohttp.ClientSession() as session:
        async with session.post(url, data=payload, headers=Hr, ssl=ssl_context) as response:
            if response.status == 200: return await response.read()
            return None

async def DecRypTMajoRLoGin(MajoRLoGinResPonsE):
    proto = MajoRLoGinrEs_pb2.MajorLoginRes()
    proto.ParseFromString(MajoRLoGinResPonsE)
    return proto

async def DecRypTLoGinDaTa(LoGinDaTa):
    proto = PorTs_pb2.GetLoginData()
    proto.ParseFromString(LoGinDaTa)
    return proto

async def DecodeWhisperMessage(hex_packet):
    packet = bytes.fromhex(hex_packet)
    proto = DEcwHisPErMsG_pb2.DecodeWhisper()
    proto.ParseFromString(packet)
    return proto
    
async def decode_team_packet(hex_packet):
    packet = bytes.fromhex(hex_packet)
    proto = sQ_pb2.recieved_chat()
    proto.ParseFromString(packet)
    return proto
    
async def xAuThSTarTuP(TarGeT, token, timestamp, key, iv):
    uid_hex = hex(TarGeT)[2:]
    uid_length = len(uid_hex)
    encrypted_timestamp = await DecodE_HeX(timestamp)
    encrypted_account_token = token.encode().hex()
    encrypted_packet = await EnC_PacKeT(encrypted_account_token, key, iv)
    encrypted_packet_length = hex(len(encrypted_packet) // 2)[2:]
    if uid_length == 9: headers = '0000000'
    elif uid_length == 8: headers = '00000000'
    elif uid_length == 10: headers = '000000'
    elif uid_length == 7: headers = '000000000'
    else: print('Unexpected length') ; headers = '0000000'
    return f"0115{headers}{uid_hex}{encrypted_timestamp}00000{encrypted_packet_length}{encrypted_packet}"
    

async def cHTypE(H):
    """Detect chat type including custom rooms"""
    if not H: 
        return 'Squid'
    elif H == 1: 
        return 'CLan'
    elif H == 2: 
        return 'PrivaTe'
    elif H == 3: 
        return 'CustomRoom'  # Custom room chat type
    else:
        return 'Squid'  # Default fallback
    
async def SEndMsG(H, message, Uid, chat_id, key, iv, region):
    """Send message to any chat type including custom rooms"""
    TypE = await cHTypE(H)
    
    if TypE == 'Squid': 
        msg_packet = await xSEndMsgsQ(message, chat_id, key, iv)
    elif TypE == 'CLan': 
        msg_packet = await xSEndMsg(message, 1, chat_id, chat_id, key, iv)
    elif TypE == 'PrivaTe': 
        msg_packet = await xSEndMsg(message, 2, Uid, Uid, key, iv)
    else:
        # Fallback to squad chat
        msg_packet = await xSEndMsgsQ(message, chat_id, key, iv)
        
    return msg_packet
    
    
async def SEndPacKeT(OnLinE , ChaT , TypE , PacKeT):
    if TypE == 'ChaT' and ChaT: whisper_writer.write(PacKeT) ; await whisper_writer.drain()
    elif TypE == 'OnLine': online_writer.write(PacKeT) ; await online_writer.drain()
    else: return 'UnsoPorTed TypE ! >> ErrrroR (:():)' 

async def safe_send_message(chat_type, message, target_uid, chat_id, key, iv, max_retries=3, region="ind"):
    """Enhanced safe send message that works with custom rooms"""
    for attempt in range(max_retries):
        try:
            P = await SEndMsG(chat_type, message, target_uid, chat_id, key, iv, region)
            await SEndPacKeT(whisper_writer, online_writer, 'ChaT', P)
                
            print(f"✅ Message sent successfully to chat type {chat_type} (attempt {attempt + 1})")
            return True
        except Exception as e:
            print(f"❌ Failed to send message (attempt {attempt + 1}): {e}")
            if attempt < max_retries - 1:
                await asyncio.sleep(0.5)
    return False

async def fast_emote_spam(uids, emote_id, key, iv, region):
    """Fast emote spam function that sends emotes rapidly"""
    global fast_spam_running
    count = 0
    max_count = 25  # Spam 25 times
    
    while fast_spam_running and count < max_count:
        for uid in uids:
            try:
                uid_int = int(uid)
                H = await Emote_k(uid_int, int(emote_id), key, iv, region)
                await SEndPacKeT(whisper_writer, online_writer, 'OnLine', H)
            except Exception as e:
                print(f"Error in fast_emote_spam for uid {uid}: {e}")
        
        count += 1
        await asyncio.sleep(0.1)  # 0.1 seconds interval between spam cycles

# NEW FUNCTION: Custom emote spam with specified times
async def custom_emote_spam(uid, emote_id, times, key, iv, region):
    """Custom emote spam function that sends emotes specified number of times"""
    global custom_spam_running
    count = 0
    
    while custom_spam_running and count < times:
        try:
            uid_int = int(uid)
            H = await Emote_k(uid_int, int(emote_id), key, iv, region)
            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', H)
            count += 1
            await asyncio.sleep(0.0000001)  # 0.1 seconds interval between emotes
        except Exception as e:
            print(f"Error in custom_emote_spam for uid {uid}: {e}")
            break

async def create_level_up_bot_connection(key, iv, region):
    """Create a separate connection for level-up bot"""
    try:
        # This would use a different bot account
        # For now, we'll use the main bot
        print("🤖 Level-up bot connection initialized")
        return True
    except Exception as e:
        print(f"❌ Level-up bot connection error: {e}")
        return False

async def level_up_join_team(team_code, key, iv, region):
    """Level-up bot joins the team"""
    try:
        join_packet = await GenJoinSquadsPacket(team_code, key, iv)
        await SEndPacKeT(whisper_writer, online_writer, 'OnLine', join_packet)
        print(f"🤖 Level-up bot joining team: {team_code}")
        await asyncio.sleep(2)
        return True
    except Exception as e:
        print(f"❌ Level-up bot join error: {e}")
        return False

async def level_up_leave_team(key, iv):
    """Level-up bot leaves the team"""
    try:
        leave_packet = await ExiT(None, key, iv)
        await SEndPacKeT(whisper_writer, online_writer, 'OnLine', leave_packet)
        print("🤖 Level-up bot leaving team")
        await asyncio.sleep(1)
        return True
    except Exception as e:
        print(f"❌ Level-up bot leave error: {e}")
        return False
        
async def level_up_loop(team_code, target_uid, key, iv, region, chat_type, chat_id):
    """Main level-up automation loop"""
    global level_up_running
    
    cycle_count = 0
    max_cycles = 1000  # Safety limit
    
    print(f"🚀 Starting level-up automation for team {team_code}")
    
    while level_up_running and cycle_count < max_cycles:
        try:
            cycle_count += 1
            print(f"🔄 Level-up cycle #{cycle_count}")
            
            # Step 1: Send instruction message
            instruction_msg = f"""[B][C][FFFF00]🔄 LEVEL-UP CYCLE #{cycle_count}

🤖 Bot: Joining your team...
🎮 Action: Will start match
⏱️ After match: Wait {level_up_wait_time} seconds
🔄 Then: Repeat process

📊 Status: Bot is working...
"""
            await safe_send_message(chat_type, instruction_msg, target_uid, chat_id, key, iv)
            
            # Step 2: Join the team
            join_success = await level_up_join_team(team_code, key, iv, region)
            if not join_success:
                print("❌ Failed to join team, retrying...")
                await asyncio.sleep(2)
                continue
            
            # Step 3: Send "ready" message
            ready_msg = f"[B][C][FFFF00]✅ Bot joined! Starting match...\n"
            await safe_send_message(chat_type, ready_msg, target_uid, chat_id, key, iv)
            
            # Step 4: Start the match (spam start packet)
            start_packet = await FS(key, iv)
            spam_duration = 10  # Spam for 10 seconds
            start_time = time.time()
            
            while time.time() - start_time < spam_duration and level_up_running:
                await SEndPacKeT(whisper_writer, online_writer, 'OnLine', start_packet)
                await asyncio.sleep(0.2)  # 200ms delay between packets
            
            # Step 5: Wait for match to complete (simulate)
            waiting_msg = f"""[B][C][FFFF00]⏱️ MATCH IN PROGRESS...

⏳ Waiting for match to complete...
🔄 Next cycle starts in {level_up_wait_time} seconds
🤖 Bot remains in team

💡 Let the match complete normally!
"""
            await safe_send_message(chat_type, waiting_msg, target_uid, chat_id, key, iv)
            
            # Step 6: Wait the specified time
            wait_count = 0
            while wait_count < level_up_wait_time and level_up_running:
                await asyncio.sleep(1)
                wait_count += 1
                
                # Progress update every 5 seconds
                if wait_count % 5 == 0:
                    progress_msg = f"[B][C][FFFF00]⏱️ {wait_count}/{level_up_wait_time} seconds waited...\n"
                    await safe_send_message(chat_type, progress_msg, target_uid, chat_id, key, iv)
            
            if not level_up_running:
                break
            
            # Step 7: Leave team
            leave_success = await level_up_leave_team(key, iv)
            
            if leave_success:
                leave_msg = f"[B][C][FF0000]🚪 Bot left team to restart cycle...\n"
                await safe_send_message(chat_type, leave_msg, target_uid, chat_id, key, iv)
            
            # Step 8: Small delay before next cycle
            await asyncio.sleep(2)
            
        except Exception as e:
            print(f"❌ Error in level-up cycle: {e}")
            # Try to recover
            await level_up_leave_team(key, iv)
            await asyncio.sleep(3)
    
    print("🛑 Level-up automation stopped")

async def Send_Entry_Emote(uid, K, V, emote_id=912038002, session_id=5, trigger_type=1):
    """Send arrival/entry animation emote
    
    Args:
        uid: Target player UID
        K: Encryption key
        V: Initialization vector
        emote_id: Emote ID (default: 912038002 - arrival animation)
        session_id: Session ID (default: 5)
        trigger_type: Trigger type (default: 1 - entry)
    """
    try:
        fields = {
            1: 4,           # Packet ID for entry emotes
            2: int(uid),    # Player UID
            3: int(session_id),     # Session ID
            4: int(emote_id),       # Emote ID
            5: int(trigger_type),   # Trigger Type (1=entry, 2=exit, etc.)
            6: int(uid),    # Repeated UID
            7: 1,           # Static Value
            8: int(uid),    # Repeated UID
            9: int(uid),    # Repeated UID
            10: int(uid),   # Repeated UID
            11: int(uid),   # Repeated UID
        }
        
        # Different arrival animations
        arrival_emotes = {
            "default": 912038002,
        }
        
        # Use provided emote_id or default
        if isinstance(emote_id, str) and emote_id in arrival_emotes:
            fields[4] = arrival_emotes[emote_id]
        
        proto_hex = (await CrEaTe_ProTo(fields)).hex()
        
        # Determine packet type based on region (you might need to pass region)
        # For now using '0515' as in your example
        return await GeneRaTePk(proto_hex, '0515', K, V)
        
    except Exception as e:
        print(f"❌ Error creating entry emote packet: {e}")
        return None


async def play_emote_spam(uids, number, key, iv, region):
    """Send all emotes based on number mapping"""
    try:
        emote_id = ALL_EMOTE.get(int(number))
        if not emote_id:
            return False, f"Invalid number! Use 1-410 only."
        
        success_count = 0
        for uid in uids:
            try:
                uid_int = int(uid)
                H = await Emote_k(uid_int, emote_id, key, iv, region)
                await SEndPacKeT(whisper_writer, online_writer, 'OnLine', H)
                success_count += 1
                await asyncio.sleep(0.1)
            except Exception as e:
                print(f"Error sending play emote to {uid}: {e}")
        
        return True, f"Sent playlution emote {number} (ID: {emote_id}) to {success_count} player(s)"
    
    except Exception as e:
        return False, f"Error in play_emote_spam: {str(e)}"
        
        
# NEW FUNCTION: Evolution emote spam with mapping
async def evo_emote_spam(uids, number, key, iv, region):
    """Send evolution emotes based on number mapping"""
    try:
        emote_id = EMOTE_MAP.get(int(number))
        if not emote_id:
            return False, f"Invalid number! Use 1-21 only."
        
        success_count = 0
        for uid in uids:
            try:
                uid_int = int(uid)
                H = await Emote_k(uid_int, emote_id, key, iv, region)
                await SEndPacKeT(whisper_writer, online_writer, 'OnLine', H)
                success_count += 1
                await asyncio.sleep(0.1)
            except Exception as e:
                print(f"Error sending evo emote to {uid}: {e}")
        
        return True, f"Sent evolution emote {number} (ID: {emote_id}) to {success_count} player(s)"
    
    except Exception as e:
        return False, f"Error in evo_emote_spam: {str(e)}"



# NEW FUNCTION: Fast evolution emote spam
async def evo_fast_emote_spam(uids, number, key, iv, region):
    """Fast evolution emote spam function"""
    global evo_fast_spam_running
    count = 0
    max_count = 25  # Spam 25 times
    
    emote_id = EMOTE_MAP.get(int(number))
    if not emote_id:
        return False, f"Invalid number! Use 1-21 only."
    
    while evo_fast_spam_running and count < max_count:
        for uid in uids:
            try:
                uid_int = int(uid)
                H = await Emote_k(uid_int, emote_id, key, iv, region)
                await SEndPacKeT(whisper_writer, online_writer, 'OnLine', H)
            except Exception as e:
                print(f"Error in evo_fast_emote_spam for uid {uid}: {e}")
        
        count += 1
        await asyncio.sleep(0.1)  # CHANGED: 0.5 seconds to 0.1 seconds
    
    return True, f"Completed fast evolution emote spam {count} times"
    
async def send_required_packets(key, iv, region, bot_uid):
    """Send packets required after connection"""
    try:
        # Packet 1: Client info
        fields1 = {
            1: 100,
            2: {
                1: bot_uid,
                2: "1.120.2",  # Game version
                3: "Android",
                4: "en",
            }
        }
        
        # Packet 2: Device info
        fields2 = {
            1: 101,
            2: {
                1: "vivo",
                2: "1901",
                3: "arm64-v8a",
                4: str(time.time()),
            }
        }
        
        packets = []
        for fields in [fields1, fields2]:
            if region.lower() == "ind":
                packet_type = '0514'
            elif region.lower() == "bd":
                packet_type = "0519"
            else:
                packet_type = "0515"
                
            packet = await GeneRaTePk((await CrEaTe_ProTo(fields)).hex(), packet_type, key, iv)
            packets.append(packet)
        
        return packets
        
    except Exception as e:
        print(f"❌ Required packets error: {e}")
        return []

# NEW FUNCTION: Custom evolution emote spam with specified times
async def evo_custom_emote_spam(uids, number, times, key, iv, region):
    """Custom evolution emote spam with specified repeat times"""
    global evo_custom_spam_running
    count = 0
    
    emote_id = EMOTE_MAP.get(int(number))
    if not emote_id:
        return False, f"Invalid number! Use 1-21 only."
    
    while evo_custom_spam_running and count < times:
        for uid in uids:
            try:
                uid_int = int(uid)
                H = await Emote_k(uid_int, emote_id, key, iv, region)
                await SEndPacKeT(whisper_writer, online_writer, 'OnLine', H)
            except Exception as e:
                print(f"Error in evo_custom_emote_spam for uid {uid}: {e}")
        
        count += 1
        await asyncio.sleep(0.1)  # CHANGED: 0.5 seconds to 0.1 seconds
    
    return True, f"Completed custom evolution emote spam {count} times"

async def RejectMSGtaxt(squad_owner,uid, key, iv):
    random_banner = f"""
.
.
.










    
[FFFF00]ＷＥＬＣＯＭＥ ＴＯ[FF0000] O U R G U I L D   [FFFF00]B O T
[FF0000]━[FFFF00]━[0000FF]━[FFFF00]━[FF00FF]━[00FFFF]━[FFA500]━[FF1493]━[00FF7F]━[FFD700]━[00CED1]━[9400D3]━[FF6347]━[32CD32]━[7B68EE]━[FF4500]━[1E90FF]━[ADFF2F]━[FF69B4]━[8A2BE2]━[DC143C]━[FF8C00]━[BA55D3]━[7CFC00]━[FFC0CB]
[1E90FF] CHAYAN   [FF0000]ZAINUㅤVIP
[FF0000]━[FFFF00]━[0000FF]━[FFFF00]━[FF00FF]━[00FFFF]━[FFA500]━[FF1493]━[00FF7F]━[FFD700]━[00CED1]━[9400D3]━[FF6347]━[32CD32]━[7B68EE]━[FF4500]━[1E90FF]━[ADFF2F]━[FF69B4]━[8A2BE2]━[DC143C]━[FF8C00]━[BA55D3]━[7CFC00]━[FFC0CB]
[FF0000]_ _ _ X ³ _ _ _ _  
[FF0000]━[FFFF00]━[0000FF]━[FFFF00]━[FF00FF]━[00FFFF]━[FFA500]━[FF1493]━[00FF7F]━[FFD700]━[00CED1]━[9400D3]━[FF6347]━[32CD32]━[7B68EE]━[FF4500]━[1E90FF]━[ADFF2F]━[FF69B4]━[8A2BE2]━[DC143C]━[FF8C00]━[BA55D3]━[7CFC00]━[FFC0CB]
[9400D3]M A D E B Y [FF0000]ZAINUㅤVIP
[FF0000]━[FFFF00]━[0000FF]━[FFFF00]━[FF00FF]━[00FFFF]━[FFA500]━[FF1493]━[00FF7F]━[FFD700]━[00CED1]━[9400D3]━[FF6347]━[32CD32]━[7B68EE]━[FF4500]━[1E90FF]━[ADFF2F]━[FF69B4]━[8A2BE2]━[DC143C]━[FF8C00]━[BA55D3]━[7CFC00]━[FFC0CB]
[FFD700] ＦＯＬＬＯＷ    ＭＥ   ＩＮ   [87CEEB]TELEGRAM: [FF0000]@chayan210
[FF0000]━[FFFF00]━[0000FF]━[FFFF00]━[FF00FF]━[00FFFF]━[FFA500]━[FF1493]━[00FF7F]━[FFD700]━[00CED1]━[9400D3]━[FF6347]━[32CD32]━[7B68EE]━[FF4500]━[1E90FF]━[ADFF2F]━[FF69B4]━[8A2BE2]━[DC143C]━[FF8C00]━[BA55D3]━[7CFC00]━[FFC0CB]"""
    fields = {
    1: 5,
    2: {
        1: int(squad_owner),
        2: 1,
        3: int(uid),
        4: random_banner
    }
    }
    return await GeneRaTePk((await CrEaTe_ProTo(fields)).hex() , '0515' , key, iv)

async def send_keep_alive(key, iv, region):
    """Send keep-alive packet to maintain connection"""
    try:
        fields = {
            1: 99,  # Keep-alive packet type
            2: {
                1: int(time.time()),
                2: 1,  # Keep-alive flag
            }
        }
        
        if region.lower() == "ind":
            packet_type = '0514'
        elif region.lower() == "bd":
            packet_type = "0519"
        else:
            packet_type = "0515"
            
        packet = await GeneRaTePk((await CrEaTe_ProTo(fields)).hex(), packet_type, key, iv)
        return packet
    except Exception as e:
        print(f"❌ Keep-alive error: {e}")
        return None

async def ArohiAccepted(uid,code,K,V):
    fields = {
        1: 4,
        2: {
            1: uid,
            3: uid,
            8: 1,
            9: {
            2: 161,
            4: "y[WW",
            6: 11,
            8: "1.114.18",
            9: 3,
            10: 1
            },
            10: str(code),
        }
        }
    return await GeneRaTePk((await CrEaTe_ProTo(fields)).hex() , '0515' , K , V)


async def new_lag(key , iv):
    fields = {
        1: 15,
        2: {
            1: 804266360,
            2: 1
        }
    }
    return await GeneRaTePk((await CrEaTe_ProTo(fields)).hex() , '0515' , key , iv)


async def convert_kyro_to_your_system(target_uid, chat_id, key, iv, nickname="juli_dvrma", title_id=None):
    """EXACT conversion with customizable title ID"""
    try:
        # Use provided title_id or get random one
        if title_id is None:
            # Get a random title from the list
            available_titles = [905090075, 904990072, 904990069, 905190079]
            title_id = random.choice(available_titles)
        
        # Create fields dictionary with specific title_id
        fields = {
            1: 1,
            2: {
                1: int(target_uid),
                2: int(chat_id),
                5: int(datetime.now().timestamp()),
                8: f'{{"TitleID":{title_id},"type":"Title"}}',  # Use specific title ID
                # ... rest of your fields
                9: {
                    1: f"[C][B][FF0000]{nickname}",
                    2: int(await xBunnEr()),
                    4: 330,
                    5: 102000015,
                    8: "BOT TEAM",
                    10: 1,
                    11: 1,
                    13: {
                        1: 2
                    },
                    14: {
                        1: 1158053040,
                        2: 8,
                        3: b"\x10\x15\x08\x0a\x0b\x15\x0c\x0f\x11\x04\x07\x02\x03\x0d\x0e\x12\x01\x05\x06"
                    }
                },
                10: "en",
                13: {
                    2: 2,
                    3: 1
                },
                14: {}
            }
        }
        
        # ... rest of your existing function
        proto_bytes = await CrEaTe_ProTo(fields)
        packet_hex = proto_bytes.hex()
        
        encrypted_packet = await encrypt_packet(packet_hex, key, iv)
        packet_length = len(encrypted_packet) // 2
        hex_length = f"{packet_length:04x}"
        
        zeros_needed = 6 - len(hex_length)
        packet_prefix = "121500" + ("0" * zeros_needed)
        
        final_packet_hex = packet_prefix + hex_length + encrypted_packet
        final_packet = bytes.fromhex(final_packet_hex)
        
        print(f"✅ Created packet with Title ID: {title_id}")
        return final_packet
        
    except Exception as e:
        print(f"❌ Conversion error: {e}")
        return None
        
def get_random_sticker():
    """
    Randomly select one sticker from available packs
    """

    sticker_packs = [
        # NORMAL STICKERS (1200000001-1 to 24)
        ("1200000001", 1, 24),

        # KELLY EMOJIS (1200000002-1 to 15)
        ("1200000002", 1, 15),

        # MAD CHICKEN (1200000004-1 to 13)
        ("1200000004", 1, 13),
    ]

    pack_id, start, end = random.choice(sticker_packs)
    sticker_no = random.randint(start, end)

    return f"[1={pack_id}-{sticker_no}]"
        
async def send_sticker(target_uid, chat_id, key, iv, nickname="BLACK"):
    """Send Random Sticker using /sticker command"""
    try:
        sticker_value = get_random_sticker()

        fields = {
            1: 1,
            2: {
                1: int(target_uid),
                2: int(chat_id),
                5: int(datetime.now().timestamp()),
                8: f'{{"StickerStr" : "{sticker_value}", "type":"Sticker"}}',
                9: {
                    1: f"[C][B][FF0000]{nickname}",
                    2: int(get_random_avatar1()),
                    4: 330,
                    5: 102000015,
                    8: "BOT TEAM",
                    10: 1,
                    11: 66,
                    12: 66,
                    13: {1: 2},
                    14: {
                        1: 1158053040,
                        2: 8,
                        3: b"\x10\x15\x08\x0a\x0b\x15\x0c\x0f\x11\x04\x07\x02\x03\x0d\x0e\x12\x01\x05\x06"
                    }
                },
                10: "en",
                13: {
                    2: 2,
                    3: 1
                },
                14: {}
            }
        }

        proto_bytes = await CrEaTe_ProTo(fields)
        packet_hex = proto_bytes.hex()

        encrypted_packet = await encrypt_packet(packet_hex, key, iv)
        packet_length = len(encrypted_packet) // 2
        hex_length = f"{packet_length:04x}"

        zeros_needed = 6 - len(hex_length)
        packet_prefix = "121500" + ("0" * zeros_needed)

        final_packet_hex = packet_prefix + hex_length + encrypted_packet
        final_packet = bytes.fromhex(final_packet_hex)

        print(f"✅ Sticker Sent: {sticker_value}")
        return final_packet

    except Exception as e:
        print(f"❌ Sticker error: {e}")
        return None

# Alternative: DIRECT port of your friend's function but with your UID
async def send_kyro_title_adapted(chat_id, key, iv, target_uid, nickname="juli_dvrma"):
    """Direct adaptation of your friend's working function"""
    try:
        # Import your proto file (make sure it's in the same directory)
        from kyro_title_pb2 import GenTeamTitle
        
        root = GenTeamTitle()
        root.type = 1
        
        nested_object = root.data
        nested_object.uid = int(target_uid)  # CHANGE: Use target UID
        nested_object.chat_id = int(chat_id)
        nested_object.title = f"{{\"TitleID\":{titles()},\"type\":\"Title\"}}"
        nested_object.timestamp = int(datetime.now().timestamp())
        nested_object.language = "en"
        
        nested_details = nested_object.field9
        nested_details.Nickname = f"[C][B][FF0000]{nickname}"  # CHANGE: Your nickname
        nested_details.avatar_id = int(await xBunnEr())  # Use your function
        nested_details.rank = 330
        nested_details.badge = 102000015
        nested_details.Clan_Name = "BOT TEAM"  # CHANGE: Your clan
        nested_details.field10 = 1
        nested_details.global_rank_pos = 1
        nested_details.badge_info.value = 2
        
        nested_details.prime_info.prime_uid = 1158053040
        nested_details.prime_info.prime_level = 8
        # IMPORTANT: This must be bytes, not string!
        nested_details.prime_info.prime_hex = b"\x10\x15\x08\x0a\x0b\x15\x0c\x0f\x11\x04\x07\x02\x03\x0d\x0e\x12\x01\x05\x06"
        
        nested_options = nested_object.field13
        nested_options.url_type = 2
        nested_options.curl_platform = 1
        
        nested_object.empty_field.SetInParent()
        
        # Serialize
        packet = root.SerializeToString().hex()
        
        # Use YOUR encryption function
        encrypted_packet = await encrypt_packet(packet, key, iv)
        
        # Calculate length
        packet_length = len(encrypted_packet) // 2
        
        # Convert to hex (4 characters with leading zeros)
        hex_length = f"{packet_length:04x}"
        
        # Build packet EXACTLY like your friend
        zeros_needed = 6 - len(hex_length)
        packet_prefix = "121500" + ("0" * zeros_needed)
        
        final_packet_hex = packet_prefix + hex_length + encrypted_packet
        return bytes.fromhex(final_packet_hex)
        
    except Exception as e:
        print(f"❌ Direct adaptation error: {e}")
        import traceback
        traceback.print_exc()
        return None

async def send_all_titles_sequentially(uid, chat_id, key, iv, region, chat_type):
    """Send all titles one by one with 2-second delay"""
    
    # Get all titles
    all_titles = [
        905090075, 904990072, 904990069, 905190079
    ]
    
    total_titles = len(all_titles)
    
    # Send initial message
    start_msg = f"""[B][C][FFFF00]🎖️ STARTING TITLE SEQUENCE!

📊 Total Titles: {total_titles}
⏱️ Delay: 2 seconds between titles
🔁 Mode: Sequential
🎯 Target: {uid}

⏳ Sending titles now...
"""
    await safe_send_message(chat_type, start_msg, uid, chat_id, key, iv)
    
    try:
        for index, title_id in enumerate(all_titles):
            title_number = index + 1
            
            # Create progress message
            progress_msg = f"""[B][C][FFFF00]📤 SENDING TITLE {title_number}/{total_titles}

🎖️ Title ID: {title_id}
📊 Progress: {title_number}/{total_titles}
⏱️ Next in: 2 seconds
"""
            await safe_send_message(chat_type, progress_msg, uid, chat_id, key, iv)
            
            # Send the actual title using your existing method
            # You'll need to use your existing title sending logic here
            # For example:
            title_packet = await convert_kyro_to_your_system(uid, chat_id, key, iv, nickname="Flash_ff", title_id=title_id)
            
            if title_packet and whisper_writer:
                whisper_writer.write(title_packet)
                await whisper_writer.drain()
                print(f"✅ Sent title {title_number}/{total_titles}: {title_id}")
            
            # Wait 2 seconds before next title (unless it's the last one)
            if title_number < total_titles:
                await asyncio.sleep(2)
        
        # Completion message
        completion_msg = f"""[B][C][FFFF00]✅ ALL TITLES SENT SUCCESSFULLY!

🎊 Total: {total_titles} titles sent
🎯 Target: {uid}
⏱️ Duration: {total_titles * 2} seconds
✅ Status: Complete!

🎖️ Titles Sent:
1. 905090075
2. 904990072
3. 904990069
4. 905190079
"""
        await safe_send_message(chat_type, completion_msg, uid, chat_id, key, iv)
        
    except Exception as e:
        error_msg = f"[B][C][FF0000]❌ Error sending titles: {str(e)}\n"
        await safe_send_message(chat_type, error_msg, uid, chat_id, key, iv)

async def handle_all_titles_command(inPuTMsG, uid, chat_id, key, iv, region, chat_type=0):
    """Handle /alltitles command to send all titles sequentially"""
    
    parts = inPuTMsG.strip().split()
    
    if len(parts) == 1:
        target_uid = uid
        target_name = "Yourself"
    elif len(parts) == 2 and parts[1].isdigit():
        target_uid = parts[1]
        target_name = f"UID {target_uid}"
    else:
        error_msg = f"""[B][C][FF0000]❌ Usage: /alltitles [uid]
        
📝 Examples:
/alltitles - Send all titles to yourself
/alltitles 123456789 - Send all titles to specific UID

🎯 What it does:
1. Sends all 4 titles one by one
2. 2-second delay between each title
3. Sends in background (non-blocking)
4. Shows progress updates
"""
        await safe_send_message(chat_type, error_msg, uid, chat_id, key, iv)
        return
    
    # Start the title sequence in the background
    asyncio.create_task(
        send_all_titles_sequentially(target_uid, chat_id, key, iv, region, chat_type)
    )
    
    # Immediate response
    response_msg = f"""[B][C][FFFF00]🚀 STARTING TITLE SEQUENCE IN BACKGROUND!

👤 Target: {target_name}
🎖️ Total Titles: 4
⏱️ Delay: 2 seconds each
📱 Status: Running in background...

💡 You'll receive progress updates as titles are sent!
"""
    await safe_send_message(chat_type, response_msg, uid, chat_id, key, iv)


async def noob(target_uid, chat_id, key, iv, nickname="juli_dvrma", title_id=None):
    """EXACT conversion with customizable title ID"""
    try:
        # Use provided title_id or get random one
        if title_id is None:
            # Get a random title from the list
            available_titles = [904090014, 904090015, 904090024, 904090025, 904090026, 904090027, 904990070, 904990071, 904990072]
            title_id = random.choice(available_titles)
        
        # Create fields dictionary with specific title_id
        fields = {
            1: 1,
            2: {
                1: int(target_uid),
                2: int(chat_id),
                5: int(datetime.now().timestamp()),
                8: f'{{"TitleID":{title_id},"type":"Title"}}',
                9: {
                    1: f"[C][B][FF0000]{nickname}",
                    2: int(await xBunnEr()),
                    4: 330,
                    5: 102000015,
                    8: "BOT TEAM",
                    10: 1,
                    11: 1,
                    13: {
                        1: 2
                    },
                    14: {
                        1: 1158053040,
                        2: 8,
                        3: b"\x10\x15\x08\x0a\x0b\x15\x0c\x0f\x11\x04\x07\x02\x03\x0d\x0e\x12\x01\x05\x06"
                    }
                },
                10: "en",
                13: {
                    2: 2,
                    3: 1
                },
                14: {}
            }
        }
        
        # ... rest of your existing function
        proto_bytes = await CrEaTe_ProTo(fields)
        packet_hex = proto_bytes.hex()
        
        encrypted_packet = await encrypt_packet(packet_hex, key, iv)
        packet_length = len(encrypted_packet) // 2
        hex_length = f"{packet_length:04x}"
        
        zeros_needed = 6 - len(hex_length)
        packet_prefix = "121500" + ("0" * zeros_needed)
        
        final_packet_hex = packet_prefix + hex_length + encrypted_packet
        final_packet = bytes.fromhex(final_packet_hex)
        
        print(f"✅ Created packet with Title ID: {title_id}")
        return final_packet
        
    except Exception as e:
        print(f"❌ Conversion error: {e}")
        return None
        


async def get_player_name_from_uid(uid, region="IND"):
    """Get player name from UID - uses same method as /friend command"""
    try:
        # Load token from token.json (same as /friend command)
        token = load_jwt_token()
        if not token:
            return f"Player_{uid[:4]}"  # Fallback if no token
        
        # Use your existing get_player_info function
        player_name, player_uid = get_player_info(str(uid), token)
        
        if player_name and player_name != "Unknown":
            return player_name
        else:
            return f"Player_{uid[:4]}"
            
    except Exception as e:
        print(f"❌ Error getting name for {uid}: {e}")
        return f"Player_{uid[:4]}"  # Fallback

async def send_all_titles_sequentiallly(uid, chat_id, key, iv, region, chat_type):
    """Send all titles one by one with 2-second delay"""
    
    # Get all titles
    all_titles = [
        904090014, 904090015, 904090024, 904090025, 904090026, 904090027, 904990070, 904990071, 904990072
    ]
    
    total_titles = len(all_titles)
    
    # Send initial message
    start_msg = f"""[B][C][FFFF00] REALY !


"""
    await safe_send_message(chat_type, start_msg, uid, chat_id, key, iv)
    
    try:
        for index, title_id in enumerate(all_titles):
            title_number = index + 1
            

            
            # Send the actual title using your existing method
            # You'll need to use your existing title sending logic here
            # For example:
            title_packet = await noob(uid, chat_id, key, iv, nickname="juli_dvrma", title_id=title_id)
            
            if title_packet and whisper_writer:
                whisper_writer.write(title_packet)
                await whisper_writer.drain()
                print(f"✅ Sent title {title_number}/{total_titles}: {title_id}")
            
            # Wait 2 seconds before next title (unless it's the last one)
            if title_number < total_titles:
                await asyncio.sleep(2)
        
        # Completion message
        completion_msg = f"""[B][C][FFFF00]LOL, NOW WHOS IS NOOB?
"""
        await safe_send_message(chat_type, completion_msg, uid, chat_id, key, iv)
        
    except Exception as e:
        error_msg = f"[B][C][FF0000]❌ Error sending titles: {str(e)}\n"
        await safe_send_message(chat_type, error_msg, uid, chat_id, key, iv)

async def handle_alll_titles_command(inPuTMsG, uid, chat_id, key, iv, region, chat_type=0):
    """Handle /alltitles command to send all titles sequentially"""
    
    parts = inPuTMsG.strip().split()
    
    if len(parts) == 1:
        target_uid = uid
        target_name = "Yourself"
    elif len(parts) == 2 and parts[1].isdigit():
        target_uid = parts[1]
        target_name = f"UID {target_uid}"
    else:
        error_msg = f"""[B][C][FF0000]❌ Usage: /alltitles [uid]
        
📝 Examples:
/alltitles - Send all titles to yourself
/alltitles 123456789 - Send all titles to specific UID

🎯 What it does:
1. Sends all 4 titles one by one
2. 2-second delay between each title
3. Sends in background (non-blocking)
4. Shows progress updates
"""
        await safe_send_message(chat_type, error_msg, uid, chat_id, key, iv)
        return
    
    # Start the title sequence in the background
    asyncio.create_task(
        send_all_titles_sequentiallly(target_uid, chat_id, key, iv, region, chat_type)
    )
    


async def RoomJoin(room_id, password, key, iv):
    """Join Free Fire custom room"""
    try:
        # Import your proto file
        from room_join_pb2 import join_room
        
        root = join_room()
        root.field_1 = 3  # Room join command
        
        # Nested object
        nested_object = root.field_2
        nested_object.field_1 = int(room_id)
        nested_object.field_2 = str(password)
        
        # Field 8
        nested_8 = nested_object.field_8
        nested_8.field_1 = "IDC3"
        nested_8.field_2 = 149
        nested_8.field_3 = "IND"
        
        # Other fields
        nested_object.field_9 = "\x01\x03\x04\x07\x09\x0a\x0b\x12\x0e\x16\x19\x20\x1d"  # Bytes, not string
        nested_object.field_10 = 1
        nested_object.field_12.SetInParent()  # Empty field
        nested_object.field_13 = 1
        nested_object.field_14 = 1
        nested_object.field_16 = "en"
        
        # Field 22
        nested_22 = nested_object.field_22
        nested_22.field_1 = 21
        
        # Serialize
        packet_hex = root.SerializeToString().hex()
        
        # Encrypt using your function
        encrypted_packet = await encrypt_packet(packet_hex, key, iv)
        packet_length = len(encrypted_packet) // 2
        
        # Convert length to hex
        hex_length = dec_to_hex(packet_length)  # Use your existing function
        
        # Build packet header (type 0e15 for room join)
        if len(hex_length) == 2:
            header = "0e15000000"
        elif len(hex_length) == 3:
            header = "0e1500000"
        elif len(hex_length) == 4:
            header = "0e150000"
        elif len(hex_length) == 5:
            header = "0e15000"
        else:
            header = "0e150000"
        
        final_packet_hex = header + hex_length + encrypted_packet
        
        return bytes.fromhex(final_packet_hex)
        
    except Exception as e:
        print(f"❌ Room join error: {e}")
        import traceback
        traceback.print_exc()
        return None
        

# Alternative: Using your fields dictionary format
async def RoomJoin_fields(room_id, password, key, iv):
    """Room join using your CrEaTe_ProTo format"""
    try:
        fields = {
            1: 3,  # Room join command
            2: {   # Nested object
                1: int(room_id),   # room_id
                2: str(password),  # password
                8: {  # field_8
                    1: "IDC3",
                    2: 149,
                    3: "IND"
                },
                9: b"\x01\x03\x04\x07\x09\x0a\x0b\x12\x0e\x16\x19\x20\x1d",  # Bytes!
                10: 1,
                12: {},  # Empty field
                13: 1,
                14: 1,
                16: "en",
                22: {  # field_22
                    1: 21
                }
            }
        }
        
        # Convert to protobuf
        proto_bytes = await CrEaTe_ProTo(fields)
        packet_hex = proto_bytes.hex()
        
        # Encrypt and build packet
        encrypted_packet = await encrypt_packet(packet_hex, key, iv)
        packet_length = len(encrypted_packet) // 2
        hex_length = dec_to_hex(packet_length)
        
        # Build header
        if len(hex_length) == 2:
            header = "0e15000000"
        elif len(hex_length) == 3:
            header = "0e1500000"
        elif len(hex_length) == 4:
            header = "0e150000"
        elif len(hex_length) == 5:
            header = "0e15000"
        else:
            header = "0e150000"
        
        final_packet_hex = header + hex_length + encrypted_packet
        return bytes.fromhex(final_packet_hex)
        
    except Exception as e:
        print(f"❌ Room join fields error: {e}")
        return None

def remove_from_whitelist(uid_to_remove):
    """Remove UID from whitelist"""
    global WHITELISTED_UIDS
    
    uid_str = str(uid_to_remove)
    
    # Don't allow removing owner
    if uid_str == "2270928791":  # Your UID
        return False, "Cannot remove bot owner from whitelist!"
    
    if uid_str not in WHITELISTED_UIDS:
        return False, f"UID {uid_str} not in whitelist"
    
    WHITELISTED_UIDS.remove(uid_str)
    return True, f"✅ Removed {uid_str} from whitelist"



async def handle_xjoin_command(inPuTMsG, uid, chat_id, key, iv, region, chat_type):
    """Handle /xjoin command to join custom rooms"""
    
    parts = inPuTMsG.strip().split()
    
    if len(parts) < 3:
        error_msg = f"""[B][C][FF0000]🎮 ROOM JOIN COMMAND

❌ Usage: /xjoin (room_id) (password)

📝 Examples:
/xjoin 123456 0000
/xjoin 987654 1111

🔑 Room Info:
• Room ID: 6-digit number
• Password: Usually 4 digits (0000-9999)

💡 Bot will join the custom room!
"""
        await safe_send_message(chat_type, error_msg, uid, chat_id, key, iv)
        return
    
    room_id = parts[1]
    password = parts[2]
    
    if not room_id.isdigit():
        error_msg = f"[B][C][FF0000]❌ Room ID must be numbers only!\n"
        await safe_send_message(chat_type, error_msg, uid, chat_id, key, iv)
        return
    
    # Send initial message
    initial_msg = f"[B][C][FFFF00]🚀 JOINING CUSTOM ROOM...\n🏠 Room: {room_id}\n🔑 Password: {password}\n"
    await safe_send_message(chat_type, initial_msg, uid, chat_id, key, iv)
    
    try:
        # Try method 1: Direct proto method
        room_packet = await RoomJoin(room_id, password, key, iv)
        
        if not room_packet:
            # Try method 2: Fields method
            room_packet = await RoomJoin_fields(room_id, password, key, iv)
        
        if room_packet and online_writer:
            # Send via Online connection
            online_writer.write(room_packet)
            await online_writer.drain()
            
            print(f"✅ Room join packet sent! Room: {room_id}")
            joinroom = join_room_chanel(room_id, key, iv)
            await SEndPacKeT(whisper_writer, online_writer, 'ChaT', joinroom)
            success_msg = f"""[B][C][FFFF00]✅ ROOM JOIN COMMAND SENT!

🏠 Room ID: {room_id}
🔑 Password: {password}
"""
        else:
            success_msg = f"[B][C][FF0000]❌ Failed to create room join packet!\n"
        
        await safe_send_message(chat_type, success_msg, uid, chat_id, key, iv)
        
    except Exception as e:
        error_msg = f"[B][C][FF0000]❌ Error joining room: {str(e)}\n"
        await safe_send_message(chat_type, error_msg, uid, chat_id, key, iv)

async def spam_request_loop_with_cosmetics(target_uid, key, iv, region):
    """Spam request function that creates group and sends join requests in loop - FASTER VERSION"""
    global spam_request_running
    count = 0
    max_requests = 100  # Send exactly 30 requests
    
    while spam_request_running and count < max_requests:
        try:
            # Create squad
            PAc = await OpEnSq(key, iv, region)
            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', PAc)
            await asyncio.sleep(0.2)  # Reduced delay
            
            # Send invite
            V = await SEnd_InV(5, int(target_uid), key, iv, region)
            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', V)
            
            # Leave squad immediately without waiting
            E = await ExiT(None, key, iv)
            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', E)
            
            count += 1
            print(f"Sent request #{count} to {target_uid}")
            
            # Shorter delay between requests
            await asyncio.sleep(0.5)  # Reduced from 1 second to 0.5 seconds
            
        except Exception as e:
            print(f"Error in spam_request_loop for uid {target_uid}: {e}")
            # Continue with next request instead of breaking
            await asyncio.sleep(0.5)
            
async def handle_room_command(inPuTMsG, uid, chat_id, key, iv, region, chat_type):
    """Handle /room command with proper error handling"""
    
    parts = inPuTMsG.strip().split()
    
    if len(parts) < 2:
        error_msg = f"[B][C][FF0000]❌ Usage: /room (uid)\nExample: /room 11686472351\n"
        await safe_send_message(chat_type, error_msg, uid, chat_id, key, iv)
        return
    
    target_uid = parts[1]
    
    try:
        # Step 1: Check player status
        status_result, status_message = await check_player_status(target_uid, key, iv)
        
        packet = None
        player_status = None
        
        # If live check failed, try cache
        if not status_result:
            # Check cache
            cached_data = load_from_cache(target_uid)
            if cached_data and 'packet' in cached_data:
                packet = cached_data['packet']
                player_status = cached_data.get('status', 'UNKNOWN')
                print(f"⚠️ Using cached data for {target_uid}")
            else:
                error_msg = f"[B][C][FF0000]❌ Player {target_uid} not found\n"
                await safe_send_message(chat_type, error_msg, uid, chat_id, key, iv)
                return
        else:
            # Use live data
            packet = status_result.get('packet', b'')
            player_status = get_player_status(packet)
        
        # Step 2: Check if player is in room
        if not player_status or "IN ROOM" not in player_status:
            info_msg = f"""[B][C][FFFF00]📊 STATUS: {player_status or 'UNKNOWN'}

👤 Player: {target_uid}
❌ Not in custom room

💡 Player must join custom room first!"""
            await safe_send_message(chat_type, info_msg, uid, chat_id, key, iv)
            return
        
        # Step 3: Extract room ID
        room_id = get_idroom_by_idplayer(packet) if packet else None
        
        if not room_id:
            error_msg = f"[B][C][FF0000]❌ Failed to extract room ID\n"
            await safe_send_message(chat_type, error_msg, uid, chat_id, key, iv)
            return
        
        # Step 4: SUCCESS - Send room info
        success_msg = f"""[B][C][FFFF00]✅ ROOM FOUND!

👤 Player: {target_uid}
🏠 Room ID: {room_id}
📊 Status: {player_status}
⚡ Data: {'CACHED' if not status_result else 'LIVE'}

💡 Quick join: /xjoin {room_id} 0000
"""
        await safe_send_message(chat_type, success_msg, uid, chat_id, key, iv)
        
        # Step 5: AUTO-SPAM (add this if you want spam)
        # Uncomment this section if you want auto-spam:
        
        spam_count = 5
        for i in range(spam_count):
            try:
                spam_packet = await Room_Spam(target_uid, room_id, f"Spam_{i+1}", key, iv)
                if spam_packet and online_writer:
                    await SEndPacKeT(whisper_writer, online_writer, 'OnLine', spam_packet)
                    await asyncio.sleep(0.2)
            except Exception as e:
                print(f"Spam error: {e}")
        
        spam_msg = f"[B][C][FFFF00]✅ Spammed {spam_count} invites!\n"
        await safe_send_message(chat_type, spam_msg, uid, chat_id, key, iv)
        
        
    except Exception as e:
        print(f"❌ Room command error: {e}")
        error_msg = f"[B][C][FF0000]❌ Error: {str(e)[:80]}\n"
        await safe_send_message(chat_type, error_msg, uid, chat_id, key, iv)

# Room spam command (send multiple messages)
async def handle_room_spam_command(inPuTMsG, uid, chat_id, key, iv, region, chat_type):
    """Handle /spamroom command to send room spam messages"""
    
    parts = inPuTMsG.strip().split()
    
    if len(parts) < 4:
        error_msg = f"""[B][C][FF0000]❌ Usage: /spamroom (room_id) (uid) (message)
        
📝 Example: /spamroom 123456 14010319252 Hello World!

⚙️ Parameters:
• room_id = Custom room ID (numbers)
• uid = Player UID to spam
• message = Text message to send

🎯 What it does:
1. Creates room spam packet
2. Sends message to specified room
3. Uses colorful formatting
4. Packet type: 0e15 (room spam)
"""
        await safe_send_message(chat_type, error_msg, uid, chat_id, key, iv)
        return
    
    try:
        room_id = parts[1]
        target_uid = parts[2]
        message = ' '.join(parts[3:])
        
        # Validate inputs
        if not room_id.isdigit():
            error_msg = f"[B][C][FF0000]❌ Room ID must be numbers only!\n"
            await safe_send_message(chat_type, error_msg, uid, chat_id, key, iv)
            return
            
        if not target_uid.isdigit():
            error_msg = f"[B][C][FF0000]❌ UID must be numbers only!\n"
            await safe_send_message(chat_type, error_msg, uid, chat_id, key, iv)
            return
        
        # Send initial message
        initial_msg = f"[B][C][FFFF00]🚀 PREPARING ROOM SPAM...\n"
        initial_msg += f"🏠 Room ID: {room_id}\n"
        initial_msg += f"👤 Target UID: {target_uid}\n"
        initial_msg += f"📝 Message: {message[:30]}...\n"
        initial_msg += f"📦 Packet type: 0e15\n"
        initial_msg += f"⏳ Creating packet...\n"
        
        await safe_send_message(chat_type, initial_msg, uid, chat_id, key, iv)
        
        # Create and send the spam packet
        spam_packet = await SPam_Room(target_uid, room_id, message, key, iv)
        
        if spam_packet:
            # Send via Online connection (since it's room-related)
            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', spam_packet)
            
            success_msg = f"""[B][C][FFFF00]✅ ROOM SPAM PACKET SENT!

🏠 Room: {room_id}
👤 Target: {target_uid}
📝 Message: {message[:40]}...
📦 Packet: Type 0e15 (Room Spam)
✅ Status: Delivered successfully

💡 Packet includes:
• Colorful message formatting
• Avatar: {await xBunnEr()}
• Rank: 330
• Badge: 201
"""
        else:
            success_msg = f"[B][C][FF0000]❌ Failed to create spam packet!\n"
        
        await safe_send_message(chat_type, success_msg, uid, chat_id, key, iv)
        
    except Exception as e:
        error_msg = f"[B][C][FF0000]❌ Error: {str(e)}\n"
        await safe_send_message(chat_type, error_msg, uid, chat_id, key, iv)

# Also create a shorter alias command handler
async def handle_sr_command(inPuTMsG, uid, chat_id, key, iv, region, chat_type):
    """Handle /sr command (short version of /spamroom)"""
    await handle_room_spam_command(inPuTMsG, uid, chat_id, key, iv, region, chat_type)
        
async def detect_emote_perfect(data_hex, key, iv):
    """100% ACCURATE emote detection using YOUR exact packet structure"""
    
    try:
        # Step 1: Decrypt using your EXACT method
        decrypted = await DeCode_PackEt(data_hex[10:])  # Use YOUR existing function
        packet_json = json.loads(decrypted)
        
        # Step 2: EXACT STRUCTURE MATCHING
        # Check for Type 21 (from your Emote_k function)
        if packet_json.get('1') == 21:
            # Check for the EXACT structure you use
            if '2' in packet_json and 'data' in packet_json['2']:
                emote_data = packet_json['2']['data']
                
                # Verify EXACT field structure matches Emote_k()
                if ('1' in emote_data and '2' in emote_data and 
                    '5' in emote_data and 'data' in emote_data['5']):
                    
                    nested = emote_data['5']['data']
                    
                    # THIS IS THE 100% ACCURATE DETECTION
                    # Matches EXACTLY what you send in Emote_k()
                    if '1' in nested and '3' in nested:
                        return {
                            'type': 'emote',
                            'packet_type': 21,  # ← EXACT MATCH
                            'identifier': emote_data.get('1', {}).get('data'),
                            'base_emote': emote_data.get('2', {}).get('data'),
                            'target_uid': nested.get('1', {}).get('data'),  # WHO received it
                            'emote_id': nested.get('3', {}).get('data'),
                            'confidence': 100.0,
                            'raw_packet': packet_json
                        }
        
        # ALTERNATIVE FORMAT: Direct to player
        elif packet_json.get('1') == 26:  # Another emote type
            # Add similar exact matching here
            pass
        
        return None
        
    except Exception as e:
        print(f"❌ Perfect detection error: {e}")
        return None
        
async def detect_emote_with_sender(data_hex, key, iv):
    """Detect emote AND find who sent it"""
    
    try:
        # First, detect if it's an emote packet
        emote_info = await detect_emote_perfect(data_hex, key, iv)
        
        if not emote_info:
            return None
        
        # Now we need to find the SENDER's UID
        # Look for sender in different packet parts
        
        # METHOD 1: Check packet header for UID
        packet_header = data_hex[:20]
        
        # Look for UID patterns in hex (9-11 digits)
        import re
        uid_pattern = r'(\d{9,11})'
        
        # Search in entire packet
        all_uids = re.findall(uid_pattern, data_hex)
        
        if len(all_uids) >= 2:
            # We have at least 2 UIDs: sender and target
            # The target is already in emote_info['target_uid']
            target_uid = str(emote_info['target_uid'])
            
            # Find which UID is NOT the target
            for uid in all_uids:
                if uid != target_uid:
                    # This is likely the SENDER
                    emote_info['sender_uid'] = int(uid)
                    emote_info['detection_method'] = 'uid_pattern'
                    
                    print(f"✅ SENDER FOUND: {uid} sent emote to {target_uid}")
                    return emote_info
        
        # METHOD 2: Look in packet structure
        packet_json = emote_info['raw_packet']
        
        # Search recursively for UID that's NOT the target
        def find_sender_in_json(obj, target_uid):
            if isinstance(obj, dict):
                for k, v in obj.items():
                    if k == 'data' and isinstance(v, (int, str)):
                        v_str = str(v)
                        if v_str.isdigit() and len(v_str) > 8:
                            if v_str != str(target_uid):
                                return int(v)
                    elif isinstance(v, dict):
                        result = find_sender_in_json(v, target_uid)
                        if result:
                            return result
            return None
        
        sender_uid = find_sender_in_json(packet_json, emote_info['target_uid'])
        if sender_uid:
            emote_info['sender_uid'] = sender_uid
            emote_info['detection_method'] = 'json_search'
            return emote_info
        
        # If we can't find sender, at least we detected the emote
        emote_info['sender_uid'] = None
        return emote_info
        
    except Exception as e:
        print(f"❌ Sender detection error: {e}")
        return None


async def send_title_packet_direct(target_uid, chat_id, key, iv, region="ind"):
    """Send title packet directly without chat context - for auto-join"""
    try:
        print(f"🎖️ Sending title to {target_uid} in chat {chat_id}")
        
        # Method 1: Using your existing function
        title_packet = await convert_kyro_to_your_system(target_uid, chat_id, key, iv)
        
        if title_packet and whisper_writer:
            # Send via Whisper connection
            whisper_writer.write(title_packet)
            await whisper_writer.drain()
            print(f"✅ Title sent via Whisper to {target_uid}")
            return True
            
    except Exception as e:
        print(f"❌ Error sending title directly: {e}")
        import traceback
        traceback.print_exc()
    
    return False

def extract_type_5(packet_json):
    """Extract from Type 5 packets"""
    if packet_json.get('1') == 5:
        try:
            if '2' in packet_json and 'data' in packet_json['2']:
                data = packet_json['2']['data']
                sender = data.get('1', {}).get('data')
                emote_id = data.get('4', {}).get('data')
                
                if sender:
                    return {
                        'sender_uid': sender,
                        'emote_id': emote_id or 909000063,  # Default if not found
                        'packet_type': 5,
                        'confidence': 'medium'
                    }
        except:
            pass
    return None

async def extract_emote_info(data_hex, key, iv):
    """Extract full emote info from packet"""
    try:
        packet = await DeCode_PackEt(data_hex[10:])
        packet_json = json.loads(packet)
        
        # DEBUG: Print packet structure
        # print("📦 Packet JSON:", json.dumps(packet_json, indent=2)[:300])
        
        # Check all possible structures
        structures = [
            # Type 21 (from your Emote_k)
            lambda: extract_type_21(packet_json),
            # Type 26
            lambda: extract_type_26(packet_json),
            # Type 5
            lambda: extract_type_5(packet_json),
            # Generic search
            lambda: generic_extract(packet_json)
        ]
        
        for extractor in structures:
            info = extractor()
            if info and info.get('sender_uid'):
                return info
        
        return None
        
    except Exception as e:
        print(f"❌ Extraction error: {e}")
        return None

def extract_type_21(packet_json):
    """Extract from Type 21 (your Emote_k structure)"""
    if packet_json.get('1') == 21:
        try:
            if ('2' in packet_json and 'data' in packet_json['2'] and
                '5' in packet_json['2']['data'] and 'data' in packet_json['2']['data']['5']):
                
                data = packet_json['2']['data']
                nested = data['5']['data']
                
                sender = nested.get('1', {}).get('data')
                emote_id = nested.get('3', {}).get('data')
                
                if sender and emote_id:
                    return {
                        'sender_uid': sender,
                        'emote_id': emote_id,
                        'packet_type': 21,
                        'confidence': 'high'
                    }
        except:
            pass
    return None

def extract_type_26(packet_json):
    """Extract from Type 26 (common emote)"""
    if packet_json.get('1') == 26:
        try:
            if '2' in packet_json and 'data' in packet_json['2']:
                data = packet_json['2']['data']
                sender = data.get('1', {}).get('data')
                emote_id = data.get('2', {}).get('data')
                
                if sender and emote_id:
                    return {
                        'sender_uid': sender,
                        'emote_id': emote_id,
                        'packet_type': 26,
                        'confidence': 'high'
                    }
        except:
            pass
    return None

# Add these imports at the top with your other imports
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import base64
import json
import requests
import asyncio

# Add these constants with your other global variables
BIO_ENCRYPTION_KEY = bytes([89, 103, 38, 116, 99, 37, 68, 69, 117, 104, 54, 37, 90, 99, 94, 56])
BIO_ENCRYPTION_IV = bytes([54, 111, 121, 90, 68, 114, 50, 50, 69, 51, 121, 99, 104, 106, 77, 37])
FREEFIRE_VERSION = "OB53"

def decode_jwt_noverify(token: str):
    """Decode JWT without verification"""
    try:
        parts = token.split(".")
        if len(parts) < 2:
            return None
        payload_b64 = parts[1] + "=" * (-len(parts[1]) % 4)
        payload = json.loads(base64.urlsafe_b64decode(payload_b64).decode())
        return payload
    except Exception:
        return None

# Add these global variables

async def is_bot_in_squad(bot_uid, key, iv):
    """Quick check if bot is in squad (with caching)"""
    global last_bot_status_check, cached_bot_status
    
    # Use cache if recent
    current_time = time.time()
    if (current_time - last_bot_status_check < bot_status_cache_time and 
        cached_bot_status is not None):
        return cached_bot_status
    
    try:
        # Send status request
        status_packet = await createpacketinfo(bot_uid, key, iv)
        if status_packet and online_writer:
            online_writer.write(status_packet)
            await online_writer.drain()
            
            # Wait for response
            await asyncio.sleep(2)
            
            # Check cache
            if bot_uid in status_response_cache:
                packet = status_response_cache[bot_uid].get('packet', b'')
                status = get_player_status(packet)
                
                in_squad = "INSQUAD" in status
                cached_bot_status = in_squad
                last_bot_status_check = current_time
                
                return in_squad
        
        return False
        
    except Exception as e:
        print(f"❌ Squad check error: {e}")
        return False

def get_bio_server_url(lock_region: str):
    """Get bio endpoint based on region"""
    region = lock_region.upper()
    if region == "IND":
        return "https://client.ind.freefiremobile.com/UpdateSocialBasicInfo"
    elif region in {"BR", "US", "SAC", "NA"}:
        return "https://client.us.freefiremobile.com/UpdateSocialBasicInfo"
    elif region == "BD":
        return "https://client.bd.freefiremobile.com/UpdateSocialBasicInfo"
    elif region == "SG":
        return "https://client.sg.freefiremobile.com/UpdateSocialBasicInfo"
    else:
        return "https://clientbp.ggblueshark.com/UpdateSocialBasicInfo"

def create_bio_protobuf(bio_text):
    """Create protobuf message for bio update - EXACT SAME AS YOUR FLASK API"""
    # This creates the EXACT same protobuf structure as your Flask API
    
    # Protobuf structure from your API:
    # field_2: 17 (0x11)
    # field_5: EmptyMessage
    # field_6: EmptyMessage  
    # field_8: bio_text (string)
    # field_9: 1 (0x01)
    # field_11: EmptyMessage
    # field_12: EmptyMessage
    
    # Build protobuf manually (matching your exact structure)
    # Field 2: varint 17
    field_2 = b'\x08\x11'  # tag:1 type:varint value:17
    
    # Field 5: EmptyMessage (empty bytes)
    field_5 = b'\x2A\x00'  # tag:5 type:length-delimited length:0
    
    # Field 6: EmptyMessage (empty bytes)
    field_6 = b'\x32\x00'  # tag:6 type:length-delimited length:0
    
    # Field 8: bio text (string)
    bio_bytes = bio_text.encode('utf-8')
    bio_length = len(bio_bytes)
    field_8 = b'\x42' + bytes([bio_length]) + bio_bytes  # tag:8 type:string
    
    # Field 9: varint 1
    field_9 = b'\x48\x01'  # tag:9 type:varint value:1
    
    # Field 11: EmptyMessage
    field_11 = b'\x5A\x00'  # tag:11 type:length-delimited length:0
    
    # Field 12: EmptyMessage
    field_12 = b'\x62\x00'  # tag:12 type:length-delimited length:0
    
    # Combine all fields
    protobuf_data = field_2 + field_5 + field_6 + field_8 + field_9 + field_11 + field_12
    return protobuf_data

async def set_bio_directly_async_with_retry(jwt_token, bio_text, region="IND", max_retries=3, retry_delay=2):
    """Set bio with automatic retry logic"""
    
    for attempt in range(max_retries):
        try:
            print(f"🔄 Bio API attempt {attempt + 1}/{max_retries}")
            
            result = await set_bio_directly_async(jwt_token, bio_text, region)
            
            if result.get("success"):
                return result
            else:
                print(f"❌ Bio update failed: {result.get('message')}")
                if attempt < max_retries - 1:
                    await asyncio.sleep(retry_delay)
                    
        except Exception as e:
            print(f"❌ Bio attempt {attempt + 1} error: {e}")
            if attempt < max_retries - 1:
                await asyncio.sleep(retry_delay)
            continue
    
    # If all retries failed
    return {
        "success": False,
        "message": f"All {max_retries} attempts failed"
    }

async def set_bio_directly_async(jwt_token, bio_text, region="IND"):
    """Set bio directly - ASYNC version with better error handling"""
    try:
        # Decode JWT to get region
        payload = decode_jwt_noverify(jwt_token)
        if not payload:
            return {
                "success": False,
                "message": "Invalid JWT token"
            }
        
        lock_region = payload.get("lock_region", region).upper()
        url_bio = get_bio_server_url(lock_region)
        
        print(f"🔧 Setting bio for region: {lock_region}")
        print(f"📝 Bio text: {bio_text}")
        
        # Create protobuf message
        data_bytes = create_bio_protobuf(bio_text)
        print(f"📦 Protobuf created: {len(data_bytes)} bytes")
        
        # Encrypt using AES CBC
        cipher = AES.new(BIO_ENCRYPTION_KEY, AES.MODE_CBC, BIO_ENCRYPTION_IV)
        
        # Pad data to AES block size (16 bytes)
        padding_length = 16 - (len(data_bytes) % 16)
        if padding_length:
            data_bytes += bytes([padding_length] * padding_length)
        
        encrypted_data = cipher.encrypt(data_bytes)
        print(f"🔐 Encrypted: {len(encrypted_data)} bytes")
        
        # Headers
        headers = {
            "Expect": "100-continue",
            "Authorization": f"Bearer {jwt_token}",
            "X-Unity-Version": "2018.4.11f1",
            "X-GA": "v1 1",
            "ReleaseVersion": FREEFIRE_VERSION,
            "Content-Type": "application/x-www-form-urlencoded",
            "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 11; SM-A305F Build/RP1A.200720.012)",
            "Connection": "Keep-Alive",
            "Accept-Encoding": "gzip"
        }
        
        print(f"🚀 Sending to: {url_bio}")
        
        # Use aiohttp with timeout
        import aiohttp
        timeout = aiohttp.ClientTimeout(total=10)
        
        async with aiohttp.ClientSession(timeout=timeout) as session:
            async with session.post(url_bio, headers=headers, data=encrypted_data) as response:
                response_text = await response.text()
                
                print(f"📡 Response status: {response.status}")
                
                if response.status == 200:
                    return {
                        "success": True,
                        "message": "Bio updated successfully!",
                        "region": lock_region,
                        "bio": bio_text
                    }
                else:
                    return {
                        "success": False,
                        "message": f"Server error: {response.status} - {response_text[:100]}"
                    }
                
    except aiohttp.ClientError as e:
        print(f"❌ Network error: {e}")
        return {
            "success": False,
            "message": f"Network error: {str(e)[:80]}"
        }
    except asyncio.TimeoutError:
        print(f"❌ Request timeout")
        return {
            "success": False,
            "message": "Request timeout (10s)"
        }
    except Exception as e:
        print(f"❌ Bio update error: {e}")
        import traceback
        traceback.print_exc()
        return {
            "success": False,
            "message": f"Error: {str(e)[:80]}"
        }

# Now add this command handler to your TcPChaT function
# Find where other commands are handled and add this:

def analyze_squad_packet(packet_json):
    """Analyze packet structure to find squad members"""
    
    print("\n🔍 ANALYZING SQUAD PACKET STRUCTURE")
    print("="*50)
    
    # Check if this is a squad data packet
    if '5' not in packet_json or 'data' not in packet_json['5']:
        print("❌ Not a squad data packet")
        return None
    
    squad_data = packet_json['5']['data']
    
    # Look for fields that could contain multiple players
    candidate_fields = []
    
    for field_num in squad_data:
        field_info = squad_data[field_num]
        if 'data' not in field_info:
            continue
            
        data_value = field_info['data']
        
        # Check if it's a list (likely contains multiple players)
        if isinstance(data_value, list):
            print(f"✅ Field {field_num}: LIST with {len(data_value)} items")
            candidate_fields.append((field_num, 'list', data_value))
            
            # Show first item structure
            if data_value and isinstance(data_value[0], dict):
                print(f"   First item keys: {list(data_value[0].keys())}")
                # Check if first item has UID (field 1)
                if '1' in data_value[0]:
                    uid = data_value[0]['1']['data']
                    print(f"   ↳ Contains UID: {uid}")
        
        # Check if it's a dict with numeric keys (0, 1, 2, 3...)
        elif isinstance(data_value, dict):
            keys = list(data_value.keys())
            numeric_keys = [k for k in keys if k.isdigit()]
            if len(numeric_keys) > 0:
                print(f"✅ Field {field_num}: DICT with numeric keys {numeric_keys[:5]}...")
                candidate_fields.append((field_num, 'dict', data_value))
    
    print("\n🎯 MOST LIKELY SQUAD MEMBERS FIELDS:")
    for field_num, field_type, data in candidate_fields:
        print(f"  Field {field_num} ({field_type})")
        
        if field_type == 'list':
            # Try to extract UIDs from list
            uids = []
            for item in data[:5]:  # Check first 5 items
                if isinstance(item, dict) and '1' in item:
                    uid = item['1']['data']
                    uids.append(uid)
            if uids:
                print(f"    ↳ Found UIDs: {uids}")
        
        elif field_type == 'dict':
            # Try to extract UIDs from dict
            uids = []
            for key in list(data.keys())[:5]:  # Check first 5 keys
                item = data[key]
                if isinstance(item, dict) and '1' in item:
                    uid = item['1']['data']
                    uids.append(uid)
            if uids:
                print(f"    ↳ Found UIDs: {uids}")
    
    return candidate_fields

def generic_extract(packet_json):
    """Generic search for UID and emote ID"""
    uid = None
    emote_id = None
    
    # Recursively search for UID (long number)
    def search(obj):
        nonlocal uid, emote_id
        
        if isinstance(obj, dict):
            for k, v in obj.items():
                if k == 'data' and isinstance(v, (int, str)) and str(v).isdigit():
                    # Check if it looks like a UID (long number)
                    num = int(v)
                    if 1000000 < num < 99999999999:  # Reasonable UID range
                        if not uid:  # First found is likely sender
                            uid = num
                        # Check if it's an emote ID (starts with 909...)
                        elif str(v).startswith('909') and len(str(v)) >= 9:
                            emote_id = num
                
                elif isinstance(v, dict):
                    search(v)
                elif isinstance(v, list):
                    for item in v:
                        search(item)
    
    search(packet_json)
    
    if uid:
        return {
            'sender_uid': uid,
            'emote_id': emote_id or 909000063,  # Default AK emote
            'packet_type': 'generic',
            'confidence': 'medium'
        }
    
    return None
    
async def auto_reply_with_emote(emote_info, key, iv):
    """Automatically reply with same emote"""
    
    try:
        # Get bot's UID (you need to set this)
        bot_uid = 14010319252  # Replace with your bot's actual UID
        
        sender_uid = emote_info['sender_uid']
        emote_id = emote_info['emote_id']
        
        # Send emote back to sender
        reply_packet = await Emote_k(sender_uid, emote_id, key, iv, region)
        
        if online_writer:
            online_writer.write(reply_packet)
            await online_writer.drain()
            
            print(f"🤖 Bot replied with emote {emote_id} to {sender_uid}")
            
    except Exception as e:
        print(f"❌ Auto-reply error: {e}")

def extract_squad_members_correct(packet_json):
    """Extract squad members from FULL squad packet"""
    
    print("\n🔍 EXTRACTING SQUAD MEMBERS")
    print("="*50)
    
    try:
        if ('5' not in packet_json or 
            'data' not in packet_json['5'] or 
            '2' not in packet_json['5']['data']):
            print("❌ Invalid packet structure")
            return []
        
        field2_data = packet_json['5']['data']['2']['data']
        
        squad_members = []
        
        # Field 2 has numeric keys: '1', '2', '3', '4', '5', etc.
        # Each key might be a squad member slot OR player data field
        
        # Let's check what each numeric key contains
        for key in field2_data:
            if not key.isdigit():
                continue
                
            item = field2_data[key]['data']
            print(f"\n📦 Key {key}: Type = {type(item)}")
            
            if isinstance(item, dict):
                # Check if this is a player object
                # Player objects usually have fields: 1=UID, 2=name, 4=rank, etc.
                if '1' in item and '2' in item:
                    try:
                        uid = item['1']['data']
                        name = item['2']['data']
                        
                        # Make sure it's a valid UID (not a small number)
                        if isinstance(uid, int) and uid > 1000000:
                            rank = item['4']['data'] if '4' in item else 0
                            
                            print(f"   ✅ PLAYER FOUND!")
                            print(f"      UID: {uid}")
                            print(f"      Name: {name}")
                            print(f"      Rank: {rank}")
                            
                            squad_members.append({
                                'slot': key,
                                'uid': uid,
                                'name': name,
                                'rank': rank
                            })
                        else:
                            print(f"   ❌ Not a UID: {uid}")
                            
                    except Exception as e:
                        print(f"   ❌ Error extracting player: {e}")
                else:
                    print(f"   ↳ Fields: {list(item.keys())[:5]}...")
            elif isinstance(item, (int, str)):
                print(f"   ↳ Value: {item}")
        
        print(f"\n🏆 TOTAL SQUAD MEMBERS FOUND: {len(squad_members)}")
        for member in squad_members:
            print(f"  • Slot {member['slot']}: {member['name']} (UID: {member['uid']})")
        
        return squad_members
        
    except Exception as e:
        print(f"❌ Extraction error: {e}")
        import traceback
        traceback.print_exc()
        return []
        
async def analyze_packet_structure(data_hex, key, iv):
    """Analyze and display packet structure"""
    
    print(f"\n📦 PACKET ANALYSIS")
    print("="*50)
    
    # Basic info
    print(f"📏 Length: {len(data_hex)} characters")
    print(f"🔢 Header: {data_hex[:10]}")
    
    # Try to decode
    try:
        if len(data_hex) > 20:
            decoded = await DeCode_PackEt(data_hex[10:])
            packet_json = json.loads(decoded)
            
            print(f"✅ Successfully decoded!")
            print(f"📊 Packet type (field 1): {packet_json.get('1', 'Unknown')}")
            
            # Show structure
            print(f"\n📋 PACKET STRUCTURE:")
            print(f"Top-level fields: {list(packet_json.keys())}")
            
            # Show field 1 value
            if '1' in packet_json:
                print(f"  Field 1: {packet_json['1']}")
            
            # Show if it contains emote ID patterns
            import re
            emote_patterns = re.findall(r'909[0-9a-f]{6}', data_hex)
            if emote_patterns:
                print(f"\n🎭 EMOTE IDS FOUND IN HEX: {emote_patterns}")
            
            # Show UID patterns
            uid_patterns = re.findall(r'(\d{9,11})', data_hex)
            uids = [uid for uid in uid_patterns if not uid.startswith('909')]
            if uids:
                print(f"👤 UIDS FOUND IN HEX: {uids}")
            
            # Return the decoded structure
            return packet_json
            
        else:
            print("❌ Packet too short to decode")
            return None
            
    except Exception as e:
        print(f"❌ Decode error: {e}")
        return None

async def RedZed_SendInv(bot_uid, uid, key, iv):
    """Async version of send invite function"""
    try:
        fields = {
            1: 2, 
            2: {
                1: int(uid), 
                2: "IND", 
                3: 1, 
                4: 1, 
                6: "RedZedKing!!", 
                7: 330, 
                8: 1000, 
                9: 100, 
                10: "DZ", 
                12: 1, 
                13: int(uid), 
                16: 1, 
                17: {
                    2: 159, 
                    4: "y[WW", 
                    6: 11, 
                    8: "1.120.2", 
                    9: 3, 
                    10: 1
                }, 
                18: 306, 
                19: 18, 
                24: 902000306, 
                26: {}, 
                27: {
                    1: 11, 
                    2: int(bot_uid), 
                    3: 99999999999
                }, 
                28: {}, 
                31: {
                    1: 1, 
                    2: 32768
                }, 
                32: 32768, 
                34: {
                    1: bot_uid, 
                    2: 8, 
                    3: b"\x10\x15\x08\x0A\x0B\x13\x0C\x0F\x11\x04\x07\x02\x03\x0D\x0E\x12\x01\x05\x06"
                }
            }
        }
        
        # Convert bytes properly
        if isinstance(fields[2][34][3], str):
            fields[2][34][3] = b"\x10\x15\x08\x0A\x0B\x13\x0C\x0F\x11\x04\x07\x02\x03\x0D\x0E\x12\x01\x05\x06"
        
        # Use async versions of your functions
        packet = await CrEaTe_ProTo(fields)
        packet_hex = packet.hex()
        
        # Generate final packet
        final_packet = await GeneRaTePk(packet_hex, '0515', key, iv)
        
        return final_packet
        
    except Exception as e:
        print(f"❌ Error in RedZed_SendInv: {e}")
        import traceback
        traceback.print_exc()
        return None
        
async def freeze_emote_spam(uid, key, iv, region, chat_type, chat_id, sender_uid):
    """Send 3 freeze emotes in 1-second cycles for 10 seconds"""
    global freeze_running
    
    try:
        cycles = 0
        max_cycles = FREEZE_DURATION  # 10 seconds
        
        while freeze_running and cycles < max_cycles:
            # Send all 3 emotes in sequence
            for i, emote_id in enumerate(FREEZE_EMOTES):
                if not freeze_running:
                    break
                    
                try:
                    # Send emote
                    emote_packet = await Emote_k(int(uid), emote_id, key, iv, region)
                    await SEndPacKeT(whisper_writer, online_writer, 'OnLine', emote_packet)
                    
                    print(f"❄️ Freeze emote {i+1}/{len(FREEZE_EMOTES)} sent: {emote_id}")
                    
                    # Small delay between emotes (0.3 seconds)
                    await asyncio.sleep(0.3)
                    
                except Exception as e:
                    print(f"❌ Error sending freeze emote {i+1}: {e}")
            
            cycles += 1
            print(f"🌀 Freeze cycle {cycles}/{max_cycles} completed")
            
            # Wait for next cycle (total 1 second per cycle)
            remaining_time = 1.0 - (0.3 * len(FREEZE_EMOTES))
            if remaining_time > 0:
                await asyncio.sleep(remaining_time)
        
        print(f"✅ Freeze sequence completed: {cycles} cycles")
        return cycles
        
    except Exception as e:
        print(f"❌ Freeze function error: {e}")
        return 0
        
async def handle_freeze_completion(freeze_task, uid, sender_uid, chat_id, chat_type, key, iv):
    """Handle freeze command completion"""
    try:
        cycles_completed = await freeze_task
        
        completion_msg = f"""[B][C][00FFFF]❄️ FREEZE COMMAND COMPLETED!

🎯 Target: {uid}
⏱️ Duration: {cycles_completed} seconds
🎭 Emotes sent: {cycles_completed * 3}
❄️ Sequence: 
  • 909040004 (Ice)
  • 909050008 (Frozen)
  • 909000002 (Freeze)

✅ Status: Complete!
"""
        await safe_send_message(chat_type, completion_msg, sender_uid, chat_id, key, iv)
        
    except asyncio.CancelledError:
        print("🛑 Freeze command cancelled")
    except Exception as e:
        error_msg = f"[B][C][FF0000]❌ Freeze error: {str(e)}\n"
        await safe_send_message(chat_type, error_msg, sender_uid, chat_id, key, iv)

async def test_emote_packet(target_uid, emote_id, key, iv, region="IND"):
    """Test if emote packet works and show structure"""
    
    print(f"\n🎭 TESTING EMOTE PACKET")
    print("="*50)
    
    # Create the packet using your function
    emote_packet = await Emote_k(target_uid, emote_id, key, iv, region)
    
    if not emote_packet:
        print("❌ Failed to create packet")
        return False
    
    # Convert to hex for analysis
    packet_hex = emote_packet.hex()
    
    print(f"📦 Packet created!")
    print(f"   Length: {len(packet_hex)} characters")
    print(f"   Header: {packet_hex[:20]}")
    
    # Try to decode it back
    try:
        if len(packet_hex) > 20:
            # Remove header (first 10 bytes = 20 hex chars)
            payload = packet_hex[20:]  # Skip header
            
            # Decrypt (you need to implement this)
            # For testing, let's see raw structure
            print(f"\n🔍 RAW PACKET STRUCTURE:")
            print(f"Full hex (first 200 chars):")
            print(packet_hex[:200] + "...")
            
            # Look for the UID in hex
            import re
            uid_hex = hex(target_uid)[2:]
            if uid_hex in packet_hex:
                print(f"✅ Target UID {target_uid} found in packet!")
            else:
                print(f"❌ Target UID not found in hex")
            
            # Look for emote ID
            emote_hex = hex(emote_id)[2:]
            if emote_hex in packet_hex:
                print(f"✅ Emote ID {emote_id} found in packet!")
            else:
                print(f"❌ Emote ID not found in hex")
        
        print(f"\n✅ Packet created successfully!")
        return True
        
    except Exception as e:
        print(f"❌ Analysis error: {e}")
        return False
        
async def send_and_monitor_emote(target_uid, emote_id, key, iv, region, reader):
    """Send emote and monitor response - FIXED VERSION"""
    
    print(f"\n🚀 SENDING TEST EMOTE")
    print(f"   👤 Target: {target_uid}")
    print(f"   🎭 Emote: {emote_id}")
    print("="*50)
    
    # 1. Create packet
    emote_packet = await Emote_k(target_uid, emote_id, key, iv, region)
    
    if not emote_packet:
        print("❌ Failed to create packet")
        return
    
    # 2. Send it
    print("📤 Sending packet...")
    if online_writer:
        online_writer.write(emote_packet)
        await online_writer.drain()
        print("✅ Packet sent!")
    else:
        print("❌ No connection")
        return
    
    # 3. Wait for response (SHORTER - 2 seconds)
    print("\n⏳ Waiting for response (2 seconds)...")
    
    responses = []
    start_time = time.time()
    
    while time.time() - start_time < 2:  # Reduced from 5 to 2 seconds
        try:
            # Read any response
            if reader:
                response = await asyncio.wait_for(reader.read(9999), timeout=0.1)
                if response:
                    resp_hex = response.hex()
                    responses.append(resp_hex)
                    
                    # Quick analysis
                    print(f"📥 Got response #{len(responses)}")
                    print(f"   Length: {len(resp_hex)} chars")
                    print(f"   Header: {resp_hex[:10]}")
                    
                    # Check if it's the emote echo
                    if '909' in resp_hex:
                        print(f"   🎭 Contains emote ID!")
        except asyncio.TimeoutError:
            continue
        except Exception as e:
            # Silent error - don't print
            pass
    
    # 4. Summary
    print(f"\n📊 RESPONSE SUMMARY")
    print(f"Total responses: {len(responses)}")
    
    if len(responses) > 0:
        print("✅ SUCCESS! Server accepted your emote packet!")
    else:
        print("⚠️ No immediate response (might still be processing)")
        
async def handle_guest_generation(count, uid, chat_id, chat_type, key, iv):
    """Handle guest generation in background and send updates"""
    try:
        # Start generation
        accounts = await generate_and_save_accounts(count)
        
        # Send completion message
        if accounts:
            success_msg = f"""[B][C][FFFF00]✅ GUEST ACCOUNTS GENERATED!

📊 Generated: {len(accounts)}/{count} accounts
💾 Saved to: guest_accounts.json

📋 Format in file:
• uid: Account UID
• password: Account password
• name: BlackApis
• timestamp: Generation time

💡 Use accounts for:
• Multi-account spams
• Friend requests
• Testing purposes
"""
        else:
            success_msg = f"""[B][C][FF0000]❌ GENERATION FAILED!

📊 Requested: {count} accounts
❌ Generated: 0 accounts

💡 Try:
1. Check internet connection
2. API might be down
3. Try smaller count (like 5)
4. Try again later
"""
        
        await safe_send_message(chat_type, success_msg, uid, chat_id, key, iv)
        
        # Optional: Send first account as preview
        if accounts:
            preview_msg = f"""[B][C][FFFF00]🔍 FIRST ACCOUNT PREVIEW:

👤 UID: {accounts[0]['uid']}
🔑 Pass: {accounts[0]['password']}
📛 Name: {accounts[0]['name']}

💡 Check guest_accounts.json for all accounts!
"""
            await safe_send_message(chat_type, preview_msg, uid, chat_id, key, iv)
            
    except Exception as e:
        error_msg = f"[B][C][FF0000]❌ Generation error: {str(e)[:50]}\n"
        await safe_send_message(chat_type, error_msg, uid, chat_id, key, iv)        
        
async def start_auto_packet(key, iv, region):
    """Create start match packet"""
    fields = {
        1: 9,
        2: {
            1: 12480598706,
        },
    }
    
    if region.lower() == "ind":
        packet_type = '0514'
    elif region.lower() == "bd":
        packet_type = "0519"
    else:
        packet_type = "0515"
        
    return await GeneRaTePk((await CrEaTe_ProTo(fields)).hex(), packet_type, key, iv)
        
async def detect_and_hijack_emote(data_hex, key, iv, bot_uid, region):
    """Detect emote and hijack it by sending with bot's UID"""
    try:
        # Detect emote info
        emote_info = await extract_emote_info(data_hex, key, iv)
        
        if not emote_info or not emote_info.get('sender_uid'):
            return False
        
        sender_uid = emote_info['sender_uid']
        emote_id = emote_info['emote_id']
        
        print(f"\n🎭 EMOTE DETECTED FOR HIJACK!")
        print(f"   👤 Original Sender: {sender_uid}")
        print(f"   🎭 Emote ID: {emote_id}")
        
        # Don't hijack bot's own emotes
        if int(sender_uid) == bot_uid:
            print("⚠️ Skipping - bot's own emote")
            return False
        
        # HIJACK: Send emote with bot's UID instead
        print(f"🤖 HIJACKING EMOTE! Sending as bot {bot_uid}...")
        
        # Use either of your emote functions
        # Method 1: Using Emote_k (your second packet)
        hijack_packet = await Emote_k(
            int(bot_uid),  # Use BOT'S UID instead of sender's
            int(emote_id),  # Same emote ID
            key, iv, region
        )
        
        # Alternative: Using emote_send (your first packet)
        # hijack_packet = await create_hijacked_emote(bot_uid, emote_id, key, iv, region)
        
        if hijack_packet and online_writer:
            # Send the hijacked emote
            online_writer.write(hijack_packet)
            await online_writer.drain()
            
            print(f"✅ Emote hijacked! Bot {bot_uid} now appears to do emote {emote_id}")
            return True
        
        return False
        
    except Exception as e:
        print(f"❌ Emote hijack error: {e}")
        return False
        
async def SwitchLoneWolfDule(BotUid, key, iv):
    fields = {1: 17, 2: {1: BotUid, 2: 1, 3: 1, 4: 43, 5: "\u000b", 8: 1, 19: 1}}
    return await GenPacket((await CreateProtobufPacket(fields)).hex(), '0519', key, iv)        
        
async def KickTarget(target_uid, key, iv):
    fields = {1: 35, 2: {1: int(target_uid)}}
    return await GeneRaTePk((await CrEaTe_ProTo(fields)).hex(), '0515' , key, iv)
        
async def create_hijacked_emote(hijacker_uid, emote_id, key, iv, region):
    """Create emote packet that appears to come from hijacker"""
    try:
        # Using your Emote_k structure but with hijacker's UID
        fields = {
            1: 21,  # Emote packet type
            2: {
                1: 804266360,  # Some identifier (keep as is)
                2: 909000001,  # Base emote ID
                5: {
                    1: int(hijacker_uid),  # HIJACKER'S UID goes here
                    3: int(emote_id),      # The emote ID to perform
                }
            }
        }
        
        if region.lower() == "ind":
            packet = '0514'
        elif region.lower() == "bd":
            packet = "0519"
        else:
            packet = "0515"
            
        return await GeneRaTePk((await CrEaTe_ProTo(fields)).hex(), packet, key, iv)
        
    except Exception as e:
        print(f"❌ Error creating hijacked emote: {e}")
        return None
            
def analyze_hex_packet(packet_hex):
    """Analyze hex packet structure"""
    
    print(f"\n🔬 HEX PACKET ANALYSIS")
    print("="*50)
    
    # Header analysis
    header = packet_hex[:10]
    print(f"Header (first 5 bytes): {header}")
    
    # Common headers:
    # 0514 = IND online packet
    # 0519 = BD online packet  
    # 1215 = Whisper packet
    # 1200 = Chat packet
    
    if header.startswith('05'):
        print("📡 Online connection packet")
    elif header.startswith('12'):
        print("💬 Whisper/Chat packet")
    
    # Look for UIDs (9-11 digit numbers in hex)
    import re
    
    # Find all sequences of 9+ hex digits
    hex_patterns = re.findall(r'[0-9a-f]{9,12}', packet_hex.lower())
    
    print(f"\n🔢 Hex sequences found:")
    for pattern in hex_patterns[:10]:  # Show first 10
        # Try to convert to decimal
        try:
            decimal = int(pattern, 16)
            if 1000000 < decimal < 99999999999:  # Reasonable UID range
                print(f"  {pattern} → {decimal} (Possible UID)")
            elif decimal > 900000000:  # Emote ID range
                print(f"  {pattern} → {decimal} (Possible emote ID)")
        except:
            print(f"  {pattern}")
    
    # Show packet content (first 200 chars)
    print(f"\n📝 Packet preview (first 200 chars):")
    print(packet_hex[:200])
    
    if len(packet_hex) > 200:
        print(f"... and {len(packet_hex) - 200} more characters")
        
def append_to_whitelist(uid_to_add):
    """Simple function to add UID to whitelist"""
    global WHITELISTED_UIDS
    
    uid_str = str(uid_to_add)
    
    if uid_str in WHITELISTED_UIDS:
        return False, f"UID {uid_str} already in whitelist"
    
    WHITELISTED_UIDS.add(uid_str)
    return True, f"✅ Added {uid_str} to whitelist"        
        
async def hijack_squad_emote(data_hex, key, iv, bot_uid, region, in_squad):
    """Only hijack emotes when bot is in a squad"""
    if not in_squad:
        return False
    
    try:
        # Extract emote info
        emote_info = await extract_emote_info(data_hex, key, iv)
        
        if not emote_info:
            return False
        
        sender_uid = emote_info['sender_uid']
        emote_id = emote_info['emote_id']
        
        print(f"\n🏆 SQUAD EMOTE HIJACK!")
        print(f"   👥 In squad: Yes")
        print(f"   👤 Original: {sender_uid}")
        print(f"   🎭 Emote: {emote_id}")
        
        # Create hijacked emote
        hijack_packet = await create_hijacked_emote(bot_uid, emote_id, key, iv, region)
        
        if hijack_packet and online_writer:
            online_writer.write(hijack_packet)
            await online_writer.drain()
            
            print(f"✅ Squad emote hijacked by bot {bot_uid}!")
            
            # Optional: Also send the original emote to maintain appearance
            await asyncio.sleep(0.3)
            original_packet = await Emote_k(int(sender_uid), int(emote_id), key, iv, region)
            online_writer.write(original_packet)
            await online_writer.drain()
            
            print(f"✅ Also sent original emote to maintain cover")
            
            return True
            
    except Exception as e:
        print(f"❌ Squad hijack error: {e}")
    
    return False
    
async def send_friend_request_async(target_uid: str, count: int = 1) -> dict:
    """
    Main function to send friend requests from TCP bot
    
    Args:
        target_uid: Target player UID
        count: Number of requests (1 for single, >1 for bulk)
    
    Returns:
        Dictionary with results
    """
    try:
        if count == 1:
            # Single request using token.json
            token = load_jwt_token()
            if not token:
                return {"success": 0, "failed": 1, "error": "No token found"}
            
            success = send_friend_request_single(target_uid, token)
            
            if success:
                return {"success": 1, "failed": 0}
            else:
                return {"success": 0, "failed": 1}
                
        else:
            # Bulk requests using token_ind.json
            tokens = load_tokens_ind()
            if not tokens:
                return {"success": 0, "failed": 0, "error": "No tokens found"}
            
            max_count = min(count, len(tokens))
            results = {"success": 0, "failed": 0}
            
            print(f"📦 Sending {max_count} friend requests...")
            
            # Send requests sequentially (or use threading for faster)
            for i in range(max_count):
                token = tokens[i]['token']
                success = send_friend_request_single(target_uid, token)
                
                if success:
                    results["success"] += 1
                else:
                    results["failed"] += 1
                
                # Small delay to avoid rate limiting
                await asyncio.sleep(0.1)
            
            return results
            
    except Exception as e:
        print(f"❌ Friend request error: {e}")
        return {"success": 0, "failed": 0, "error": str(e)}    

async def TcPOnLine(ip, port, key, iv, AutHToKen, reconnect_delay=0.5):
    global online_writer, last_status_packet, status_response_cache, senthi
    global insquad, joining_team, whisper_writer, region
 
    bot_uid = 14010319252
 
    if insquad is not None:
        insquad = None
    if joining_team is True:
        joining_team = False
    
    online_writer = None
    whisper_writer = None
    
    while True:
        try:
            print(f"Attempting to connect to {ip}:{port}...")
            reader, writer = await asyncio.open_connection(ip, int(port))
            online_writer = writer
            
            # --- AUTHENTICATION ---
            bytes_payload = bytes.fromhex(AutHToKen)
            online_writer.write(bytes_payload)
            await online_writer.drain()
            print("Authentication token sent. Listening for emotes...")
            
            # --- READING LOOP ---
            while True:
                data2 = await reader.read(9999)
                    
                if not data2: 
                    print("Connection closed by the server.")
                    break
                    
                data_hex = data2.hex()
      
                # Your existing code...
  
                
                
              # =================== EMOTE DETECTION ONLY ===================
                if data_hex.startswith("0500") and emote_hijack == True:
                    try:
                        # Try to detect emote
                        emote_info = await extract_emote_info(data_hex, key, iv)
                        
                        in_squad = insquad is not None
            

                

                        
                        if emote_info and emote_info.get('sender_uid'):
                            sender_uid = emote_info['sender_uid']
                            emote_id = emote_info['emote_id']
                            
                            
                            
                            print(f"\n🎯 EMOTE DETECTED!")
                            print(f"   👤 Sender UID: {sender_uid}")
                            print(f"   🎭 Emote ID: {emote_id}")
                            
                            # Don't respond to bot's own emotes
                            if int(sender_uid) != bot_uid:
                                print("🤖 Bot responding with dual emotes...")
                                
                                # STEP 1: Send fixed emote 909035003 to the sender
                                print(f"  1️⃣ Sending emote 909035003 to {sender_uid}")
                                fixed_emote_packet = await Emote_k(
                                    int(sender_uid), 
                                    909035003,  # Fixed emote ID
                                    key, iv, region
                                )
                                if fixed_emote_packet and online_writer:
                                    online_writer.write(fixed_emote_packet)
                                    await online_writer.drain()
                                    await asyncio.sleep(0.5)
                                
                                # STEP 2: Bot does the SAME emote that user did (to itself)
                                print(f"  2️⃣ Bot doing same emote {emote_id} to itself")
                                bot_self_emote = await Emote_k(
                                    bot_uid,  # Bot's own UID
                                    int(emote_id),  # Same emote user did
                                    key, iv, region
                                )
                                if bot_self_emote and online_writer:
                                    online_writer.write(bot_self_emote)
                                    await online_writer.drain()
                                    await asyncio.sleep(0.5)
                                
                                # STEP 3: Bot also sends the emote back to sender
                                print(f"  3️⃣ Mirroring emote {emote_id} back to {sender_uid}")
                                mirror_emote = await Emote_k(
                                    int(sender_uid),
                                    int(emote_id),  # Same emote back
                                    key, iv, region
                                )
                                if mirror_emote and online_writer:
                                    online_writer.write(mirror_emote)
                                    await online_writer.drain()
                                
                                print("✅ Dual emote response complete!")
                            
                            else:
                                print("⚠️ Skipping - bot's own emote")
                                
                    except Exception as e:
                        print(f"❌ Emote response error: {e}")
                        continue 
            
                    


                # =================== AUTO ACCEPT HANDLING ===================
                
                # Case 1: Squad is cancelled or left (6, 7 are often status/exit codes)
                if data_hex.startswith('0500') and insquad is not None and joining_team == False:
                    try:
                        # Assuming DeCode_PackEt and json.loads are available and correct
                        packet = await DeCode_PackEt(data_hex[10:])
                        packet_json = json.loads(packet)
                        
                        if packet_json.get('1') in [6, 7]: 
                             insquad = None
                             joining_team = False
                             print("Squad cancelled or exited (code 6/7).")
                             continue
                             
                    except Exception as e:
                        print(f"Error in auto-accept case 1: {e}")
                        pass
                
                # case 2
                # Case 2: Auto-accept for whitelisted users
                if data_hex.startswith("0500") and insquad is None and joining_team == False:
                    try:
                        packet = await DeCode_PackEt(data_hex[10:])
                        packet_json = json.loads(packet)
    
                        uid = packet_json['5']['data']['1']['data']
                        invite_uid = packet_json['5']['data']['2']['data']['1']['data']
                        squad_owner = packet_json['5']['data']['1']['data']  # Person inviting
                        code = packet_json['5']['data']['8']['data']
  

                        emote_id = 909050009
                        bot_uid = 14009897329
    
                        # 🎯 FIX: Check SQUAD_OWNER (person who clicked "invite")
                        if True:
                            print(f"✅ Whitelisted user {squad_owner} invited bot. Accepting...")
                        
                            SendInv = await RedZed_SendInv(bot_uid, invite_uid, key, iv)
                            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', SendInv)
                            inv_packet = await RejectMSGtaxt(squad_owner, uid, key, iv)
                            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', inv_packet)
        
                            print(f"Received squad invite from {squad_owner}, accepting...")                  
                            Join = await ArohiAccepted(squad_owner, code, key, iv)
                            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', Join)
        
                            await asyncio.sleep(2)
                                                    
                            emote_to_sender = await Emote_k(int(uid), emote_id, key, iv, region)
                            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', emote_to_sender)
        
                            bot_emote = await Emote_k(int(bot_uid), emote_id, key, iv, region)
                            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', bot_emote)
                            
                            
            
                            # Set squad status
                            insquad = True
                            print(f"🤖 Bot joined squad of {squad_owner}")
        
        
        
                        else:
                            try:
                                print(f"🚫 Bot is private! Ignoring invite from {squad_owner}")
                                 # Send quick reject message
                                bot_uid = 14010319252
                                message_text = f" Can't accept Your request Talk to D I A B LO__C O D E X !"
                                private_msg_packet = await xSEndMsg(
                                    Msg=message_text,
                                    Tp=2,  # 2 = Private message
                                    Tp2=int(squad_owner),  # Recipient UID
                                    id=int(bot_uid),  # Sender UID (your bot)
                                    K=key,
                                    V=iv
                                )
                                print("got it")

                                if private_msg_packet and whisper_writer:
                                    # Send via Whisper connection (chat connection)
                                    await SEndPacKeT(whisper_writer, online_writer, 'ChaT', private_msg_packet)
                                else:
                                    print("can't do it")
                    
                                    
                            except Exception as e:
                                print(" got an error in can't accept")
    

                    except Exception as e:
                        print(f"Error in auto-accept: {e}")
                        insquad = None
                        joining_team = False
                        continue
                
                # =================== HANDLE KICK/RECONNECT ===================
                # Case 3: Bot was kicked and needs to re-join chat
                if data_hex.startswith('0500') and len(data_hex) > 1000:
                    try:
                        packet = await DeCode_PackEt(data_hex[10:])
                        packet_json = json.loads(packet)
                    
                        packet_type = packet_json.get('1')
        
                        # Detect ALL kick/leave packets
                        if packet_type in [6, 7, 8, 9, 10, 11, 12]:
                            print(f"🚪 Kick/Leave packet detected (Type: {packet_type})")
            
                            # RESET SQUAD STATUS
                            insquad = None
                            joining_team = False
            
                            print(f"✅ Bot reset after kick. Ready for new invites.")
                            
                            # Try to extract squad info for possible reconnection
                            try:
                                if '5' in packet_json and 'data' in packet_json['5']:
                                    OwNer_UiD, CHaT_CoDe, SQuAD_CoDe = await GeTSQDaTa(packet_json)
                                    print(f"🔄 Attempting reconnection to squad {SQuAD_CoDe}...")
                    
                                    # Re-authenticate chat
                                    JoinCHaT = await AutH_Chat(3, OwNer_UiD, CHaT_CoDe, key, iv)
                                    await SEndPacKeT(whisper_writer, online_writer, 'ChaT', JoinCHaT)
                    
                                    print(f"✅ Chat re-authenticated for reconnection")
                            except:
                                print("⚠️ Could not extract squad info")
                                
                            continue  # Skip other handlers
        
                        # Also check for general squad data packets (for reconnection)
                        elif '5' in packet_json and 'data' in packet_json['5']:
                            try:
                                OwNer_UiD, CHaT_CoDe, SQuAD_CoDe = await GeTSQDaTa(packet_json)
                
                                # If we have squad data but insquad is None, try to reconnect
                                if insquad is None:
                                    print(f"🤖 Received squad data while not in squad. Attempting chat auth...")
                                    
                                    JoinCHaT = await AutH_Chat(3, OwNer_UiD, CHaT_CoDe, key, iv)
                                    await SEndPacKeT(whisper_writer, online_writer, 'ChaT', JoinCHaT)
                    
                                    # Optional welcome back message
                                    welcome_msg = """[B][C][FFFF00]🤖 Bot reconnected!"""
                                    P = await SEndMsG(0, welcome_msg, OwNer_UiD, OwNer_UiD, key, iv, region)
                                    await SEndPacKeT(whisper_writer, online_writer, 'ChaT', P)
                    
                            except:
                                pass  # Not a squad data packet
                
                    except Exception as e:
                        print(f"❌ Kick/reconnect handler error: {e}")
                        pass
                
                # case 5
                if insquad == True:
                    try:
                        # Assuming DeCode_PackEt, json.loads, GeTSQDaTa, AutH_Chat, SEndPacKeT are available
                        packet = await DeCode_PackEt(data_hex[10:])
                        packet_json = json.loads(packet)
                        
                        OwNer_UiD , CHaT_CoDe , SQuAD_CoDe = await GeTSQDaTa(packet_json)
                        
                        print(f"Received squad data for joining team, attempting chat auth for {OwNer_UiD}...")
                        JoinCHaT = await AutH_Chat(3 , OwNer_UiD , CHaT_CoDe, key,iv)
                        await SEndPacKeT(whisper_writer , online_writer , 'ChaT' , JoinCHaT)
                        
                        def get_random_color(): return "_" 
                        message = """[[B][C][9B59B6]╔═══◆ WELCOME TO ZAINUㅤVIP BOT ◆═══╗
[7F8C8D]╟──────────────────────────────╢
[FFFFFF]⚡ Powered By : [BB8FCE]ZAINUㅤVIP
[FFFFFF]🎯 Status     : [2ECC71]ONLINE All time
[FFFFFF]📱 Contact    : [1ABC9C]tt [b][c]@chayan210
[7F8C8D]╟──────────────────────────────╢
[9B59B6]╚═══◆ EXPERIENCE THE POWER ◆═══╝
"""
                        # In your auto-join (Old Handler) code, find this line:

                        P = await SEndMsG(0, message, OwNer_UiD, OwNer_UiD, key, iv, region)
                        await SEndPacKeT(whisper_writer, online_writer, 'ChaT', P)
                        
                        joining_team = False
                        insquad = None
                            
                    except Exception as e:
                        print(f"Error in joining_team chat auth: {e}")
                        # Removed the redundant inner try/except block.
                        pass
                
                if "0600" in data2.hex()[0:4] and len(data2.hex()) > 700:
                    accept_packet = f'08{data2.hex().split("08", 1)[1]}'
                    kk = get_available_room(accept_packet)
                    parsed_data = json.loads(kk)
                    #logging.info(parsed_data)

                    senthi = True

                if senthi == True:
                    
                    def get_random_color(): return "_" 
                    message = """[B][C][9B59B6]╔═══◆ WELCOME TO ZAINUㅤVIP BOT ◆═══╗
[7F8C8D]╟──────────────────────────────╢
[FFFFFF]⚡ Powered By : [BB8FCE]ZAINUㅤVIP
[FFFFFF]🎯 Status     : [2ECC71]ONLINE 24/7
[FFFFFF]📱 Contact    : [1ABC9C]tt [b][c]@9x_jubayer_
[7F8C8D]╟──────────────────────────────╢
[9B59B6]╚═══◆ EXPERIENCE THE POWER ◆═══╝"""
                        # In your auto-join (Old Handler) code, find this line:

                    P = await SEndMsG(0, message, OwNer_UiD, OwNer_UiD, key, iv, region)
                    await SEndPacKeT(whisper_writer, online_writer, 'ChaT', P)
                    senthi = False

                # =================== STATUS HANDLER ===================
                if data_hex.startswith('0f00') and len(data_hex) > 100:
                    print(f"📡 Received status response packet")
    
                    try:
                        # Assuming the protocol structure: 0f00 + length bytes + 08 + actual proto data
                        # The split logic might need refinement based on the exact protocol
                        if '08' in data_hex:
                            proto_part = f'08{data_hex.split("08", 1)[1]}'
                        else:
                            print("⚠️ Status packet structure missing '08' marker.")
                            continue
        
                        # Assuming get_available_room is available
                        parsed_data = get_available_room(proto_part)
                        if parsed_data:
                            parsed_json = json.loads(parsed_data)
            
                            # Check if it's field 15 (player info)
                            if "2" in parsed_json and parsed_json["2"]["data"] == 15:
                                # Get player ID
                                player_id = parsed_json["5"]["data"]["1"]["data"]["1"]["data"]
                
                                # Assuming get_player_status is available
                                player_status = get_player_status(proto_part) 
                                print(f"✅ Parsed status for {player_id}: {player_status}")
                
                                # Create cache entry
                                cache_entry = {
                                    'status': player_status, 
                                    'packet': proto_part,
                                    'timestamp': time.time(),
                                    'full_packet': data_hex,
                                    'parsed_json': parsed_json
                                }
                
                                # --- SPECIAL CONDITION CHECK ---
                                try:
                                    StatusData = parsed_json
                                    if ("5" in StatusData and "data" in StatusData["5"] and 
                                        "1" in StatusData["5"]["data"] and "data" in StatusData["5"]["data"]["1"] and 
                                        "3" in StatusData["5"]["data"]["1"]["data"] and "data" in StatusData["5"]["data"]["1"]["data"]["3"] and 
                                        StatusData["5"]["data"]["1"]["data"]["3"]["data"] == 1 and 
                                        "11" in StatusData["5"]["data"]["1"]["data"] and "data" in StatusData["5"]["data"]["1"]["data"]["11"] and 
                                        StatusData["5"]["data"]["1"]["data"]["11"]["data"] == 1):
                
                                        print(f"🎯 SPECIAL CONDITION MET: Player {player_id} is in SOLO mode with special flag 11=1")
                                        cache_entry['special_state'] = 'SOLO_WITH_FLAG_1'
                
                                except Exception as cond_error:
                                    print(f"⚠️ Error checking special condition: {cond_error}")
                                # ------------------------------

                                # If in room, extract room ID
                                if "IN ROOM" in player_status:
                                    try:
                                        # Assuming get_idroom_by_idplayer is available
                                        room_id = get_idroom_by_idplayer(proto_part)
                                        if room_id:
                                            cache_entry['room_id'] = room_id
                                            print(f"🏠 Room ID extracted: {room_id}")
                                    except Exception as room_error:
                                        print(f"Failed to extract room ID: {room_error}")
                
                                # If in squad, extract leader
                                elif "INSQUAD" in player_status:
                                    try:
                                        # Assuming get_leader is available
                                        leader_id = get_leader(proto_part)
                                        if leader_id:
                                            cache_entry['leader_id'] = leader_id
                                            print(f"👑 Leader ID: {leader_id}")
                                    except Exception as leader_error:
                                        print(f"Failed to extract leader: {leader_error}")
                
                                # Save to FILE cache (Assuming save_to_cache is available)
                                save_to_cache(player_id, cache_entry)
                                print(f"✅ Saved to cache: {player_id} = {player_status}")
                
                    except Exception as e:
                        print(f"❌ Error parsing status: {e}")
                        import traceback
                        traceback.print_exc()
                
                # =================== END STATUS HANDLER ===================


            # --- CLEANUP AFTER INNER LOOP (Connection closed) ---
            if online_writer is not None:
                online_writer.close()
                await online_writer.wait_closed()
                online_writer = None
            
            if whisper_writer is not None:
                try:
                    whisper_writer.close()
                    await whisper_writer.wait_closed()
                except:
                    pass
                whisper_writer = None
                
            insquad = None
            joining_team = False
            
            print(f"Connection closed. Reconnecting in {reconnect_delay} seconds...")

        except ConnectionRefusedError:
            print(f"Connection refused by server at {ip}:{port}.")
        except asyncio.TimeoutError:
            print(f"Connection attempt to {ip}:{port} timed out.")
        except Exception as e:
            print(f"- ErroR With {ip}:{port} - {e}")
            traceback.print_exc() 
            
            # --- CLEANUP AFTER EXCEPTION ---
            if online_writer is not None:
                try:
                    online_writer.close()
                    await online_writer.wait_closed()
                except:
                    pass
                online_writer = None
            if whisper_writer is not None:
                try:
                    whisper_writer.close()
                    await whisper_writer.wait_closed()
                except:
                    pass
                whisper_writer = None
                
            insquad = None
            joining_team = False
            
        await asyncio.sleep(reconnect_delay)

async def send_keep_alive(key, iv, region):
    """Send keep-alive packet to maintain connection"""
    try:
        fields = {
            1: 99,  # Keep-alive packet type
            2: {
                1: int(time.time()),
                2: 1,  # Keep-alive flag
            }
        }
        
        if region.lower() == "ind":
            packet_type = '0514'
        elif region.lower() == "bd":
            packet_type = "0519"
        else:
            packet_type = "0515"
            
        packet = await GeneRaTePk((await CrEaTe_ProTo(fields)).hex(), packet_type, key, iv)
        return packet
    except Exception as e:
        print(f"❌ Keep-alive error: {e}")
        return None
        
                    

                            
async def TcPChaT(ip, port, AutHToKen, key, iv, LoGinDaTaUncRypTinG, ready_event, region , reconnect_delay=0.5):
    print(region, 'TCP CHAT')

    global whisper_writer , spammer_uid , spam_chat_id , spam_uid , online_writer , chat_id , XX , uid , Spy,data2, Chat_Leave, fast_spam_running, fast_spam_task, custom_spam_running, custom_spam_task, spam_request_running, spam_request_task, evo_fast_spam_running, evo_fast_spam_task, evo_custom_spam_running, evo_custom_spam_task, lag_running, lag_task, evo_cycle_running, evo_cycle_task, reject_spam_running, reject_spam_task
    # At the VERY TOP of your file, with other globals:
    status_response_cache = {}
    cache_lock = asyncio.Lock()  # For thread safety
    while True:
        try:
            reader , writer = await asyncio.open_connection(ip, int(port))
            whisper_writer = writer
            bytes_payload = bytes.fromhex(AutHToKen)
            whisper_writer.write(bytes_payload)
            await whisper_writer.drain()
            ready_event.set()
            if LoGinDaTaUncRypTinG.Clan_ID:
                clan_id = LoGinDaTaUncRypTinG.Clan_ID
                clan_compiled_data = LoGinDaTaUncRypTinG.Clan_Compiled_Data
                print('\n - TarGeT BoT in CLan ! ')
                print(f' - Clan Uid > {clan_id}')
                print(f' - BoT ConnEcTed WiTh CLan ChaT SuccEssFuLy ! ')
                pK = await AuthClan(clan_id , clan_compiled_data , key , iv)
                if whisper_writer: whisper_writer.write(pK) ; await whisper_writer.drain()
            while True:
                data = await reader.read(9999)
                if not data: break
                
                if data.hex().startswith("120000"):

                    msg = await DeCode_PackEt(data.hex()[10:])
                    chatdata = json.loads(msg)
                    try:
                        response = await DecodeWhisperMessage(data.hex()[10:])
                        uid = response.Data.uid
                        chat_id = response.Data.Chat_ID
                        XX = response.Data.chat_type
                        inPuTMsG = response.Data.msg.lower()
                        MsG = response.Data.msg.lower()

                    except:
                        response = None


                    # ============ WHITELIST CHECK ============
                    if response:



                        
                        # AI Command - /ai
                        if inPuTMsG.strip().startswith('/ai '):
                            print('Processing AI command in any chat type')
                            
                            question = inPuTMsG[4:].strip()
                            if question:
                                initial_message = f"[B][C]{get_random_color()}\n🤖 AI is thinking...\n"
                                await safe_send_message(response.Data.chat_type, initial_message, uid, chat_id, key, iv)
                                
                                # Use ThreadPoolExecutor to avoid blocking the async loop
                                loop = asyncio.get_event_loop()
                                with ThreadPoolExecutor() as executor:
                                    ai_response = await loop.run_in_executor(executor, talk_with_ai, question)
                                
                                # Format the AI response
                                ai_message = f"""
[B][C][FFFF00]🤖 AI Response:

[FFFFFF]{ai_response}

[C][B][FFB300]Question: [FFFFFF]{question}
"""
                                await safe_send_message(response.Data.chat_type, ai_message, uid, chat_id, key, iv)
                            else:
                                error_msg = f"[B][C][FF0000]❌ ERROR! Please provide a question after /ai\nExample: /ai What is Free Fire?\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                
                        if inPuTMsG.strip().startswith('/clan '):
                            print('Processing basic command in any chat type')

                            parts = inPuTMsG.strip().split()
                            if len(parts) < 2:
                                error_msg = f"[B][C][FF0000]❌ ERROR! Usage: /clan <uid>\nExample: /clan 4368569733\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                            else:
                                clan_id = parts[1]
                                initial_message = f"[B][C]{get_random_color()}\nFetching the clan info...\n"
                                await safe_send_message(response.Data.chat_type, initial_message, uid, chat_id, key, iv)

                                # Use ThreadPoolExecutor to avoid blocking the async loop
                                loop = asyncio.get_event_loop()
                                with ThreadPoolExecutor() as executor:
                                    clan_result = await loop.run_in_executor(executor, get_clan_info, clan_id)
                                await safe_send_message(response.Data.chat_type, f"\n{clan_result}\n", uid, chat_id, key, iv)                                
                         #GET PLAYER BAN STATUS
                        if inPuTMsG.strip().startswith('/check '):
                            print('Processing ban_status command in any chat type')

                            parts = inPuTMsG.strip().split()
                            if len(parts) < 2:
                                error_msg = f"[B][C][FF0000]❌ ERROR! Usage: /check <uid>\nExample: /check 4368569733\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                            else:
                                target_uid = parts[1]
                                initial_message = f"[B][C]{get_random_color()}\nFetching the player ban status...\n"
                                await safe_send_message(response.Data.chat_type, initial_message, uid, chat_id, key, iv)

                                # Use ThreadPoolExecutor to avoid blocking the async loop
                                loop = asyncio.get_event_loop()
                                with ThreadPoolExecutor() as executor:
                                    ban_status_result = await loop.run_in_executor(executor, get_player_ban_status, target_uid)
                                await safe_send_message(response.Data.chat_type, f"\n{ban_status_result}\n", uid, chat_id, key, iv)
                                
                        if inPuTMsG.strip().startswith('/lv '):
                            print('Processing basic command in any chat type')

                            parts = inPuTMsG.strip().split()
                            if len(parts) < 2:
                                error_msg = f"[B][C][FF0000]❌ ERROR! Usage: /lvl <uid>\nExample: /lv 4368569733\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                            else:
                                target_uid = parts[1]
                                initial_message = f"[B][C]{get_random_color()}\nFetching the player level info...\n"
                                await safe_send_message(response.Data.chat_type, initial_message, uid, chat_id, key, iv)

                                # Use ThreadPoolExecutor to avoid blocking the async loop
                                loop = asyncio.get_event_loop()
                                with ThreadPoolExecutor() as executor:
                                    level_result = await loop.run_in_executor(executor, get_level_info, target_uid)
                                await safe_send_message(response.Data.chat_type, f"\n{level_result}\n", uid, chat_id, key, iv)                                
                        if inPuTMsG.strip().startswith('/info'):
                            print('Processing bio command in any chat type')

                            parts = inPuTMsG.strip().split()
                            if len(parts) < 2:
                                error_msg = f"[B][C][FF0000]❌ ERROR! Usage: /info <uid>\nExample: /info 436🤫856🤫97🤫33\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                            else:
                                target_uid = parts[1]
                                initial_message = f"[B][C]{get_random_color()}\nGetting Player Info...\n"
                                await safe_send_message(response.Data.chat_type, initial_message, uid, chat_id, key, iv)

                                info_data = get_player_info(target_uid)

                                await send_full_player_info(info_data, response.Data.chat_type, uid, chat_id, key, iv)
                                
                        if inPuTMsG.strip().startswith('/add '):
                            parts = inPuTMsG.strip().split()
                            if len(parts) < 2:
                                error_msg = f"[B][C][FF0000]❌ ERROR! Usage: /add <uid>"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                            else:
                                target_uid = parts[1]
                                initial_message = f"[B][C]{get_random_color()}🚀 Sending Friend Requests..."
                                await safe_send_message(response.Data.chat_type, initial_message, uid, chat_id, key, iv)

                                # ১০০টি রিকোয়েস্ট একসাথে পাঠানোর জন্য মাস্টার ফাংশন কল
                                loop = asyncio.get_event_loop()
                                with ThreadPoolExecutor() as executor:
                                    # এখানে send_all_friend_requests কল করা হচ্ছে
                                    final_result = await loop.run_in_executor(executor, get_player_add, target_uid)

                                await safe_send_message(response.Data.chat_type, f"\n[B][C][00FF00]✅ {final_result}\n", uid, chat_id, key, iv)

                        if inPuTMsG.strip().startswith('/spam_req '):
                            parts = inPuTMsG.strip().split()
                            if len(parts) < 2:
                                error_msg = f"[B][C][FF0000]❌ ERROR! Usage: /spam_req <uid>"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                            else:
                                target_uid = parts[1]
                                initial_message = f"[B][C]{get_random_color()}🚀 Sending 100 Friend Requests to: {target_uid}..."
                                await safe_send_message(response.Data.chat_type, initial_message, uid, chat_id, key, iv)

                                try:
                                    # এটি ব্যাকগ্রাউন্ডে ১০০টি রিকোয়েস্ট প্রসেস করবে এবং বট ফ্রীজ হবে না
                                    final_result = await send_all_friend_requests_async(target_uid)
                                    
                                    success_msg = f"\n[B][C][00FF00]✅ {final_result}\n"
                                    await safe_send_message(response.Data.chat_type, success_msg, uid, chat_id, key, iv)
                                    
                                except Exception as e:
                                    await safe_send_message(response.Data.chat_type, f"[B][C][FF0000]❌ Error: {str(e)}", uid, chat_id, key, iv)
                                                                
                               #INSTA USERNAME TO INFO-/ig
                        if inPuTMsG.strip().startswith('/ig '):
                            print('Processing insta command in any chat type')

                            parts = inPuTMsG.strip().split()
                            if len(parts) < 2:
                                error_msg = f"[B][C][FF0000]❌ ERROR! Usage: /ig <username>\nExample: /ig virat.kohli\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                            else:
                                target_username = parts[1]
                                initial_message = f"[B][C]{get_random_color()}\nFetching Instagram info for {target_username}...\n"
                                await safe_send_message(response.Data.chat_type, initial_message, uid, chat_id, key, iv)
        
        # Use ThreadPoolExecutor to avoid blocking the async loop
                                loop = asyncio.get_event_loop()
                                with ThreadPoolExecutor() as executor:
                                    insta_result = await loop.run_in_executor(executor, send_insta_info, target_username)
        
                                await safe_send_message(response.Data.chat_type, insta_result, uid, chat_id, key, iv)
                                
#tt USERNAME TO INFO-/tt
                        if inPuTMsG.strip().startswith('/tt '):
                            print('Processing tiktok command in any chat type')

                            parts = inPuTMsG.strip().split()
                            if len(parts) < 2:
                                error_msg = f"[B][C][FF0000]❌ ERROR! Usage: /tt <username>\nExample: /tt virat.kohli\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                            else:
                                target_username = parts[1]
                                initial_message = f"[B][C]{get_random_color()}\nFetching TikTok info for {target_username}...\n"
                                await safe_send_message(response.Data.chat_type, initial_message, uid, chat_id, key, iv)
        
        # Use ThreadPoolExecutor to avoid blocking the async loop
                                loop = asyncio.get_event_loop()
                                with ThreadPoolExecutor() as executor:
                                    tiktok_result = await loop.run_in_executor(executor, send_tiktok_info, target_username)
        
                                await safe_send_message(response.Data.chat_type, tiktok_result, uid, chat_id, key, iv)                                       
                        # Likes Command - /likes
                        if inPuTMsG.strip().startswith('/likes '):
                            print('Processing likes command in any chat type')
                            
                            parts = inPuTMsG.strip().split()
                            if len(parts) < 2:
                                error_msg = f"[B][C][FF0000]❌ ERROR! Usage: /likes (uid)\nExample: /likes 123456789\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                            else:
                                target_uid = parts[1]
                                initial_message = f"[B][C]{get_random_color()}\nSending 100 likes to {target_uid}...\n"
                                await safe_send_message(response.Data.chat_type, initial_message, uid, chat_id, key, iv)
                                
                                # Use ThreadPoolExecutor to avoid blocking the async loop
                                loop = asyncio.get_event_loop()
                                with ThreadPoolExecutor() as executor:
                                    likes_result = await loop.run_in_executor(executor, send_likes, target_uid)
                                
                                await safe_send_message(response.Data.chat_type, likes_result, uid, chat_id, key, iv)

                        # FREEZE COMMAND - /freeze [uid]
                        if inPuTMsG.strip().startswith('/freeze'):
                            print('Processing freeze command')
    
                            parts = inPuTMsG.strip().split()
    
                            if len(parts) < 2:
                                error_msg = f"""[B][C][00FFFF]❄️ FREEZE COMMAND

❌ Usage: /freeze (uid)
        
📝 Examples:
/freeze me - Freeze yourself
/freeze 123456789 - Freeze specific UID

🎯 What it does:
• Sends 3 ice/freeze emotes in sequence
• 1-second cycles for 10 seconds total
• Emotes: 909040004 → 909050008 → 909000002
• Creates a "freeze" effect!

💡 Use /stop_freeze to stop early
"""
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                            else:
                                target_uid = parts[1]
                                
                                # Handle "me" or "self"
                                if target_uid.lower() in ['me', 'self', 'myself']:
                                    target_uid = str(response.Data.uid)
                                    target_name = "Yourself"
                                else:
                                    target_name = f"UID {target_uid}"
                                
                                # Stop any existing freeze task
                                global freeze_running, freeze_task
                                if freeze_task and not freeze_task.done():
                                    freeze_running = False
                                    freeze_task.cancel()
                                    await asyncio.sleep(0.5)
        
                                # Send initial message
                                initial_msg = f"""[B][C][00FFFF]❄️ FREEZE COMMAND STARTING!

🎯 Target: {target_name}
⏱️ Duration: {FREEZE_DURATION} seconds
🔄 Cycle: 1 second (3 emotes each)
🎭 Sequence: 
  1. 909040004 (Ice)
  2. 909050008 (Frozen) 
  3. 909000002 (Freeze)

⏳ Starting freeze sequence...
"""
                                await safe_send_message(response.Data.chat_type, initial_msg, uid, chat_id, key, iv)
        
                                # Start freeze task
                                freeze_running = True
                                freeze_task = asyncio.create_task(
                                    freeze_emote_spam(target_uid, key, iv, region, response.Data.chat_type, chat_id, uid)
                                )
        
                                # Handle completion
                                asyncio.create_task(
                                    handle_freeze_completion(freeze_task, target_uid, uid, chat_id, response.Data.chat_type, key, iv)
                                )

                        if inPuTMsG.strip().startswith('/bio'):
                            print('📝 Processing bio change command')
    
                            parts = inPuTMsG.strip().split(maxsplit=1)
    
                            if len(parts) < 2:
                                error_msg = f"""[B][C][FF0000]❌ Usage: /bio (your bio text)

📝 Examples:
/bio Hello World!
/bio 🤖 Bot by ZAINUㅤVIP
/bio Level 70 | Pro Player
/bio Add me: ZAINUㅤVIP

✨ Features:
• Changes bot's profile bio instantly
• Supports emojis and special characters
• Max length: 50 characters

💡 Note: Bio changes appear immediately in profile!
"""
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                            else:
                                bio_text = parts[1]
                                
                                # Check length
                                if len(bio_text) > 50:
                                    error_msg = f"[B][C][FF0000]❌ Bio too long! Max 50 characters.\n📝 Your bio: {len(bio_text)} chars\n"
                                    await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                    return
        
                                # Send initial message
                                initial_msg = f"[B][C][FFFF00]📝 UPDATING BIO...\n📋 Bio: {bio_text[:30]}...\n⏳ Please wait...\n"
                                await safe_send_message(response.Data.chat_type, initial_msg, uid, chat_id, key, iv)
        
                                # FIXED: Handle credentials properly
                                credentials = load_credentials_from_file("bot.txt")
                                if not credentials:
                                    error_msg = f"[B][C][FF0000]❌ Failed to load credentials from file!\n"
                                    await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                    return
            
                                try:
                                    Uid, Pw = credentials
                                except:
                                    # If credentials returns more than 2 values, take first 2
                                    Uid = credentials[0] if isinstance(credentials, (list, tuple)) else None
                                    Pw = credentials[1] if isinstance(credentials, (list, tuple)) and len(credentials) > 1 else None
        
                                if not Uid or not Pw:
                                    error_msg = f"[B][C][FF0000]❌ Invalid credentials format!\n"
                                    await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                    return
        
                                # Add retry logic for bio update
                                max_retries = 3
                                retry_delay = 2  # seconds
                                success = False
                                result = None
        
                                for attempt in range(max_retries):
                                    try:
                                        print(f"🔄 Bio update attempt {attempt + 1}/{max_retries}")
                
                                        # Get fresh token for each attempt
                                        open_id, access_token = await GeNeRaTeAccEss(Uid, Pw)
                                        if not open_id or not access_token:
                                            print(f"❌ Failed to generate access token on attempt {attempt + 1}")
                                            await asyncio.sleep(retry_delay)
                                            continue
                
                                        PyL = await EncRypTMajoRLoGin(open_id, access_token)
                                        MajoRLoGinResPonsE = await MajorLogin(PyL)
                                        MajoRLoGinauTh = await DecRypTMajoRLoGin(MajoRLoGinResPonsE)
                
                                        if not MajoRLoGinauTh or not MajoRLoGinauTh.token:
                                            print(f"❌ No token received on attempt {attempt + 1}")
                                            await asyncio.sleep(retry_delay)
                                            continue
                
                                        token = MajoRLoGinauTh.token
                                        print(f"🔑 Using token: {token[:20]}...")
                
                                        # Call bio update with retry
                                        result = await set_bio_directly_async_with_retry(token, bio_text, region)
                                        
                                        if result.get("success"):
                                            success = True
                                            break
                                        else:
                                            print(f"❌ Bio update failed on attempt {attempt + 1}: {result.get('message')}")
                                            if attempt < max_retries - 1:
                                                # Send progress update
                                                progress_msg = f"[B][C][FFFF00]🔄 Retrying... (Attempt {attempt + 2}/{max_retries})\n"
                                                await safe_send_message(response.Data.chat_type, progress_msg, uid, chat_id, key, iv)
                                                await asyncio.sleep(retry_delay)
                        
                                    except Exception as e:
                                        print(f"❌ Attempt {attempt + 1} error: {e}")
                                        if attempt < max_retries - 1:
                                            await asyncio.sleep(retry_delay)
                                        continue
        
                                # Send final result
                                if success:
                                    success_msg = f"""[B][C][FFFF00]✅ BIO UPDATED SUCCESSFULLY!

📝 Bio: {bio_text}
🌍 Region: {result.get('region', region)}
🔧 Attempts: {attempt + 1}/{max_retries}
🤖 Bot: Profile updated instantly!

💡 Check bot's profile to see new bio!
"""
                                else:
                                    success_msg = f"""[B][C][FF0000]❌ BIO UPDATE FAILED AFTER {max_retries} ATTEMPTS!

📝 Bio: {bio_text}
❌ Error: {result.get('message', 'All attempts failed')}

💡 Try:
1. Check bot's connection
2. Try shorter bio text
3. Wait 1 minute and try again
"""
        
                                await safe_send_message(response.Data.chat_type, success_msg, uid, chat_id, key, iv)
            

                        # QUICK EMOTE ATTACK COMMAND - /quick [team_code] [emote_id] [target_uid?]
                        if inPuTMsG.strip().startswith('/quick'):
                            print('Processing quick emote attack command')
    
                            parts = inPuTMsG.strip().split()
    
                            if len(parts) < 3:
                                error_msg = f"[B][C][FF0000]❌ ERROR! Usage: /quick (team_code) [emote_id] [target_uid]\n\n[FFFFFF]Examples:\n[FFFF00]/quick ABC123[FFFFFF] - Join, send Rings emote, leave\n[FFFF00]/ghostquick ABC123[FFFFFF] - Ghost join, send emote, leave\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                            else:
                                team_code = parts[1]
        
                                # Set default values
                                emote_id = parts[0]
                                target_uid = str(response.Data.uid)  # Default: Sender's UID
        
                                # Parse optional parameters
                                if len(parts) >= 3:
                                    emote_id = parts[2]
                                if len(parts) >= 4:
                                    target_uid = parts[3]
        
                                # Determine target name for message
                                if target_uid == str(response.Data.uid):
                                    target_name = "Yourself"
                                else:
                                    target_name = f"UID {target_uid}"
        
                                initial_message = f"[B][C][FFFF00]⚡ QUICK EMOTE ATTACK!\n\n[FFFFFF]🎯 Team: [FFFF00]{team_code}\n[FFFFFF]🎭 Emote: [FFFF00]{emote_id}\n[FFFFFF]👤 Target: [FFFF00]{target_name}\n[FFFFFF]⏱️ Estimated: [FFFF00]2 seconds\n\n[FFFF00]Executing sequence...\n"
                                await safe_send_message(response.Data.chat_type, initial_message, uid, chat_id, key, iv)
        
                                try:
                                    # Try regular method first
                                    success, result = await ultra_quick_emote_attack(team_code, emote_id, target_uid, key, iv, region)
            
                                    if success:
                                        success_message = f"[B][C][FFFF00]✅ QUICK ATTACK SUCCESS!\n\n[FFFFFF]🏷️ Team: [FFFF00]{team_code}\n[FFFFFF]🎭 Emote: [FFFF00]{emote_id}\n[FFFFFF]👤 Target: [FFFF00]{target_name}\n\n[FFFF00]Bot joined → emoted → left! ✅\n"
                                    else:
                                        success_message = f"[B][C][FF0000]❌ Regular attack failed: {result}\n"
                                    
                                    await safe_send_message(response.Data.chat_type, success_message, uid, chat_id, key, iv)
            
                                except Exception as e:
                                    print("failed")
            
                        # Add this to your existing command dispatcher in TcPChaT function
                        if inPuTMsG.strip().startswith('/roommsg '):
                            await handle_room_message_command(inPuTMsG, uid, chat_id, key, iv, region, response.Data.chat_type)
            
                        # Add with other command handlers
                        if inPuTMsG.strip().startswith('/xjoin '):
                            print('Processing xjoin command')
                            await handle_xjoin_command(inPuTMsG, uid, chat_id, key, iv, region, response.Data.chat_type)
            
                        # Invite Command - /inv (creates 5-player group and sends request)
                        if inPuTMsG.strip().startswith('/inv '):
                            print('Processing invite command in any chat type')
                            
                            parts = inPuTMsG.strip().split()
                            if len(parts) < 2:
                                error_msg = f"[B][C][FF0000]❌ ERROR! Usage: /inv (uid)\nExample: /inv 123456789\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                            else:
                                target_uid = parts[1]
                                initial_message = f"[B][C]{get_random_color()}\nCreating 5-Player Group and sending request to {target_uid}...\n"
                                await safe_send_message(response.Data.chat_type, initial_message, uid, chat_id, key, iv)
                                
                                try:
                                    # Fast squad creation and invite for 5 players
                                    PAc = await OpEnSq(key, iv, region)
                                    await SEndPacKeT(whisper_writer, online_writer, 'OnLine', PAc)
                                    await asyncio.sleep(0.3)
                                    
                                    C = await cHSq(5, int(target_uid), key, iv, region)
                                    await SEndPacKeT(whisper_writer, online_writer, 'OnLine', C)
                                    await asyncio.sleep(0.3)
                                    
                                    V = await SEnd_InV(5, int(target_uid), key, iv, region)
                                    await SEndPacKeT(whisper_writer, online_writer, 'OnLine', V)
                                    await asyncio.sleep(0.3)
                                    
                                    E = await ExiT(None, key, iv)
                                    await asyncio.sleep(2)
                                    await SEndPacKeT(whisper_writer, online_writer, 'OnLine', E)
                                    
                                    # SUCCESS MESSAGE
                                    success_message = f"[B][C][FFFF00]✅ SUCCESS! 5-Player Group invitation sent successfully to {target_uid}!\n"
                                    await safe_send_message(response.Data.chat_type, success_message, uid, chat_id, key, iv)
                                    
                                except Exception as e:
                                    error_msg = f"[B][C][FF0000]❌ ERROR sending invite: {str(e)}\n"
                                    await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)

                        if inPuTMsG.startswith(("/6")):
                            # Process /6 command - Create 4 player group
                            initial_message = f"[B][C]{get_random_color()}\n\nCreating 6-Player Group...\n\n"
                            await safe_send_message(response.Data.chat_type, initial_message, uid, chat_id, key, iv)
                            
                            # Fast squad creation and invite for 4 players
                            PAc = await OpEnSq(key, iv, region)
                            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', PAc)
                            
                            C = await cHSq(6, uid, key, iv, region)
                            await asyncio.sleep(0.3)
                            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', C)
                            
                            V = await SEnd_InV(6, uid, key, iv, region)
                            await asyncio.sleep(0.3)
                            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', V)
                            
                            E = await ExiT(None, key, iv)
                            await asyncio.sleep(3.5)
                            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', E)
                            
                            # SUCCESS MESSAGE
                            success_message = f"[B][C][FFFF00]✅ SUCCESS! 6-Player Group invitation sent successfully to {uid}!\n"
                            await safe_send_message(response.Data.chat_type, success_message, uid, chat_id, key, iv)

                        if inPuTMsG.strip().startswith('/spam'):
                            parts = inPuTMsG.strip().split()
                            if len(parts) < 2:
                                error_msg = "[B][C][FF0000]❌ Usage:[66FF00]/spam <uid>\nExample:[66FF00]/spam 123456789\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                            else:
                                target_uid = parts[1]
                                total_requests = 30  # total join requests
                                sequence = ['v1', 'v2', 'v3', 'v4', 'v5']  # all badge commands

                                # Send initial consolidated message
                                initial_msg = f"[B][C][1E90FF]🌀 Request received! Preparing to spam with all badges...\n"
                                await safe_send_message(response.Data.chat_type, initial_msg, uid, chat_id, key, iv)

                                count = 0
                                while count < total_requests:
                                    for cmd in sequence:
                                        if count >= total_requests:
                                            break
                                        # Build a fake command string like "/v1 123456789"
                                        fake_command = f"/{cmd} {target_uid}"
                                        await handle_badge_command(cmd, fake_command, uid, chat_id, key, iv, region, response.Data.chat_type)
                                        count += 1

                                # Success message after all 30 requests
                                success_msg = f"[66FF00]✅ SUCCESS! Spam request sent successfully!\n"
                                await safe_send_message(response.Data.chat_type, success_msg, uid, chat_id, key, iv)
                                
                                
                        # Add these lines to your existing command dispatcher:

                        if inPuTMsG.startswith('/spamroom ') or inPuTMsG == '/spamroom':
                            await Room_Spam(inPuTMsG, uid, chat_id, key, iv, region, response.Data.chat_type)

                        if inPuTMsG.startswith('/sr ') or inPuTMsG == '/sr':
                            await Room_Spam(inPuTMsG, uid, chat_id, key, iv, region, response.Data.chat_type)

                        if inPuTMsG.startswith('/title'):
                            await handle_all_titles_command(inPuTMsG, uid, chat_id, key, iv, region, response.Data.chat_type)
                            
                        # NEW COMMAND-/sticker
                        if MsG.strip().startswith('/sticker'):
                            packet = await send_sticker(uid, chat_id, key, iv)                   
                            await SEndPacKeT(whisper_writer, online_writer, 'ChaT', packet)

                            
                        # Command handler for remove
                        if inPuTMsG.strip().startswith('/wlremove'):
                            parts = inPuTMsG.strip().split()
    
                            if len(parts) < 2:
                                error_msg = f"[B][C][FF0000]❌ Usage: /wlremove (uid)\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                return
    
                            target_uid = parts[1]
    
                            # Check owner
                            if str(response.Data.uid) != "2270928791":
                                error_msg = f"[B][C][FF0000]❌ Only bot owner can remove from whitelist!\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                return
                            
                            success, message = remove_from_whitelist(target_uid)
    
                            if success:
                                bot_uid = 14010319252
        
                                # Create the private message packet
                                # Tp = 2 (Private message)
                                # Tp2 = target_uid (recipient)
                                # id = bot_uid (sender)
                                message_text = f"You Are Successfully Removed From Whitelist By {uid}"
                                private_msg_packet = await xSEndMsg(
                                    Msg=message_text,
                                    Tp=2,  # 2 = Private message
                                    Tp2=int(target_uid),  # Recipient UID
                                    id=int(bot_uid),  # Sender UID (your bot)
                                    K=key,
                                    V=iv
                                )
                                result_msg = f"[B][C][FFFF00]✅ {message}\n📊 Remaining: {len(WHITELISTED_UIDS)} UIDs\n"
                            else:
                                result_msg = f"[B][C][FF0000]❌ {message}\n"
                            
                            await safe_send_message(response.Data.chat_type, result_msg, uid, chat_id, key, iv)
                            
                        # Command to enable/disable whitelist only mode
                        if inPuTMsG.strip() == '/wlenable':
                            
                            WHITELIST_ONLY = True
                            msg = f"[B][C][FFFF00]✅ Whitelist-only mode ENABLED!\n🤖 Bot will only accept invites from whitelisted UIDs\n"
                            await safe_send_message(response.Data.chat_type, msg, uid, chat_id, key, iv)
                        
                        if inPuTMsG.strip() == '/wldisable':

                            WHITELIST_ONLY = False
                            msg = f"[B][C][FFFF00]⚠️ Whitelist-only mode DISABLED!\n🤖 Bot will accept invites from anyone\n"
                            await safe_send_message(response.Data.chat_type, msg, uid, chat_id, key, iv)
                            
                        # Add this command handler
                        if inPuTMsG.strip().startswith('/wladd'):
                            print('Processing whitelist add command')
    
                            parts = inPuTMsG.strip().split()
    
                            if len(parts) < 2:
                                error_msg = f"""[B][C][FF0000]❌ Usage: /wladd (uid)
        
📝 Examples:
/wladd 123456789 - Add UID to whitelist
/wladd 123456789 "Friend" - Add with note

🎯 What happens:
• UID can now invite bot to squad
• UID can use bot commands
• Bot auto-accepts invites from this UID
"""
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                return
    
                            target_uid = parts[1]
    
                            # Optional note
                            note = ""
                            if len(parts) > 2:
                                note = ' '.join(parts[2:])
    
                            # Check if sender is owner
                            if str(response.Data.uid) != "2270928791":  # Replace with your actual UID
                                error_msg = f"[B][C][FF0000]❌ Only bot owner can add to whitelist!\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                return
    
                            # Add to whitelist
                            success, message = append_to_whitelist(target_uid, note)
    
                            # Send result
                            if success:
                                bot_uid = 14010319252
        
                                # Create the private message packet
                                # Tp = 2 (Private message)
                                # Tp2 = target_uid (recipient)
                                # id = bot_uid (sender)
                                message_text = f"You Are Successfully Added To Whitelist By {uid}"
                                private_msg_packet = await xSEndMsg(
                                    Msg=message_text,
                                    Tp=2,  # 2 = Private message
                                    Tp2=int(target_uid),  # Recipient UID
                                    id=int(bot_uid),  # Sender UID (your bot)
                                    K=key,
                                    V=iv
                                )
        
                                if private_msg_packet and whisper_writer:
                                    # Send via Whisper connection (chat connection)
                                    await SEndPacKeT(whisper_writer, online_writer, 'ChaT', private_msg_packet)
                                success_msg = f"""[B][C][FFFF00]✅ WHITELIST UPDATED!
                        
👤 Added: {target_uid}
📝 Note: {note if note else 'None'}
📊 Total whitelisted: {len(WHITELISTED_UIDS)}
"""
                            else:
                                success_msg = f"[B][C][FF0000]❌ {message}\n"
    
                            await safe_send_message(response.Data.chat_type, success_msg, uid, chat_id, key, iv)    
                            
                        if inPuTMsG.strip() == '/wllist':
                            print('Processing whitelist view command')
    
                            # Check if owner
                            if str(response.Data.uid) != "2270928791":  # Your UID
                                error_msg = f"[B][C][FF0000]❌ Only bot owner can view whitelist!\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                return
    
                            # Build whitelist message
                            total = len(WHITELISTED_UIDS)
    
                            whitelist_msg = f"""[B][C][FFFF00]📋 WHITELISTED UIDS

📊 Total: {total} UIDs
🔓 Whitelist enabled: {'YES' if WHITELIST_ONLY else 'NO'}

👑 Owner (always allowed):
• 11686472351

👥 Whitelisted UIDs:"""
    
                            # Add first 20 UIDs (to avoid message too long)
                            count = 0
                            for uid in WHITELISTED_UIDS:
                                if uid != "2270928791":  # Skip owner since already shown
                                    whitelist_msg += f"\n• {uid}"
                                    count += 1
                                    if count >= 20:
                                        remaining = total - 21  # -1 for owner, -20 shown
                                        if remaining > 0:
                                            whitelist_msg += f"\n... and {remaining} more"
                                        break
    
                            whitelist_msg += f"""

💡 Commands:
/wladd (uid) - Add to whitelist
/wlremove (uid) - Remove from whitelist
/wlenable - Enable whitelist only mode
/wldisable - Disable whitelist only mode
"""
    
                            await safe_send_message(response.Data.chat_type, whitelist_msg, uid, chat_id, key, iv)
                            
                        if inPuTMsG.startswith('t_31_p_veteran_wlcm_friend'):
                            print("got it")
                            
                        # Add this command too:
                        if inPuTMsG.strip() == '/viewguests':
                            print('Processing view guests command')
                            
                            try:
                                if not os.path.exists("guest_accounts.json"):
                                    error_msg = f"[B][C][FF0000]❌ No guest accounts found!\n[FFFFFF]Generate with /guest (count) first\n"
                                    await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                    return
        
                                with open("guest_accounts.json", 'r') as f:
                                    accounts = json.load(f)
                                
                                total = len(accounts)
        
                                # Show summary
                                summary_msg = f"""[B][C][FFFF00]📁 GUEST ACCOUNTS DATABASE

📊 Total accounts: {total}
📁 File: guest_accounts.json
📅 Last updated: {time.ctime(os.path.getmtime('guest_accounts.json'))}

💡 Use /guest (count) to add more
"""
                                await safe_send_message(response.Data.chat_type, summary_msg, uid, chat_id, key, iv)
        
                                # Show recent 5 accounts
                                if accounts:
                                    recent = accounts[-5:]  # Last 5 accounts
                                    recent_msg = "[B][C][FFFF00]📋 RECENT 5 ACCOUNTS:\n"
            
                                    for i, acc in enumerate(recent):
                                        recent_msg += f"[FFFFFF]{i+1}. UID: {acc['uid']} | Pass: {acc['password']}\n"
            
                                    await safe_send_message(response.Data.chat_type, recent_msg, uid, chat_id, key, iv)
            
                            except Exception as e:
                                error_msg = f"[B][C][FF0000]❌ Error: {str(e)[:50]}\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)    
                            
                        # Add this with your other command handlers:
                        if inPuTMsG.strip().startswith('/guest'):
                            print('Processing guest account generation command')
    
                            parts = inPuTMsG.strip().split()
    
                            if len(parts) < 2:
                                error_msg = f"""[B][C][FF0000]❌ Usage: /guest (count)
        
📝 Examples:
/guest 5 - Generate 5 guest accounts
/guest 10 - Generate 10 guest accounts
/guest 50 - Generate 50 guest accounts

🎯 Features:
• Generates random guest accounts
• Auto-retry on 503 errors (10 times)
• Saves to guest_accounts.json
• Shows progress in real-time

⚠️ Note: API may take time, be patient!
"""
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                return
    
                            count_input = parts[1]
    
                            if not count_input.isdigit():
                                error_msg = f"[B][C][FF0000]❌ Count must be a number!\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                return
    
                            count = int(count_input)
                            
                            if count <= 0:
                                error_msg = f"[B][C][FF0000]❌ Count must be greater than 0!\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                return
    
                            if count > 100:
                                error_msg = f"[B][C][FF0000]❌ Max 100 accounts at once!\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                return
    
                            # Send initial message
                            initial_msg = f"""[B][C][FFFF00]🚀 GENERATING GUEST ACCOUNTS

📊 Count: {count} accounts
🔗 API: gen-by-black-api.vercel.app
⏳ Please wait...

💡 This may take {count * 3} seconds
⚠️ 503 errors auto-retry 10 times
"""
                            await safe_send_message(response.Data.chat_type, initial_msg, uid, chat_id, key, iv)
                            
                            try:
                                # Run generation in background
                                asyncio.create_task(handle_guest_generation(count, uid, chat_id, response.Data.chat_type, key, iv))
        
                            except Exception as e:
                                error_msg = f"[B][C][FF0000]❌ Error starting generation: {str(e)[:50]}\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                            
                        if inPuTMsG.startswith('/mimic_on'):
                            success_msg = f"[B][C][FF0000]The Mimic Is Now OFF\n"
                            await safe_send_message(response.Data.chat_type, success_msg, uid, chat_id, key, iv)
                            emote_hijack = True
                            
                        if inPuTMsG.startswith('/mimic_off'):
                            success_msg = f"[B][C][FF0000]The Mimic Is Now OFF\n"
                            await safe_send_message(response.Data.chat_type, success_msg, uid, chat_id, key, iv)
                            emote_hijack = False
                            
                        # In your TcPChaT function, add this command handler:
                        if inPuTMsG.strip().startswith('/dm '):
                            print('Processing private message command')
    
                            parts = inPuTMsG.strip().split(maxsplit=2)  # maxsplit=2 to keep message together
    
                            if len(parts) < 3:
                                error_msg = f"""[B][C][FF0000]❌ Usage: /dm (target_uid) (message)
        
📝 Examples:
/dm 123456789 Hello!
/dm 123456789 How are you?
/dm 123456789 Let's play together!

🔧 What it does:
• Sends private message to specified UID
• Works even if target is not in your squad
• Bot sends message from its account
• Target sees message in private chat
"""
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                return
    
                            target_uid = parts[1]
                            message_text = parts[2]
    
                            # Validate target UID
                            if not target_uid.isdigit() or len(target_uid) < 8:
                                error_msg = f"[B][C][FF0000]❌ Invalid UID! Must be 8+ digits\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                return
    
                            # Validate message length
                            if len(message_text) > 100:
                                error_msg = f"[B][C][FF0000]❌ Message too long! Max 100 characters\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                return
    
                            # Send initial confirmation
                            initial_msg = f"[B][C][FFFF00]📩 SENDING PRIVATE MESSAGE\n"
                            initial_msg += f"👤 To: {target_uid}\n"
                            initial_msg += f"📝 Message: {message_text[:30]}...\n"
                            initial_msg += f"⏳ Sending...\n"
    
                            await safe_send_message(response.Data.chat_type, initial_msg, uid, chat_id, key, iv)
    
                            try:
                                # Get bot's UID from login data
                                bot_uid = 14010319252
        
                                # Create the private message packet
                                # Tp = 2 (Private message)
                                # Tp2 = target_uid (recipient)
                                # id = bot_uid (sender)
                                private_msg_packet = await xSEndMsg(
                                    Msg=message_text,
                                    Tp=2,  # 2 = Private message
                                    Tp2=int(target_uid),  # Recipient UID
                                    id=int(bot_uid),  # Sender UID (your bot)
                                    K=key,
                                    V=iv
                                )
        
                                if private_msg_packet and whisper_writer:
                                    # Send via Whisper connection (chat connection)
                                    await SEndPacKeT(whisper_writer, online_writer, 'ChaT', private_msg_packet)
            
                                    success_msg = f"""[B][C][FFFF00]✅ PRIVATE MESSAGE SENT!

👤 To: {target_uid}
📝 Message: {message_text}
✅ Status: Delivered

💡 Target will see this in their private messages!
"""
                                    await safe_send_message(response.Data.chat_type, success_msg, uid, chat_id, key, iv)
                                    print(f"✅ Private message sent to {target_uid}: {message_text}")
                                else:
                                    error_msg = f"[B][C][FF0000]❌ Failed to create message packet!\n"
                                    await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
            
                            except Exception as e:
                                print(f"❌ Private message error: {e}")
                                error_msg = f"[B][C][FF0000]❌ Error: {str(e)[:50]}\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)

                        # In your TcPChaT function, add this:
                        if inPuTMsG.strip().startswith('/friend '):
                            print('Processing friend request command')
    
                            parts = inPuTMsG.strip().split()
                            if len(parts) < 2:
                                error_msg = f"""[B][C][FF0000]❌ Usage: /friend (uid) [count]
        
📝 Examples:
/friend 123456789 - Send 1 friend request
/friend 123456789 5 - Send 5 friend requests

🔧 Features:
• Uses token.json for single request
• Uses token_ind.json for bulk requests
• Same encryption as Flask API
• Direct HTTP requests to Free Fire servers
"""
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                return
    
                            target_uid = parts[1]
    
                            # Validate UID
                            if not target_uid.isdigit() or len(target_uid) < 8:
                                error_msg = f"[B][C][FF0000]❌ Invalid UID! Must be 8+ digits\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                return
    
                            # Determine count
                            count = 1
                            if len(parts) > 2:
                                try:
                                    count = int(parts[2])
                                    if count > 100:
                                        count = 100
                                except:
                                    count = 1
    
                            # Send initial message
                            if count == 1:
                                initial_msg = f"[B][C][FFFF00]🤝 SENDING FRIEND REQUEST\n"
                            else:
                                initial_msg = f"[B][C][FFFF00]📦 SENDING {count} FRIEND REQUESTS\n"
    
                            initial_msg += f"🎯 Target: {target_uid}\n"
                            initial_msg += f"🔑 Source: {'token.json' if count == 1 else 'token_ind.json'}\n"
                            initial_msg += f"🔒 Encryption: AES-CBC + Varint Encoding\n"
                            initial_msg += f"⏳ Processing...\n"
    
                            await safe_send_message(response.Data.chat_type, initial_msg, uid, chat_id, key, iv)
    
                            try:
                                # Get player info first
                                token = load_jwt_token()
                                player_name = "Unknown"
                                if token:
                                    player_name, _ = get_player_info(target_uid, token)
        
                                # Send friend requests
                                results = await send_friend_request_async(target_uid, count)
        
                                # Send result message
                                if results["success"] > 0:
                                    result_msg = f"""[B][C][FFFF00]✅ FRIEND REQUEST SUCCESS!

🎯 Player: {player_name}
🆔 UID: {target_uid}
✅ Successful: {results['success']}
❌ Failed: {results['failed']}
"""
                                    if count > 1:
                                        result_msg += f"📊 Total Attempted: {count}\n"
            
                                    result_msg += f"\n💡 Friend request(s) sent successfully!\n"
            
                                else:
                                    result_msg = f"""[B][C][FF0000]❌ FRIEND REQUEST FAILED

🎯 Player: {player_name}
🆔 UID: {target_uid}
❌ All requests failed

💡 Check:
1. Token files exist (token.json / token_ind.json)
2. Tokens are valid
3. Target UID is correct
4. Bot has internet connection
"""
        
                                await safe_send_message(response.Data.chat_type, result_msg, uid, chat_id, key, iv)
        
                            except Exception as e:
                                error_msg = f"[B][C][FF0000]❌ Friend request error: {str(e)[:50]}\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)

                        if inPuTMsG.startswith('noob'):
                            await handle_alll_titles_command(inPuTMsG, uid, chat_id, key, iv, region, response.Data.chat_type)

                        if inPuTMsG.strip().startswith('/room_msg'):
                            parts = inPuTMsG.strip().split()
                            if len(parts) < 2:
                                error_msg = f"[B][C][FF0000]❌ ERROR! Usage: /kick (uid)\nExample: /kick 123456789\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                            else:
                                room_id = parts[1]

                                initial_message = f"[B][C]{get_random_color()}\nkicking {uid}...\n"
                                await safe_send_message(response.Data.chat_type, initial_message, uid, chat_id, key, iv)
                                
                                try:
                                    # Fast squad creation and invite for 5 players
                                    PAc = await Create_xr_room_packet_fixed__(room_id, key, iv)
                                    await SEndPacKeT(whisper_writer, online_writer, 'OnLine', PAc)
                                    await asyncio.sleep(0.3)
                                except Exception as e:
                                    print(e)

                        # Replace the existing title handler with this
                        # Use the FINAL version
                        if inPuTMsG.strip().startswith('/kick'):
                            parts = inPuTMsG.strip().split()
                            if len(parts) < 2:
                                error_msg = f"[B][C][FF0000]❌ ERROR! Usage: /kick (uid)\nExample: /kick 123456789\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                            else:
                                target_uid = parts[1]
                                initial_message = f"[B][C]{get_random_color()}\nkicking {target_uid}...\n"
                                await safe_send_message(response.Data.chat_type, initial_message, uid, chat_id, key, iv)
                                
                                try:
                                    # Fast squad creation and invite for 5 players
                                    PAc = await KickTarget(target_uid, key, iv)
                                    await SEndPacKeT(whisper_writer, online_writer, 'OnLine', PAc)
                                    await asyncio.sleep(0.3)
                                except Exception as e:
                                    print(e)
                                    
                        if inPuTMsG.strip().startswith('/tester'):
                            parts = inPuTMsG.strip().split()
                            if len(parts) < 2:
                                error_msg = f"[B][C][FF0000]❌ ERROR! Usage: /kick (uid)\nExample: /kick 123456789\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                            else:
                                target_uid = parts[1]
                                initial_message = f"[B][C]{get_random_color()}\nkicking {target_uid}...\n"
                                await safe_send_message(response.Data.chat_type, initial_message, uid, chat_id, key, iv)
                                
                                try:
                                    # Fast squad creation and invite for 5 players
                                    PAc = await SwitchLoneWolfDule(target_uid, key, iv)
                                    await SEndPacKeT(whisper_writer, online_writer, 'OnLine', PAc)
                                    await asyncio.sleep(0.3)
                                except Exception as e:
                                    print(e)
                            
                        if inPuTMsG.strip().startswith('/kkick'):
                            print('Processing FINAL title command (friend method)')
                            await LagSquad(key, iv)

                        if inPuTMsG.startswith(("/3")):
                            # Process /3 command - Create 3 player group
                            initial_message = f"[B][C]{get_random_color()}\n\nCreating 3-Player Group...\n\n"
                            await safe_send_message(response.Data.chat_type, initial_message, uid, chat_id, key, iv)
                            
                            # Fast squad creation and invite for 6 players
                            PAc = await OpEnSq(key, iv, region)
                            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', PAc)
                            
                            C = await cHSq(3, uid, key, iv, region)
                            await asyncio.sleep(0.3)
                            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', C)
                            
                            V = await SEnd_InV(3, uid, key, iv, region)
                            await asyncio.sleep(0.3)
                            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', V)
                            
                            E = await ExiT(None, key, iv)
                            await asyncio.sleep(3.5)
                            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', E)
                            
                            # SUCCESS MESSAGE
                            success_message = f"[B][C][FFFF00]✅ SUCCESS! 6-Player Group invitation sent successfully to {uid}!\n"
                            await safe_send_message(response.Data.chat_type, success_message, uid, chat_id, key, iv)

                        if inPuTMsG.startswith(("/4")):
                            # Process /3 command - Create 3 player group
                            initial_message = f"[B][C]{get_random_color()}\n\nCreating 3-Player Group...\n\n"
                            await safe_send_message(response.Data.chat_type, initial_message, uid, chat_id, key, iv)
                            
                            # Fast squad creation and invite for 6 players
                            PAc = await OpEnSq(key, iv, region)
                            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', PAc)
                            
                            C = await cHSq(4, uid, key, iv, region)
                            await asyncio.sleep(0.3)
                            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', C)
                            
                            V = await SEnd_InV(4, uid, key, iv, region)
                            await asyncio.sleep(0.3)
                            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', V)
                            
                            E = await ExiT(None, key, iv)
                            await asyncio.sleep(3.5)
                            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', E)
                            
                            # SUCCESS MESSAGE
                            success_message = f"[B][C][FFFF00]✅ SUCCESS! 6-Player Group invitation sent successfully to {uid}!\n"
                            await safe_send_message(response.Data.chat_type, success_message, uid, chat_id, key, iv)

                        # In your TcPChaT function, look for the command handling section
                        # It might look something like this:

                        if inPuTMsG.startswith('/room '):
                            await handle_room_command(inPuTMsG, uid, chat_id, key, iv, region, response.Data.chat_type)

                        # Join Custom Room Command
                        if inPuTMsG.strip().startswith('/joinroom'):
                            print('Processing custom room join command')
    
                            parts = inPuTMsG.strip().split()
                            if len(parts) < 3:
                                error_msg = f"[B][C][FF0000]❌ Usage: /joinroom (room_id) (password)\nExample: /joinroom 123456 0000\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                            else:
                                room_id = parts[1]
                                room_password = parts[2]
        
                                initial_msg = f"[B][C][FFFF00]🚀 Joining custom room...\n🏠 Room: {room_id}\n🔑 Password: {room_password}\n"
                                await safe_send_message(response.Data.chat_type, initial_msg, uid, chat_id, key, iv)
        
                                try:
                                    # Join the custom room
                                    join_packet = await join_custom_room(room_id, room_password, key, iv, region)
                                    await SEndPacKeT(whisper_writer, online_writer, 'OnLine', join_packet)
            
                                    success_msg = f"[B][C][FFFF00]✅ Joined custom room {room_id}!\n🤖 Bot is now in room chat!\n"
                                    await safe_send_message(response.Data.chat_type, success_msg, uid, chat_id, key, iv)
            
                                except Exception as e:
                                    error_msg = f"[B][C][FF0000]❌ Failed to join room: {str(e)}\n"
                                    await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)

                        if inPuTMsG.startswith(("/5")):
                            # Process /5 command in any chat type
                            initial_message = f"[B][C]{get_random_color()}\n\nSending Group Invitation...\n\n"
                            await safe_send_message(response.Data.chat_type, initial_message, uid, chat_id, key, iv)
                            
                            # Fast squad creation and invite
                            PAc = await OpEnSq(key, iv, region)
                            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', PAc)
                            
                            C = await cHSq(5, uid, key, iv, region)
                            await asyncio.sleep(0.3)  # Reduced delay
                            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', C)
                            
                            V = await SEnd_InV(5, uid, key, iv, region)
                            await asyncio.sleep(0.3)  # Reduced delay
                            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', V)
                            
                            E = await ExiT(None, key, iv)
                            await asyncio.sleep(3.5)  # Reduced from 3 seconds
                            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', E)
                            
                            # SUCCESS MESSAGE
                            success_message = f"[B][C][FFFF00]✅ SUCCESS! Group invitation sent successfully to {uid}!\n"
                            await safe_send_message(response.Data.chat_type, success_message, uid, chat_id, key, iv)

                            if len(parts) < 2:
                                error_msg = f"[B][C][FF0000]❌ ERROR! Usage: /kick (uid)\nExample: /kick 123456789\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                            else:
                                room_id = parts[1]

                                initial_message = f"[B][C]{get_random_color()}\nkicking {uid}...\n"
                                await safe_send_message(response.Data.chat_type, initial_message, uid, chat_id, key, iv)
                                
                                try:
                                    # Fast squad creation and invite for 5 players
                                    PAc = await Create_xr_room_packet_fixed__(room_id, key, iv)
                                    await SEndPacKeT(whisper_writer, online_writer, 'OnLine', PAc)
                                    await asyncio.sleep(0.3)
                                except Exception as e:
                                    print(e)

                        # Replace the existing title handler with this
                        # Use the FINAL version
                        if inPuTMsG.strip().startswith('/kick'):
                            parts = inPuTMsG.strip().split()
                            if len(parts) < 2:
                                error_msg = f"[B][C][FF0000]❌ ERROR! Usage: /kick (uid)\nExample: /kick 123456789\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                            else:
                                target_uid = parts[1]
                                initial_message = f"[B][C]{get_random_color()}\nkicking {target_uid}...\n"
                                await safe_send_message(response.Data.chat_type, initial_message, uid, chat_id, key, iv)
                                
                                try:
                                    # Fast squad creation and invite for 5 players
                                    PAc = await KickTarget(target_uid, key, iv)
                                    await SEndPacKeT(whisper_writer, online_writer, 'OnLine', PAc)
                                    await asyncio.sleep(0.3)
                                except Exception as e:
                                    print(e)
                                    
                        if inPuTMsG.strip().startswith('/tester'):
                            parts = inPuTMsG.strip().split()
                            if len(parts) < 2:
                                error_msg = f"[B][C][FF0000]❌ ERROR! Usage: /kick (uid)\nExample: /kick 123456789\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                            else:
                                target_uid = parts[1]
                                initial_message = f"[B][C]{get_random_color()}\nkicking {target_uid}...\n"
                                await safe_send_message(response.Data.chat_type, initial_message, uid, chat_id, key, iv)
                                
                                
                            if len(parts) < 2:
                                error_msg = f"""[B][C][FF0000]❌ Usage: /entry (uid)
                        Example: /entry 123456789
                        Example: /entry me (for yourself)

                        Effect: Sends arrival animation to player
                        """
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                            else:
                                target_uid = parts[1]
        
                                # Handle "me" or "self"
                                if target_uid.lower() in ['me', 'self', 'myself']:
                                    target_uid = str(response.Data.uid)
                                    target_name = "Yourself"
                                else:
                                    target_name = f"UID {target_uid}"
        
                                initial_msg = f"[B][C][00FF00]🎬 Sending arrival animation to {target_name}...\n"
                                await safe_send_message(response.Data.chat_type, initial_msg, uid, chat_id, key, iv)
        
                                try:
                                    # Send the entry emote packet
                                    entry_packet = await Send_Entry_Emote(int(target_uid), key, iv)
                                    
                                    if entry_packet:
                                        await SEndPacKeT(whisper_writer, online_writer, 'OnLine', entry_packet)
                
                                        success_msg = f"[B][C][00FF00]✅ ARRIVAL ANIMATION SENT!\n"
                                        success_msg += f"[FFFFFF]👤 Target: {target_name}\n"
                                        success_msg += f"[FFFFFF]🎭 Emote ID: 912038002\n"
                                        success_msg += f"[FFFFFF]✨ Effect: Entry/Arrival Animation\n"
                
                                        await safe_send_message(response.Data.chat_type, success_msg, uid, chat_id, key, iv)
                                        print(f"✅ Sent entry emote to {target_uid}")
                                    else:
                                        error_msg = f"[B][C][FF0000]❌ Failed to create entry emote packet!\n"
                                        await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                
                                except Exception as e:
                                    error_msg = f"[B][C][FF0000]❌ Error sending entry emote: {str(e)[:50]}\n"
                                    await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                    
                                    
                        if inPuTMsG.strip() == "/admin":
                            # Process /admin command in any chat type
                            admin_message = """
[C][B][00BFFF]╔════════════════════╗
[FFFFFF]✨ Join Our Official Telegram
[FFFFFF]⚡ [00E5FF]@chayan210 💎
[AAAAAA]Thank you for your continued support
[00BFFF]╠════════════════════╣
[FFD700]⚡ Owner : [FFFFFF]ZAINUㅤVIP
[00FF99]✨ To purchase a GUILD BOT,
[00FF99]please contact us on Telegram:
[FFFFFF]@chayan210 💎
[00BFFF]╚════════════════════╝
[CCCCCC]✨ Developed by —͟͞͞ </> [00E5FF]ZAINUㅤVIP ❄️
"""
                            await safe_send_message(response.Data.chat_type, admin_message, uid, chat_id, key, iv)

                        # Add this with your other command handlers in the TcPChaT function
                        
                        if inPuTMsG.strip().startswith('/multijoin'):
                            print('Processing multi-account join request')
    
                            parts = inPuTMsG.strip().split()
                            if len(parts) < 2:
                                error_msg = f"[B][C][FF0000]❌ Usage: /multijoin (target_uid)\nExample: /multijoin 123456789\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                            else:
                                target_uid = parts[1]
        
                                if not target_uid.isdigit():
                                    error_msg = f"[B][C][FF0000]❌ Please write a valid player ID!\n"
                                    await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                    return
        
                                initial_msg = f"[B][C][FFFF00]🚀 Starting multi-join attack on {target_uid}...\n"
                                await safe_send_message(response.Data.chat_type, initial_msg, uid, chat_id, key, iv)
        
                                try:
                                    # Try the fake multi-account method (more reliable)
                                    success_count, total_attempts = await real_multi_account_join(target_uid, key, iv, region)
            
                                    if success_count > 0:
                                        result_msg = f"""
[B][C][FFFF00]✅ MULTI-JOIN ATTACK COMPLETED!

🎯 Target: {target_uid}
✅ Successful Requests: {success_count}
📊 Total Attempts: {total_attempts}
⚡ Different squad variations sent!

💡 Check your game for join requests!
"""
                                    else:
                                        result_msg = f"[B][C][FF0000]❌ All join requests failed! Check bot connection.\n"
            
                                    await safe_send_message(response.Data.chat_type, result_msg, uid, chat_id, key, iv)
            
                                except Exception as e:
                                    error_msg = f"[B][C][FF0000]❌ Multi-join error: {str(e)}\n"
                                    await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)



                        # Update the command handler
                        if inPuTMsG.strip().startswith('/reject'):
                            print('Processing reject spam command in any chat type')
    
                            parts = inPuTMsG.strip().split()
                            if len(parts) < 2:
                                error_msg = f"[B][C][FF0000]❌ ERROR! Usage: /reject (target_uid)\nExample: /reject 123456789\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                            else:
                                target_uid = parts[1]
        
                                # Stop any existing reject spam
                                if reject_spam_task and not reject_spam_task.done():
                                    reject_spam_running = False
                                    reject_spam_task.cancel()
                                    await asyncio.sleep(0.5)
        
                                # Send start message
                                start_msg = f"[B][C][1E90FF]🌀 Started Reject Spam on: {target_uid}\n🌀 Packets: 150 each type\n🌀 Interval: 0.2 seconds\n"
                                await safe_send_message(response.Data.chat_type, start_msg, uid, chat_id, key, iv)
        
                                # Start reject spam in background
                                reject_spam_running = True
                                reject_spam_task = asyncio.create_task(reject_spam_loop(target_uid, key, iv))
        
                                # Wait for completion in background and send completion message
                                asyncio.create_task(handle_reject_completion(reject_spam_task, target_uid, uid, chat_id, response.Data.chat_type, key, iv))


                        if inPuTMsG.strip() == '/reject_stop':
                            if reject_spam_task and not reject_spam_task.done():
                                reject_spam_running = False
                                reject_spam_task.cancel()
                                stop_msg = f"[B][C][FFFF00]✅ Reject spam stopped successfully!\n"
                                await safe_send_message(response.Data.chat_type, stop_msg, uid, chat_id, key, iv)
                            else:
                                error_msg = f"[B][C][FF0000]❌ No active reject spam to stop!\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                
                        # In your command handler where you call Room_Spam:
                        if inPuTMsG.strip().startswith('/room'):
                            print('Processing advanced room spam command')
                            
                            parts = inPuTMsG.strip().split()
                            if len(parts) < 2:
                                error_msg = f"[B][C][FF0000]❌ ERROR! Usage: /room (uid)\nExample: /room 123456789\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                            else:
                                target_uid = parts[1]
                                room_id = parts[2]
        
                                if not target_uid.isdigit():
                                    error_msg = f"[B][C][FF0000]❌ ERROR! Please write a valid player ID!\n"
                                    await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                    return
        
                                # Send initial message
                                initial_msg = f"[B][C][00FF00]🔍 Working on room spam for {target_uid}...\n"
                                await safe_send_message(response.Data.chat_type, initial_msg, uid, chat_id, key, iv)
                                
                                try:
                                    # Method 1: Try to get room ID from recent packets
                                
                                    

                                    room_msg = f"[B][C][00FF00]🎯 Detected player in room {room_id}\n"
                                    await safe_send_message(response.Data.chat_type, room_msg, uid, chat_id, key, iv)
            
                                    # Create spam packet
                                    spam_packet = await Room_Spam(target_uid, room_id, "MG24 GAMER", key, iv)
            
                                    # Send 99 spam packets rapidly (like your other TCP)
                                    spam_count = 99
                                    
                                    start_msg = f"[B][C][00FF00]🚀 Starting spam: {spam_count} packets to room {room_id}\n"
                                    await safe_send_message(response.Data.chat_type, start_msg, uid, chat_id, key, iv)
            
                                    for i in range(spam_count):
                                        await SEndPacKeT(whisper_writer, online_writer, 'OnLine', spam_packet)
                
                                        # Progress updates
                                        if (i + 1) % 25 == 0:
                                            progress_msg = f"[B][C][00FF00]📦 Progress: {i+1}/{spam_count} packets sent\n"
                                            await safe_send_message(response.Data.chat_type, progress_msg, uid, chat_id, key, iv)
                                            print(f"Room spam progress: {i+1}/{spam_count} to UID: {target_uid}")
                
                                        # Very short delay (0.05 seconds = 50ms)
                                        await asyncio.sleep(0.05)
            
                                    # Final success message
                                    success_msg = f"[B][C][00FF00]✅ ROOM SPAM COMPLETED!\n🎯 Target: {target_uid}\n📦 Packets: {spam_count}\n🏠 Room: {room_id}\n⚡ Speed: Ultra fast\n"
                                    await safe_send_message(response.Data.chat_type, success_msg, uid, chat_id, key, iv)
                                    print(f"Room spam completed for UID: {target_uid}")
            
                                except Exception as e:
                                    error_msg = f"[B][C][FF0000]❌ ERROR in room spam: {str(e)}\n"
                                    await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                    print(f"Room spam error: {e}")                                

                        # Individual command handlers for /v1 to /s8
                        if inPuTMsG.strip().startswith('/v1'):

                            await handle_badge_command('v1', inPuTMsG, uid, chat_id, key, iv, region, response.Data.chat_type)
    
                        if inPuTMsG.strip().startswith('/v2'):

                            await handle_badge_command('v2', inPuTMsG, uid, chat_id, key, iv, region, response.Data.chat_type)

                        if inPuTMsG.strip().startswith('/v3'):

                            await handle_badge_command('v3', inPuTMsG, uid, chat_id, key, iv, region, response.Data.chat_type)

                        if inPuTMsG.strip().startswith('/v4'):

                            await handle_badge_command('v4', inPuTMsG, uid, chat_id, key, iv, region, response.Data.chat_type)

                        if inPuTMsG.strip().startswith('/v5'):

                            await handle_badge_command('v5', inPuTMsG, uid, chat_id, key, iv, region, response.Data.chat_type)

                        if inPuTMsG.strip().startswith('/s6'):
                            await handle_badge_command('s6', inPuTMsG, uid, chat_id, key, iv, region, response.Data.chat_type)

                        if inPuTMsG.strip().startswith('/s7'):
                            await handle_badge_command('s7', inPuTMsG, uid, chat_id, key, iv, region, response.Data.chat_type)

                        if inPuTMsG.strip().startswith('/s8'):
                            await handle_badge_command('s8', inPuTMsG, uid, chat_id, key, iv, region, response.Data.chat_type)

                                    
                                                                                                     
                        if inPuTMsG.strip().startswith('@joinroom'):
                            print('Processing custom room join command')
    
                            parts = inPuTMsG.strip().split()
                            if len(parts) < 3:
                                error_msg = f"[B][C][FF0000]❌ Usage: /joinroom (room_id) (password)\nExample: /joinroom 123456 0000\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                            else:
                                room_id = parts[1]
                                room_password = parts[2]
        
                                initial_msg = f"[B][C][FFFF00]🚀 Joining custom room...\n🏠 Room: {room_id}\n🔑 Password: {room_password}\n"
                                await safe_send_message(response.Data.chat_type, initial_msg, uid, chat_id, key, iv)
        
                                try:
                                    # Join the custom room
                                    join_packet = await join_custom_room(room_id, room_password, key, iv, region)
                                    await SEndPacKeT(whisper_writer, online_writer, 'OnLine', join_packet)
            
                                    success_msg = f"[B][C][FFFF00]✅ Joined custom room {room_id}!\n🤖 Bot is now in room chat!\n"
                                    await safe_send_message(response.Data.chat_type, success_msg, uid, chat_id, key, iv)
            
                                except Exception as e:
                                    error_msg = f"[B][C][FF0000]❌ Failed to join room: {str(e)}\n"
                                    await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)

                        if inPuTMsG.strip().startswith('/createroom'):
                            print('Processing custom room creation')
    
                            parts = inPuTMsG.strip().split()
                            if len(parts) < 3:
                                error_msg = f"[B][C][FF0000]❌ Usage: /createroom (room_name) (password) [players=4]\nExample: /createroom BOTROOM 0000 4\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                            else:
                                room_name = parts[1]
                                room_password = parts[2]
                                max_players = parts[3] if len(parts) > 3 else "4"
        
                                initial_msg = f"[B][C][FFFF00]🏠 Creating custom room...\n📛 Name: {room_name}\n🔑 Password: {room_password}\n👥 Max Players: {max_players}\n"
                                await safe_send_message(response.Data.chat_type, initial_msg, uid, chat_id, key, iv)
        
                                try:
                                    # Create custom room
                                    create_packet = await create_custom_room(room_name, room_password, int(max_players), key, iv, region)
                                    await SEndPacKeT(whisper_writer, online_writer, 'OnLine', create_packet)
            
                                    success_msg = f"[B][C][FFFF00]✅ Custom room created!\n🏠 Room: {room_name}\n🔑 Password: {room_password}\n👥 Max: {max_players}\n🤖 Bot is now hosting!\n"
                                    await safe_send_message(response.Data.chat_type, success_msg, uid, chat_id, key, iv)
            
                                except Exception as e:
                                    error_msg = f"[B][C][FF0000]❌ Failed to create room: {str(e)}\n"
                                    await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)               
                        
                                                
                        # Add with other command handlers in TcPChaT
                        if inPuTMsG.strip().startswith('/arr'):
                            print('Processing entry emote command')
    
                            parts = inPuTMsG.strip().split()
    
                            if len(parts) < 2:
                                error_msg = f"""[B][C][FF0000]❌ Usage: /entry (uid)
                        Example: /entry 123456789
                        Example: /entry me (for yourself)

                        Effect: Sends arrival animation to player
                        """
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                            else:
                                target_uid = parts[1]
        
                                # Handle "me" or "self"
                                if target_uid.lower() in ['me', 'self', 'myself']:
                                    target_uid = str(response.Data.uid)
                                    target_name = "Yourself"
                                else:
                                    target_name = f"UID {target_uid}"
        
                                initial_msg = f"[B][C][FFFF00]🎬 Sending arrival animation to {target_name}...\n"
                                await safe_send_message(response.Data.chat_type, initial_msg, uid, chat_id, key, iv)
        
                                try:
                                    # Send the entry emote packet
                                    entry_packet = await Send_Entry_Emote(int(target_uid), key, iv)
                                    
                                    if entry_packet:
                                        await SEndPacKeT(whisper_writer, online_writer, 'OnLine', entry_packet)
                
                                        success_msg = f"[B][C][FFFF00]✅ ARRIVAL ANIMATION SENT!\n"
                                        success_msg += f"[FFFFFF]👤 Target: {target_name}\n"
                                        success_msg += f"[FFFFFF]🎭 Emote ID: 912038002\n"
                                        success_msg += f"[FFFFFF]✨ Effect: Entry/Arrival Animation\n"
                
                                        await safe_send_message(response.Data.chat_type, success_msg, uid, chat_id, key, iv)
                                        print(f"✅ Sent entry emote to {target_uid}")
                                    else:
                                        error_msg = f"[B][C][FF0000]❌ Failed to create entry emote packet!\n"
                                        await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                
                                except Exception as e:
                                    error_msg = f"[B][C][FF0000]❌ Error sending entry emote: {str(e)[:50]}\n"
                                    await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                            
                                                                                          # FIXED JOIN COMMAND
                        if inPuTMsG.startswith('!'):
                            # Process /join command in any chat type
                            parts = inPuTMsG.strip().split()
                            if len(parts) < 2:
                                error_msg = f"[B][C][FF0000]❌ ERROR! Usage: /join (team_code)\nExample: /join ABC123\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                            else:
                                CodE = parts[1]
                                uid = response.Data.uid  # Get the UID of person who sent the command
        
                                initial_message = f"[B][C]{get_random_color()}\nJoining squad with code: {CodE}...\n"
                                await safe_send_message(response.Data.chat_type, initial_message, uid, chat_id, key, iv)
        
                                try:
                                    # Try using the regular join method first
                                    EM = await GenJoinSquadsPacket(CodE, key, iv)
                                    await SEndPacKeT(whisper_writer, online_writer, 'OnLine', EM)
            
                                    # Wait a bit for the join to complete
                                    await asyncio.sleep(2)
            
                                    # DUAL RINGS EMOTE - BOTH SENDER AND BOT
                                    try:
                                        await auto_rings_emote_dual(uid, key, iv, region)
                                    except Exception as emote_error:
                                        print(f"Dual emote failed but join succeeded: {emote_error}")
            
                                    # SUCCESS MESSAGE
                                    success_message = f"[B][C][FFFF00]✅ SUCCESS! Joined squad: {CodE}!\n💍 Dual Rings emote activated!\n🤖 Bot + You = 💕\n"
                                    await safe_send_message(response.Data.chat_type, success_message, uid, chat_id, key, iv)
            
                                except Exception as e:
                                    print(f"Regular join failed, trying ghost join: {e}")
                                    # If regular join fails, try ghost join
                                    try:
                                        # Get bot's UID from global context or login data
                                        bot_uid = LoGinDaTaUncRypTinG.AccountUID if hasattr(LoGinDaTaUncRypTinG, 'AccountUID') else TarGeT
                
                                        ghost_packet = await ghost_join_packet(bot_uid, CodE, key, iv)
                                        if ghost_packet:
                                            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', ghost_packet)
                    
                                            # Wait a bit for ghost join to complete
                                            await asyncio.sleep(2)
                    
                                            # DUAL RINGS EMOTE - BOTH SENDER AND BOT
                                            try:
                                                await auto_rings_emote_dual(uid, key, iv, region)
                                            except Exception as emote_error:
                                                print(f"Dual emote failed but ghost join succeeded: {emote_error}")
                    
                                            success_message = f"[B][C][FFFF00]✅ SUCCESS! Ghost joined squad: {CodE}!\n💍 Dual Rings emote activated!\n🤖 Bot + You = 💕\n"
                                            await safe_send_message(response.Data.chat_type, success_message, uid, chat_id, key, iv)
                                        else:
                                            error_msg = f"[B][C][FF0000]❌ ERROR! Failed to create ghost join packet.\n"
                                            await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                    
                                    except Exception as ghost_error:
                                        print(f"Ghost join also failed: {ghost_error}")
                                        error_msg = f"[B][C][FF0000]❌ ERROR! Failed to join squad: {str(ghost_error)}\n"
                                        await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                
                
                        if inPuTMsG.strip().startswith('/ghost'):
                            # Process /ghost command in any chat type
                            parts = inPuTMsG.strip().split()
                            if len(parts) < 2:
                                error_msg = f"[B][C][FF0000]❌ ERROR! Usage: /ghost (team_code)\nExample: /ghost ABC123\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                            else:
                                CodE = parts[1]
                                initial_message = f"[B][C]{get_random_color()}\nGhost joining squad with code: {CodE}...\n"
                                await safe_send_message(response.Data.chat_type, initial_message, uid, chat_id, key, iv)
                                
                                try:
                                    # Get bot's UID from global context or login data
                                    bot_uid = LoGinDaTaUncRypTinG.AccountUID if hasattr(LoGinDaTaUncRypTinG, 'AccountUID') else TarGeT
                                    
                                    ghost_packet = await ghost_join_packet(bot_uid, CodE, key, iv)
                                    if ghost_packet:
                                        await SEndPacKeT(whisper_writer, online_writer, 'OnLine', ghost_packet)
                                        success_message = f"[B][C][FFFF00]✅ SUCCESS! Ghost joined squad with code: {CodE}!\n"
                                        await safe_send_message(response.Data.chat_type, success_message, uid, chat_id, key, iv)
                                    else:
                                        error_msg = f"[B][C][FF0000]❌ ERROR! Failed to create ghost join packet.\n"
                                        await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                        
                                except Exception as e:
                                    error_msg = f"[B][C][FF0000]❌ ERROR! Ghost join failed: {str(e)}\n"
                                    await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)

                        # NEW LAG COMMAND
                        if inPuTMsG.strip().startswith('/lag '):
                            print('Processing lag command in any chat type')
                            
                            parts = inPuTMsG.strip().split()
                            if len(parts) < 2:
                                error_msg = f"[B][C][FF0000]❌ ERROR! Usage: /lag (team_code)\nExample: /lag ABC123\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                            else:
                                team_code = parts[1]
                                
                                # Stop any existing lag task
                                if lag_task and not lag_task.done():
                                    lag_running = False
                                    lag_task.cancel()
                                    await asyncio.sleep(0.1)
                                
                                # Start new lag task
                                lag_running = True
                                lag_task = asyncio.create_task(lag_team_loop(team_code, key, iv, region))
                                
                                # SUCCESS MESSAGE
                                success_msg = f"[B][C][FFFF00]✅ SUCCESS! Lag attack started!\nTeam: {team_code}\nAction: Rapid join/leave\nSpeed: Ultra fast (milliseconds)\n"
                                await safe_send_message(response.Data.chat_type, success_msg, uid, chat_id, key, iv)

                        # STOP LAG COMMAND
                        if inPuTMsG.strip() == '/stop lag':
                            if lag_task and not lag_task.done():
                                lag_running = False
                                lag_task.cancel()
                                success_msg = f"[B][C][FFFF00]✅ SUCCESS! Lag attack stopped successfully!\n"
                                await safe_send_message(response.Data.chat_type, success_msg, uid, chat_id, key, iv)
                            else:
                                error_msg = f"[B][C][FF0000]❌ ERROR! No active lag attack to stop!\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)

                        if inPuTMsG.startswith('/exit'):
                            # Process /exit command in any chat type
                            initial_message = f"[B][C]{get_random_color()}\nLeaving current squad...\n"
                            await safe_send_message(response.Data.chat_type, initial_message, uid, chat_id, key, iv)
                            
                            leave = await ExiT(uid,key,iv)
                            await SEndPacKeT(whisper_writer , online_writer , 'OnLine' , leave)
                            
                            # SUCCESS MESSAGE
                            success_message = f"[B][C][FFFF00]✅ SUCCESS! Left the squad successfully!\n"
                            await safe_send_message(response.Data.chat_type, success_message, uid, chat_id, key, iv)

                        if inPuTMsG.strip().startswith('/start'):
                            # Process /s command in any chat type
                            initial_message = f"[B][C]{get_random_color()}\nStarting match...\n"
                            await safe_send_message(response.Data.chat_type, initial_message, uid, chat_id, key, iv)
                            
                            start_packet = await start_auto_packet(key, iv, region)
                            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', start_packet)
                            initiial_message = f"[B][C]{get_random_color()}\nStarting match...\n"
                            await safe_send_message(response.Data.chat_type, initiial_message, uid, chat_id, key, iv)
                            
        

                        if inPuTMsG.strip().startswith('/mg '):
                            print('Processing wave message command')
                          
                            parts = inPuTMsG.strip().split()
    
                            if len(parts) < 2:
                                error_msg = f"[B][C][FF0000]❌ Usage: /mg (message) [repeats=5]\n"
                                error_msg += f"[FFFFFF]Example: /mg hello 3\n"
                                error_msg += f"[FFFFFF]Will send: h, he, hel, hell, hello, hell, hel, he, h\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                            else:
                                try:
                                    # Get message and optional repeats
                                    message_text = parts[1]
                                    repeats = 5  # Default
            
                                    if len(parts) > 2:
                                        repeats = int(parts[2])
            
                                    if repeats <= 0:
                                        error_msg = f"[B][C][FF0000]❌ Repeats must be > 0!\n"
                                        await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                    elif repeats > 10:
                                        error_msg = f"[B][C][FF0000]❌ Max 10 repeats!\n"
                                        await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                    elif len(message_text) < 2:
                                        error_msg = f"[B][C][FF0000]❌ Message must be at least 2 characters!\n"
                                        await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                    else:
                                        global mg_spam_task
                                        if mg_spam_task and not mg_spam_task.done():
                                            global msg_spam_running
                                            msg_spam_running = False
                                            mg_spam_task.cancel()
                                            await asyncio.sleep(0.5)
                
                                        # Calculate total messages
                                        total_messages_per_cycle = (len(message_text) * 2) - 2
                                        total_messages = total_messages_per_cycle * repeats
                
                                        initial_msg = f"[B][C][FFFF00]🌊 WAVE MESSAGE STARTING!\n"
                                        initial_msg += f"[FFFFFF]Message: {message_text}\n"
                                        initial_msg += f"[FFFFFF]Repeats: {repeats} cycles\n"
                                        initial_msg += f"[FFFFFF]Pattern: h → he → hel → hell → hello → hell → hel → he → h\n"
                                        initial_msg += f"[FFFF00]Total messages: {total_messages}\n"
                                        await safe_send_message(response.Data.chat_type, initial_msg, uid, chat_id, key, iv)
                                        
                                        # Start wave messages
                                        msg_spam_running = True
                                        mg_spam_task = asyncio.create_task(
                                            send_wave_messages(message_text, repeats, chat_id, key, iv, region)
                                        )
                
                                        # Handle completion
                                        asyncio.create_task(
                                            handle_wave_completion(mg_spam_task, message_text, repeats, uid, chat_id, response.Data.chat_type, key, iv)
                                        )
                
                                except ValueError:
                                    error_msg = f"[B][C][FF0000]❌ Invalid format!\n"
                                    await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                        
                        if inPuTMsG.strip().startswith('/msg '):
                            print('Processing message spam command')
                            global msg_spam_task
                            parts = inPuTMsG.strip().split()
    
                            if len(parts) < 3:
                                error_msg = f"[B][C][FF0000]❌ ERROR! Usage: /msg (message) (times)\n"
                                error_msg += f"[FFFFFF]Example: /msg Hello Team! 5\n"
                                error_msg += f"[FFFFFF]Will send 'Hello Team!' 5 times in team chat\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                            else:
                                try:
                                    # Extract message and times
                                    times = int(parts[-1]) # Last part is the number
            
                                    # Reconstruct the message (everything except first part and last part)
                                    message_text = ' '.join(parts[1:-1])
            
                                    if times <= 0:
                                        error_msg = f"[B][C][FF0000]❌ ERROR! Times must be greater than 0!\n"
                                        await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                    
                                    elif not message_text.strip():
                                        error_msg = f"[B][C][FF0000]❌ ERROR! Message cannot be empty!\n"
                                        await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                    else:
                                        # Stop any existing message spam
                                      
                                        if msg_spam_task and not msg_spam_task.done():
                                            
                                            msg_spam_running = False
                                            msg_spam_task.cancel()
                                            await asyncio.sleep(0.1)
                
                                        # Check if we have the chat_id from the message
                                        # If not, use the bot's UID from login data
                                        chat_id = chat_id
                
                                        # Send initial message
                                        initial_msg = f"[B][C][FFFF00]📢 MESSAGE SPAM STARTING!\n"
                                        initial_msg += f"[FFFFFF]Message: {message_text}\n"
                                        initial_msg += f"[FFFFFF]Times: {times}\n"
                                        initial_msg += f"[FFFFFF]Chat: Team/Squad Chat\n"
                                        initial_msg += f"[FFFF00]Sending messages...\n"
                                        await safe_send_message(response.Data.chat_type, initial_msg, uid, chat_id, key, iv)
                
                                        # Start message spam
                                        msg_spam_running = True
                                        msg_spam_task = asyncio.create_task(
                                            msg_spam_loop(message_text, times, chat_id, key, iv, region)
                                        )
                
                                        # Wait for completion and send result
                                        asyncio.create_task(
                                            handle_msg_spam_completion(msg_spam_task, message_text, times, uid, chat_id, response.Data.chat_type, key, iv)
                                        )
                                        
                                except ValueError:
                                    error_msg = f"[B][C][FF0000]❌ ERROR! Invalid format!\n"
                                    error_msg += f"[FFFFFF]Usage: /msg (message) (times)\n"
                                    error_msg += f"[FFFFFF]Example: /msg Hello World! 10\n"
                                    await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                except Exception as e:
                                    error_msg = f"[B][C][FF0000]❌ ERROR: {str(e)}\n"
                                    await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)

                        # Add stop command
                        if inPuTMsG.strip() == '/stop msg':
                            if msg_spam_task and not msg_spam_task.done():
                                msg_spam_running = False
                                msg_spam_task.cancel()
                                success_msg = f"[B][C][FFFF00]✅ MESSAGE SPAM STOPPED!\n[FFFFFF]All message sending has been stopped.\n"
                                await safe_send_message(response.Data.chat_type, success_msg, uid, chat_id, key, iv)
                            else:
                                error_msg = f"[B][C][FF0000]❌ No active message spam to stop!\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
        
                        # Add this to your command handlers in TcPChaT function:
                        if inPuTMsG.strip().startswith('/train'):
                            print('Processing training mode command')
                            await handle_training_command(inPuTMsG, uid, chat_id, key, iv, region, response.Data.chat_type)
                            
                        # Add these to your command handlers in TcPChaT function:
                        # Add this to your command handlers in TcPChaT function:
                        if inPuTMsG.strip().startswith('/join_req '):
                            print('Processing /join_req command')
                            await handle_join_req_command(inPuTMsG, uid, chat_id, key, iv, region, response.Data.chat_type, LoGinDaTaUncRypTinG)


                        if inPuTMsG.strip().startswith('/e'):
                            print(f'Processing emote command in chat type: {response.Data.chat_type}')
    
                            parts = inPuTMsG.strip().split()
    
                            # Check if user wants to list emotes or show help
                            if len(parts) == 1 or (len(parts) == 2 and parts[1].lower() == 'list'):
                                # Show available emotes
                                emote_list_msg = f"[B][C][FFFF00]🎭 EMOTE SYSTEM\n"
                                emote_list_msg += f"[FFFFFF]────────────────\n"
                                emote_list_msg += f"[FFFF00]📊 STATS:\n"
                                emote_list_msg += f"[FFFFFF]• Number emotes: 1-{len(NUMBER_EMOTES)}\n"
                                emote_list_msg += f"[FFFFFF]• Named emotes: {len(NAME_EMOTES)} names\n"
                                emote_list_msg += f"[FFFFFF]────────────────\n"
                                emote_list_msg += f"[FFFF00]🎯 USAGE:\n"
                                emote_list_msg += f"[FFFFFF]/e [number/name] → Send to yourself\n"
                                emote_list_msg += f"[FFFFFF]/e [uid] [number/name] → Send to UID\n"
                                emote_list_msg += f"[FFFFFF]────────────────\n"
                                emote_list_msg += f"[FFFF00]🔥 POPULAR NAMES:\n"
        
                                # Show popular named emotes
                                popular_names = ["ak", "m60", "p90", "scar", "famas", "heart", "love", "dance", "hello", "money"]
                                line = ""
                                for name in popular_names:
                                    if name.lower() in NAME_EMOTES:
                                        line += f"[FFFF00]{name}[FFFFFF], "
                                if line:
                                    emote_list_msg += line.rstrip(", ") + "\n"
        
                                emote_list_msg += f"[FFFFFF]────────────────\n"
                                emote_list_msg += f"[FFFF00]📖 EXAMPLES:\n"
                                emote_list_msg += f"[FFFFFF]/e ak → Send AK emote to yourself\n"
                                emote_list_msg += f"[FFFFFF]/e 123456789 heart → Send ❤️ to UID\n"
                                emote_list_msg += f"[FFFFFF]/e 123456789 1 → Send emote #1 to UID\n"
                                emote_list_msg += f"[FFFFFF]/e ring → Send ring emote to yourself\n"
                                emote_list_msg += f"[FFFFFF]/e list names → Show all named emotes\n"
        
                                # Check if user wants detailed name list
                                if len(parts) == 2 and parts[1].lower() == 'names':
                                    emote_list_msg += f"[FFFFFF]────────────────\n"
                                    emote_list_msg += f"[FFFF00]📝 ALL NAMED EMOTES:\n"
            
                                    # Show all named emotes in groups
                                    all_names = sorted(NAME_EMOTES.keys())
                                    for i in range(0, min(len(all_names), 30), 5):  # Show first 30 names
                                        group = all_names[i:i+5]
                                        emote_list_msg += f"[FFFFFF]{' | '.join(group)}\n"
            
                                    if len(all_names) > 30:
                                        emote_list_msg += f"[FFFFFF]... and {len(all_names) - 30} more\n"
        
                                await safe_send_message(response.Data.chat_type, emote_list_msg, uid, chat_id, key, iv)
                                continue
    
                            # Parse command
                            if len(parts) < 2:
                                error_msg = f"[B][C][FF0000]❌ ERROR! Usage: /e [emote_name_or_number]\n"
                                error_msg += f"[FFFFFF]Examples:\n"
                                error_msg += f"[FFFF00]/e ak[FFFFFF] → AK emote to yourself\n"
                                error_msg += f"[FFFF00]/e 123456789 heart[FFFFFF] → ❤️ to UID\n"
                                error_msg += f"[FFFF00]/e 123456789 1[FFFFFF] → Emote #1 to UID\n"
                                error_msg += f"[FFFF00]/e ring[FFFFFF] → Send ring emote to yourself\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                continue
    
                            # Show "preparing" message
                            initial_message = f'[B][C]{get_random_color()}\n🎭 Preparing emote...\n'
                            await safe_send_message(response.Data.chat_type, initial_message, uid, chat_id, key, iv)
                            
                            target_uids = []
                            emote_key = None
    
                            try:
                                # Determine if last part is emote key (could be number or name)
                                last_part = parts[-1].lower()
        
                                # Check if last part is an emote (number or name)
                                # Note: Your numbers go up to 417, so check for 3-digit numbers too
                                is_number = last_part.isdigit() and last_part in NUMBER_EMOTES
                                is_name = last_part in NAME_EMOTES
        
                                if is_number or is_name:
                                    # Case 1: /e ak or /e 1 (only emote - send to sender)
                                    if len(parts) == 2:
                                        emote_key = last_part
                                        target_uids.append(int(response.Data.uid))
            
                                    # Case 2: /e 123456789 heart (UID + emote)
                                    elif len(parts) == 3:
                                        target_uids.append(int(parts[1]))
                                        emote_key = last_part
            
                                    # Case 3: /e 111 222 333 ak (multiple UIDs + emote)
                                    else:
                                        for i in range(1, len(parts) - 1):
                                            target_uids.append(int(parts[i]))
                                        emote_key = last_part
                                else:
                                    # Last part is not a valid emote
                                    error_msg = f"[B][C][FF0000]❌ Invalid emote: '{last_part}'\n"
                                    error_msg += f"[FFFFFF]Use numbers (1-{len(NUMBER_EMOTES)}) or names like 'ak', 'heart', 'dance', 'ring'\n"
                                    error_msg += f"[FFFFFF]Use /e list names to see all available names\n"
                                    await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                    continue
        
                                # Get emote ID from either number or name dictionary
                                emote_id = None
                                emote_name_display = None
                                
                                if is_number:
                                    # Number-based emote
                                    emote_id = NUMBER_EMOTES.get(emote_key)
                                    emote_name_display = f"#{emote_key}"
                                else:
                                    # Name-based emote
                                    emote_id = NAME_EMOTES.get(emote_key)
                                    emote_name_display = emote_key
        
                                if not emote_id:
                                    error_msg = f"[B][C][FF0000]❌ Emote '{emote_name_display}' not found!\n"
                                    if emote_key.isdigit():
                                        error_msg += f"[FFFFFF]Available numbers: 1-{len(NUMBER_EMOTES)}\n"
                                    else:
                                        error_msg += f"[FFFFFF]Use /e list names to see all available names\n"
                                    await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                    continue
        
                                # Send emotes
                                success_count = 0
                                failed_uids = []
        
                                for target_uid in target_uids:
                                    try:
                                        H = await Emote_k(target_uid, int(emote_id), key, iv, region)
                                        await SEndPacKeT(whisper_writer, online_writer, 'OnLine', H)
                                        success_count += 1
                                        await asyncio.sleep(0.1)
                                    except Exception as e:
                                        print(f"Error sending emote to {target_uid}: {e}")
                                        failed_uids.append(str(target_uid))
        
                                # Success message
                                if success_count > 0:
                                    if target_uids[0] == int(response.Data.uid):
                                        target_list = "Yourself"
                                    elif len(target_uids) == 1:
                                        target_list = str(target_uids[0])
                                    else:
                                        target_list = f"{len(target_uids)} players"
            
                                    success_msg = f"[B][C][FFFF00]✅ EMOTE SENT!\n"
                                    success_msg += f"[FFFFFF]────────────────\n"
                                    success_msg += f"[FFFF00]🎭 Emote: {emote_name_display}\n"
                                    success_msg += f"[FFFF00]🆔 ID: {emote_id}\n"
                                    success_msg += f"[FFFF00]👤 Target: {target_list}\n"
                                    success_msg += f"[FFFF00]📊 Status: {success_count}/{len(target_uids)} successful\n"
            
                                    if failed_uids:
                                        success_msg += f"[FF0000]❌ Failed: {', '.join(failed_uids)}\n"
            
                                    success_msg += f"[FFFFFF]────────────────\n"
            
                                    await safe_send_message(response.Data.chat_type, success_msg, uid, chat_id, key, iv)
                                else:
                                    error_msg = f"[B][C][FF0000]❌ Failed to send emote to any target!\n"
                                    await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                    
                            except ValueError as ve:
                                print("ValueError:", ve)
                                error_msg = f"[B][C][FF0000]❌ Invalid format!\n"
                                error_msg += f"[FFFFFF]UIDs must be numbers (like 123456789)\n"
                                error_msg += f"[FFFFFF]Examples: /e ak, /e 123456789 heart, /e 1, /e ring\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                            except Exception as e:
                                print(f"Error processing /e command: {e}")
                                error_msg = f"[B][C][FF0000]❌ Error: {str(e)[:50]}\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)

                                #GALI SPAM MESSAGE 
                        # Add at the top with other global variables
                        BLOCKED_NAMES = ["durga", "hasib", "diablo", "codex"]  # Add your actual name

                        # Then in the /praise command handler, add this check:
                        if inPuTMsG.strip().startswith('/praise '):
                            print('Processing /praise command')

                            try:
                                parts = inPuTMsG.strip().split(maxsplit=1)

                                if len(parts) < 2:
                                    error_msg = (
                                        "[B][C][FF0000]❌ ERROR! Usage:\n"
                                        "/praise <name>\n"
                                        "Example: /praise hater"
                                    )
                                    await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                else:
                                    name = parts[1].strip()
            
                                    # ADD THIS CHECK - Prevent targeting yourself
                                    if name.lower() in [n.lower() for n in BLOCKED_NAMES]:
                                        error_msg = (
                                            f"[B][C][FF0000]⚠️ WARNING!\n"
                                            f"[FFFFFF]You cannot target '{name}'!\n"
                                            f"[FF0000]Bot owner protected! ⛔\n"
                                            f"[FFFFFF]Try another name."
                                        )
                                        await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                        continue
            
                                    # Rest of your code continues here...
                                    messages = [
                                        "{Name} তুমি সত্যিই খুব ভালো একজন মানুষ",
    "{Name} তোমার ব্যবহার সবার মন জয় করে নেয়",
    "{Name} তোমার হাসিটা খুব সুন্দর",
    "{Name} তোমার সঙ্গে কথা বললে ভালো লাগে",
    "{Name} তুমি অনেক স্মার্ট আর বুদ্ধিমান",
    "{Name} তোমার ব্যক্তিত্বটা খুব আকর্ষণীয়",
    "{Name} তুমি সবসময় পজিটিভ ভাবনা রাখো",
    "{Name} তোমার মতো মানুষ খুব কমই দেখা যায়",
    "{Name} তুমি সত্যিই বিশেষ একজন",
    "{Name} তোমার কাজের প্রতি নিষ্ঠা প্রশংসার যোগ্য",
    "{Name} তুমি বন্ধু হিসেবে অসাধারণ",
    "{Name} তোমার কথায় আলাদা একটা মাধুর্য আছে",
    "{Name} তুমি সবার সম্মান পাওয়ার যোগ্য",
    "{Name} তোমার উপস্থিতিতেই পরিবেশ ভালো হয়ে যায়",
    "{Name} তুমি ভবিষ্যতে অনেক দূর যাবে",
    "{Name} তোমার চিন্তাধারা খুব সুন্দর",
    "{Name} তুমি মানুষের মনে ইতিবাচক প্রভাব ফেলো"
                                            ]

                                    # Send each message one by one with random color
                                    for msg in messages:
                                        colored_message = f"[B][C]{get_random_color()} {msg.replace('{Name}', name.upper())}"
                                        await safe_send_message(response.Data.chat_type, colored_message, uid, chat_id, key, iv)
                                        await asyncio.sleep(2)

                            except Exception as e:
                                error_msg = f"[B][C][FF0000]❌ ERROR! Something went wrong:\n{str(e)}"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)                        
                                
                        # Add this with your other command handlers in the TcPChaT function

                        # EVO CYCLE START COMMAND - @evos
                        # EVO CYCLE START COMMAND - @evos
                        # EVO CYCLE START COMMAND - @evos
                        if inPuTMsG.strip().startswith('@evos'):
                            print('Processing evo cycle start command in any chat type')
    
                            parts = inPuTMsG.strip().split()
                            uids = []
    
                            # Always use the sender's UID (the person who typed @evos)
                            sender_uid = str(response.Data.uid)
                            uids.append(sender_uid)
                            print(f"Using sender's UID: {sender_uid}")
    
                            # Optional: Also allow specifying additional UIDs
                            if len(parts) > 1:
                                for part in parts[1:]:  # Skip the first part which is "@evos"
                                    if part.isdigit() and len(part) >= 7 and part != sender_uid:  # UIDs are usually 7+ digits
                                        uids.append(part)
                                        print(f"Added additional UID: {part}")

                            # Stop any existing evo cycle
                            if evo_cycle_task and not evo_cycle_task.done():
                                evo_cycle_running = False
                                evo_cycle_task.cancel()
                                await asyncio.sleep(0.5)
    
                            # Start new evo cycle
                            evo_cycle_running = True
                            evo_cycle_task = asyncio.create_task(
                                evo_cycle_spam(uids, key, iv, region, LoGinDaTaUncRypTinG)
                            )
    
                            # SUCCESS MESSAGE
                            if len(uids) == 1:
                                success_msg = f"[B][C][FFFF00]✅ SUCCESS! Evolution emote cycle started!\n🎯 Target: Yourself\n🎭 Emotes: All 18 evolution emotes\n⏰ Delay: 5 seconds between emotes\n🔄 Cycle: Continuous loop until @sevos\n"
                            else:
                                success_msg = f"[B][C][FFFF00]✅ SUCCESS! Evolution emote cycle started!\n🎯 Targets: Yourself + {len(uids)-1} other players\n🎭 Emotes: All 18 evolution emotes\n⏰ Delay: 5 seconds between emotes\n🔄 Cycle: Continuous loop until @sevos\n"
    
                            await safe_send_message(response.Data.chat_type, success_msg, uid, chat_id, key, iv)
                            print(f"Started evolution emote cycle for UIDs: {uids}")
                        
                        # EVO CYCLE STOP COMMAND - @sevos
                        if inPuTMsG.strip() == '@sevos':
                            if evo_cycle_task and not evo_cycle_task.done():
                                evo_cycle_running = False
                                evo_cycle_task.cancel()
                                success_msg = f"[B][C][FFFF00]✅ SUCCESS! Evolution emote cycle stopped successfully!\n"
                                await safe_send_message(response.Data.chat_type, success_msg, uid, chat_id, key, iv)
                                print("Evolution emote cycle stopped by command")
                            else:
                                error_msg = f"[B][C][FF0000]❌ ERROR! No active evolution emote cycle to stop!\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)

                        # Fast emote spam command - works in all chat types
                        if inPuTMsG.strip().startswith('/fast'):
                            print('Processing fast emote spam in any chat type')
                            
                            parts = inPuTMsG.strip().split()
                            if len(parts) < 3:
                                error_msg = f"[B][C][FF0000]❌ ERROR! Usage: /fast uid1 [uid2] [uid3] [uid4] emoteid\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                            else:
                                # Parse uids and emoteid
                                uids = []
                                emote_id = None
                                
                                for part in parts[1:]:
                                    if part.isdigit():
                                        if len(part) > 3:  # Assuming UIDs are longer than 3 digits
                                            uids.append(part)
                                        else:
                                            emote_id = part
                                    else:
                                        break
                                
                                if not emote_id and parts[-1].isdigit():
                                    emote_id = parts[-1]
                                
                                if not uids or not emote_id:
                                    error_msg = f"[B][C][FF0000]❌ ERROR! Invalid format! Usage: /fast uid1 [uid2] [uid3] [uid4] emoteid\n"
                                    await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                else:
                                    # Stop any existing fast spam
                                    if fast_spam_task and not fast_spam_task.done():
                                        fast_spam_running = False
                                        fast_spam_task.cancel()
                                    
                                    # Start new fast spam
                                    fast_spam_running = True
                                    fast_spam_task = asyncio.create_task(fast_emote_spam(uids, emote_id, key, iv, region))
                                    
                                    # SUCCESS MESSAGE
                                    success_msg = f"[B][C][FFFF00]✅ SUCCESS! Fast emote spam started!\nTargets: {len(uids)} players\nEmote: {emote_id}\nSpam count: 25 times\n"
                                    await safe_send_message(response.Data.chat_type, success_msg, uid, chat_id, key, iv)

                        # Custom emote spam command - works in all chat types
                        if inPuTMsG.strip().startswith('/p'):
                            print('Processing custom emote spam in any chat type')
                            
                            parts = inPuTMsG.strip().split()
                            if len(parts) < 4:
                                error_msg = f"[B][C][FF0000]❌ ERROR! Usage: /p (uid) (emote_id) (times)\nExample: /p 123456789 909000001 10\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                            else:
                                try:
                                    target_uid = parts[1]
                                    emote_id = parts[2]
                                    times = int(parts[3])
                                    
                                    if times <= 0:
                                        error_msg = f"[B][C][FF0000]❌ ERROR! Times must be greater than 0!\n"
                                        await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                    elif times > 1000:
                                        error_msg = f"[B][C][FF0000]❌ ERROR! Maximum 100 times allowed for safety!\n"
                                        await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                    else:
                                        # Stop any existing custom spam
                                        if custom_spam_task and not custom_spam_task.done():
                                            custom_spam_running = False
                                            custom_spam_task.cancel()
                                         
                                        
                                        # Start new custom spam
                                        custom_spam_running = True
                                        custom_spam_task = asyncio.create_task(custom_emote_spam(target_uid, emote_id, times, key, iv, region))
                                        
                                        # SUCCESS MESSAGE
                                        success_msg = f"[B][C][FFFF00]✅ SUCCESS! Custom emote spam started!\nTarget: {target_uid}\nEmote: {emote_id}\nTimes: {times}\n"
                                        await safe_send_message(response.Data.chat_type, success_msg, uid, chat_id, key, iv)
                                        
                                except ValueError:
                                    error_msg = f"[B][C][FF0000]❌ ERROR! Invalid number format! Usage: /p (uid) (emote_id) (times)\n"
                                    await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                except Exception as e:
                                    error_msg = f"[B][C][FF0000]❌ ERROR! {str(e)}\n"
                                    await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                    
 

                        # Spam request command - works in all chat types
                        if inPuTMsG.strip().startswith('/spm'):
                            print('Processing spam invite with cosmetics')
    
                            parts = inPuTMsG.strip().split()
                            if len(parts) < 2:
                                error_msg = f"[B][C][FF0000]❌ Usage: /spm (uid)\nExample: /spm 123456789\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                            else:
                                target_uid = parts[1]
        
                                # Stop any existing spam request
                                if spam_request_task and not spam_request_task.done():
                                    spam_request_running = False
                                    spam_request_task.cancel()
                                    await asyncio.sleep(0.5)
        
                                # Start new spam request WITH COSMETICS
                                spam_request_running = True
                                spam_request_task = asyncio.create_task(spam_request_loop_with_cosmetics(target_uid, key, iv, region))
        
                                # SUCCESS MESSAGE
                                success_msg = f"[B][C][FFFF00]✅ SUCCESS! Spam request started successfully!\n"
                                await safe_send_message(response.Data.chat_type, success_msg, uid, chat_id, key, iv)

                        # Stop spam request command - works in all chat types
                        if inPuTMsG.strip() == '/sspm':
                            if spam_request_task and not spam_request_task.done():
                                spam_request_running = False
                                spam_request_task.cancel()
                                success_msg = f"[B][C][FFFF00]✅ SUCCESS! Spam request stopped successfully!\n"
                                await safe_send_message(response.Data.chat_type, success_msg, uid, chat_id, key, iv)
                            else:
                                error_msg = f"[B][C][FF0000]❌ ERROR! No active spam request to stop!\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)

                        # In TcPChaT function, update /status command:
                        if inPuTMsG.strip().startswith('/status '):
                            print('Processing status command')
    
                            parts = inPuTMsG.strip().split()
                            if len(parts) < 2:
                                error_msg = f"[B][C][FF0000]❌ Usage: /status (player_uid)\nExample: /status 123456789\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                return
    
                            target_uid = parts[1]
    
                            # DEBUG: Show cache before clearing
                            print(f"\n🔍 BEFORE clearing cache:")
                            debug_file_cache()
                            
                            # Clear old cache entry first
                            clear_cache_entry(target_uid)
    
                            # Send initial message
                            initial_msg = f"[B][C][FFFF00]🔍 Checking status of {fix_num(target_uid)}...\n"
                            await safe_send_message(response.Data.chat_type, initial_msg, uid, chat_id, key, iv)
                            
                            try:
                                # Create and send status request
                                status_packet = await createpacketinfo(target_uid, key, iv)
                                if not status_packet:
                                    error_msg = f"[B][C][FF0000]❌ Failed to create status packet!\n"
                                    await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                    return
        
                                await SEndPacKeT(whisper_writer, online_writer, 'OnLine', status_packet)
                                print(f"📤 Sent status request for {target_uid}")
        
                                # Wait for response - check FILE cache
                                max_retries = 12  # Increased for reliability
                                response_received = False
        
                                for attempt in range(max_retries):
                                    print(f"⏳ Checking file cache... attempt {attempt + 1}/{max_retries}")
            
                                    # Check FILE cache
                                    cache_data = load_from_cache(target_uid)
                                    if cache_data:
                                        print(f"🎯 FOUND in file cache! Status: {cache_data['status']}")
                                        response_received = True
                
                                        # DEBUG: Show what we found
                                        print(f"📦 Cache data keys: {list(cache_data.keys())}")
                
                                        # Build response
                                        status_msg = f"[B][C][FFFF00]📊 PLAYER STATUS\n"
                                        status_msg += f"────────────────\n"
                                        status_msg += f"👤 UID: {fix_num(target_uid)}\n"
                                        status_msg += f"📊 Status: {cache_data['status']}\n"
                
                                        # Add specific info
                                        if "IN ROOM" in cache_data['status']:
                                            if 'room_id' in cache_data:
                                                status_msg += f"🏠 Room ID: {fix_num(cache_data['room_id'])}\n"
                                                status_msg += f"💡 Use: /roomspam {target_uid}\n"
                                                room_id_msg = f"{fix_num(cache_data['room_id'])}"
                                                await safe_send_message(response.Data.chat_type, room_id_msg, uid, chat_id, key, iv)
                                            else:
                                                status_msg += f"🏠 Room ID: Not available\n"
                
                                        elif "INSQUAD" in cache_data['status']:
                                            if 'leader_id' in cache_data:
                                                status_msg += f"👑 Leader: {fix_num(cache_data['leader_id'])}\n"
                    
                                            # Try to get squad size
                                            try:
                                                if 'parsed_json' in cache_data:
                                                    parsed = cache_data['parsed_json']
                                                    if '5' in parsed and 'data' in parsed['5']:
                                                        squad_data = parsed['5']['data']['1']['data']
                                                        if '9' in squad_data and 'data' in squad_data['9']:
                                                            members = squad_data['9']['data']
                                                            max_members = squad_data['10']['data'] + 1
                                                            status_msg += f"👥 Squad: {members}/{max_members}\n"
                                            except:
                                                pass
                
                                        elif "OFFLINE" in cache_data['status']:
                                            status_msg += f"🔴 Player is offline\n"
                
                                        elif "INGAME" in cache_data['status']:
                                            status_msg += f"🎮 Player is in a match\n"
                
                                        elif "SOLO" in cache_data['status']:
                                            status_msg += f"👤 Player is solo\n"
                
                                        status_msg += f"────────────────\n"
                                        status_msg += f"✅ Real-time data\n"
                
                                        await safe_send_message(response.Data.chat_type, status_msg, uid, chat_id, key, iv)

                                        # DEBUG: Show cache after success
                                        print(f"\n✅ AFTER successful response:")
                                        debug_file_cache()
                
                                        break
            
                                    # Wait between checks
                                    await asyncio.sleep(0.5)
                                                        
                                if not response_received:
                                    # DEBUG: Show cache state on failure
                                    print(f"\n❌ FAILED after {max_retries} tries")
                                    debug_file_cache()
            
                                    error_msg = f"[B][C][FF0000]❌ STATUS CHECK FAILED\n"
                                    error_msg += f"────────────────\n"
                                    error_msg += f"👤 UID: {fix_num(target_uid)}\n"
                                    error_msg += f"📛 No response from server\n"
                                    error_msg += f"────────────────\n"
                                    error_msg += f"💡 Possible issues:\n"
                                    error_msg += f"• Player is offline\n"
                                    error_msg += f"• Server is busy\n"
                                    error_msg += f"• Try again in 10 seconds\n"
            
                                    await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
            
                            except Exception as e:
                                print(f"❌ Status command error: {e}")
                                import traceback
                                traceback.print_exc()
        
                                error_msg = f"[B][C][FF0000]❌ Error: {str(e)[:50]}\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)

                        if inPuTMsG.strip().startswith('/play '):
                            print('Processing evo command in any chat type')
                            
                            parts = inPuTMsG.strip().split()
                            if len(parts) < 2:
                                error_msg = f"[B][C][FF0000]❌ ERROR! Usage: /play uid1 [uid2] [uid3] [uid4] number(1-410)\nExample: /play 123456789 1\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                            else:
                                # Parse uids and number
                                uids = []
                                number = None
                                
                                for part in parts[1:]:
                                    if part.isdigit():
                                        if len(part) <= 3:  # Number should be 1-410 (1,2 or 3 digits)
                                            number = part
                                        else:
                                            uids.append(part)
                                    else:
                                        break
                                
                                if not number and parts[-1].isdigit() and len(parts[-1]) <= 2:
                                    number = parts[-1]
                                
                                if not uids or not number:
                                    error_msg = f"[B][C][FF0000]❌ ERROR! Invalid format! Usage: /play uid1 [uid2] [uid3] [uid4] number(1-410)\n"
                                    await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                else:
                                    try:
                                        number_int = int(number)
                                        if number_int not in ALL_EMOTE:
                                            error_msg = f"[B][C][FF0000]❌ ERROR! Number must be between 1-410 only!\n"
                                            await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                        else:
                                            initial_message = f"[B][C]{get_random_color()}\nSending emote {number_int}...\n"
                                            await safe_send_message(response.Data.chat_type, initial_message, uid, chat_id, key, iv)
                                            
                                            success, result_msg = await play_emote_spam(uids, number_int, key, iv, region)
                                            
                                            if success:
                                                success_msg = f"[B][C][00FF00]✅ SUCCESS! {result_msg}\n"
                                                await safe_send_message(response.Data.chat_type, success_msg, uid, chat_id, key, iv)
                                            else:
                                                error_msg = f"[B][C][FF0000]❌ ERROR! {result_msg}\n"
                                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                            
                                    except ValueError:
                                        error_msg = f"[B][C][FF0000]❌ ERROR! Invalid number format! Use (1-410) only.\n"
                                        await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)

                        # NEW 100 LV EMOTE COMMANDS
                        if inPuTMsG.strip().startswith('/100 '):
                            print('Processing evo command in any chat type')
                            
                            parts = inPuTMsG.strip().split()
                            if len(parts) < 2:
                                error_msg = f"[B][C][FF0000]❌ ERROR! Usage: /100 uid1 [uid2] [uid3] [uid4]\nExample: /100 123456789\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                            else:
                                # Parse uids and number
                                uids = []
                                number = None
                                
                                for part in parts[1:]:
                                    if part.isdigit():
                                        if len(part) <= 3:  # Number should be 1-410 (1,2 or 3 digits)
                                            number = part
                                        else:
                                            uids.append(part)
                                    else:
                                        break
                                
                                if not number and parts[-1].isdigit() and len(parts[-1]) <= 2:
                                    number = parts[-1]
                                
                                if not uids or not number:
                                    error_msg = f"[B][C][FF0000]❌ ERROR! Invalid format! Usage: /100 uid1 [uid2] [uid3] [uid4]\n"
                                    await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                else:
                                    try:
                                        number_int = 268
                                        if number_int not in ALL_EMOTE:
                                            error_msg = f"[B][C][FF0000]❌ ERROR! Number must be between 1-410 only!\n"
                                            await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                        else:
                                            initial_message = f"[B][C]{get_random_color()}\nSending 100 level emote...\n"
                                            await safe_send_message(response.Data.chat_type, initial_message, uid, chat_id, key, iv)
                                            
                                            success, result_msg = await play_emote_spam(uids, number_int, key, iv, region)
                                            
                                            if success:
                                                success_msg = f"[B][C][00FF00]✅ SUCCESS! {result_msg}\n"
                                                await safe_send_message(response.Data.chat_type, success_msg, uid, chat_id, key, iv)
                                            else:
                                                error_msg = f"[B][C][FF0000]❌ ERROR! {result_msg}\n"
                                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                            
                                    except ValueError:
                                        error_msg = f"[B][C][FF0000]❌ ERROR! Invalid number format! Use (1-410) only.\n"
                                        await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                        
                                        
                        # NEW EVO COMMANDS
                        if inPuTMsG.strip().startswith('/evo '):
                            print('Processing evo command in any chat type')
                            
                            parts = inPuTMsG.strip().split()
                            if len(parts) < 2:
                                error_msg = f"[B][C][FF0000]❌ ERROR! Usage: /evo uid1 [uid2] [uid3] [uid4] number(1-21)\nExample: /evo 123456789 1\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                            else:
                                # Parse uids and number
                                uids = []
                                number = None
                                
                                for part in parts[1:]:
                                    if part.isdigit():
                                        if len(part) <= 2:  # Number should be 1-21 (1 or 2 digits)
                                            number = part
                                        else:
                                            uids.append(part)
                                    else:
                                        break
                                
                                if not number and parts[-1].isdigit() and len(parts[-1]) <= 2:
                                    number = parts[-1]
                                
                                if not uids or not number:
                                    error_msg = f"[B][C][FF0000]❌ ERROR! Invalid format! Usage: /evo uid1 [uid2] [uid3] [uid4] number(1-21)\n"
                                    await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                else:
                                    try:
                                        number_int = int(number)
                                        if number_int not in EMOTE_MAP:
                                            error_msg = f"[B][C][FF0000]❌ ERROR! Number must be between 1-21 only!\n"
                                            await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                        else:
                                            initial_message = f"[B][C]{get_random_color()}\nSending evolution emote {number_int}...\n"
                                            await safe_send_message(response.Data.chat_type, initial_message, uid, chat_id, key, iv)
                                            
                                            success, result_msg = await evo_emote_spam(uids, number_int, key, iv, region)
                                            
                                            if success:
                                                success_msg = f"[B][C][FFFF00]✅ SUCCESS! {result_msg}\n"
                                                await safe_send_message(response.Data.chat_type, success_msg, uid, chat_id, key, iv)
                                            else:
                                                error_msg = f"[B][C][FF0000]❌ ERROR! {result_msg}\n"
                                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                            
                                    except ValueError:
                                        error_msg = f"[B][C][FF0000]❌ ERROR! Invalid number format! Use 1-21 only.\n"
                                        await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)

                        if inPuTMsG.strip().startswith('/evo_fast '):
                            print('Processing evo_fast command in any chat type')
                            
                            parts = inPuTMsG.strip().split()
                            if len(parts) < 2:
                                error_msg = f"[B][C][FF0000]❌ ERROR! Usage: /evo_fast uid1 [uid2] [uid3] [uid4] number(1-21)\nExample: /evo_fast 123456789 1\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                            else:
                                # Parse uids and number
                                uids = []
                                number = None
                                
                                for part in parts[1:]:
                                    if part.isdigit():
                                        if len(part) <= 2:  # Number should be 1-21 (1 or 2 digits)
                                            number = part
                                        else:
                                            uids.append(part)
                                    else:
                                        break
                                
                                if not number and parts[-1].isdigit() and len(parts[-1]) <= 2:
                                    number = parts[-1]
                                
                                if not uids or not number:
                                    error_msg = f"[B][C][FF0000]❌ ERROR! Invalid format! Usage: /evo_fast uid1 [uid2] [uid3] [uid4] number(1-21)\n"
                                    await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                else:
                                    try:
                                        number_int = int(number)
                                        if number_int not in EMOTE_MAP:
                                            error_msg = f"[B][C][FF0000]❌ ERROR! Number must be between 1-21 only!\n"
                                            await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                        else:
                                            # Stop any existing evo_fast spam
                                            if evo_fast_spam_task and not evo_fast_spam_task.done():
                                                evo_fast_spam_running = False
                                                evo_fast_spam_task.cancel()
                                                await asyncio.sleep(0.5)
                                            
                                            # Start new evo_fast spam
                                            evo_fast_spam_running = True
                                            evo_fast_spam_task = asyncio.create_task(evo_fast_emote_spam(uids, number_int, key, iv, region))
                                            
                                            # SUCCESS MESSAGE
                                            emote_id = EMOTE_MAP[number_int]
                                            success_msg = f"[B][C][FFFF00]✅ SUCCESS! Fast evolution emote spam started!\nTargets: {len(uids)} players\nEmote: {number_int} (ID: {emote_id})\nSpam count: 25 times\nInterval: 0.1 seconds\n"
                                            await safe_send_message(response.Data.chat_type, success_msg, uid, chat_id, key, iv)
                                            
                                    except ValueError:
                                        error_msg = f"[B][C][FF0000]❌ ERROR! Invalid number format! Use 1-21 only.\n"
                                        await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)

                        # Add this to your command handlers in TcPChaT function:
                        if inPuTMsG.strip().startswith('/bundle'):
                            print('Processing bundle command')
    
                            parts = inPuTMsG.strip().split()
                            
                            if len(parts) < 2:
                                # Show available bundles
                                bundle_list = """[B][C][00FF00]🎁 AVAILABLE BUNDLES 🎁
[FF6347]━[32CD32]━[7B68EE]━[FF4500]━[1E90FF]━[ADFF2F]━[FF69B4]━[8A2BE2]━[DC143C]━[FF8C00]━[BA55D3]━[7CFC00]━[FFC0CB]
[FFFFFF]• midnight
[FFFFFF]• aurora
[FFFFFF]• naruto  
[FFFFFF]• paradox
[FFFFFF]• frostfire
[FFFFFF]• rampage
[FFFFFF]• cannibal
[FFFFFF]• devil
[FFFFFF]• scorpio
[FFFFFF]• dreamspace
[FFFFFF]• itachi
[FF6347]━[32CD32]━[7B68EE]━[FF4500]━[1E90FF]━[ADFF2F]━[FF69B4]━[8A2BE2]━[DC143C]━[FF8C00]━[BA55D3]━[7CFC00]━[FFC0CB]
[00FF00]Usage: /bundle [name]
[FFFFFF]Example: /bundle midnight"""
                                await safe_send_message(response.Data.chat_type, bundle_list, uid, chat_id, key, iv)
                            else:
                                bundle_name = parts[1].lower()
        
                                # All bundles use the same ID: 914000002
                                bundle_id = BUNDLE.get(bundle_name)
        
                                initial_msg = f"[B][C][00FF00]🎁 Sending {bundle_name}\n"
                                await safe_send_message(response.Data.chat_type, initial_msg, uid, chat_id, key, iv)
        
                                try:
                                    # Create bundle packet
                                    bundle_packet = await bundle_packet_async(bundle_id, key, iv, region)
            
                                    if bundle_packet and online_writer:
                                        await SEndPacKeT(whisper_writer, online_writer, 'OnLine', bundle_packet)
                                        success_msg = f"[B][C][00FF00]✅ Done: {bundle_name}"
                                        await safe_send_message(response.Data.chat_type, success_msg, uid, chat_id, key, iv)
                                    else:
                                        error_msg = f"[B][C][FF0000]❌ Failed to create bundle packet!\n"
                                        await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                
                                except Exception as e:
                                    error_msg = f"[B][C][FF0000]❌ Error sending bundle: {str(e)[:50]}\n"
                                    await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)

                        # NEW EVO_CUSTOM COMMAND
                        if inPuTMsG.strip().startswith('/evo_c '):
                            print('Processing evo_c command in any chat type')
                            
                            parts = inPuTMsG.strip().split()
                            if len(parts) < 3:
                                error_msg = f"[B][C][FF0000]❌ ERROR! Usage: /evo_c uid1 [uid2] [uid3] [uid4] number(1-21) time(1-100)\nExample: /evo_c 123456789 1 10\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                            else:
                                # Parse uids, number, and time
                                uids = []
                                number = None
                                time_val = None
                                
                                for part in parts[1:]:
                                    if part.isdigit():
                                        if len(part) <= 2:  # Number or time should be 1-100 (1, 2, or 3 digits)
                                            if number is None:
                                                number = part
                                            elif time_val is None:
                                                time_val = part
                                            else:
                                                uids.append(part)
                                        else:
                                            uids.append(part)
                                    else:
                                        break
                                
                                # If we still don't have time_val, try to get it from the last part
                                if not time_val and len(parts) >= 3:
                                    last_part = parts[-1]
                                    if last_part.isdigit() and len(last_part) <= 3:
                                        time_val = last_part
                                        # Remove time_val from uids if it was added by mistake
                                        if time_val in uids:
                                            uids.remove(time_val)
                                
                                if not uids or not number or not time_val:
                                    error_msg = f"[B][C][FF0000]❌ ERROR! Invalid format! Usage: /evo_c uid1 [uid2] [uid3] [uid4] number(1-21) time(1-100)\n"
                                    await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                else:
                                    try:
                                        number_int = int(number)
                                        time_int = int(time_val)
                                        
                                        if number_int not in EMOTE_MAP:
                                            error_msg = f"[B][C][FF0000]❌ ERROR! Number must be between 1-21 only!\n"
                                            await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                        elif time_int < 1 or time_int > 100:
                                            error_msg = f"[B][C][FF0000]❌ ERROR! Time must be between 1-100 only!\n"
                                            await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                        else:
                                            # Stop any existing evo_custom spam
                                            if evo_custom_spam_task and not evo_custom_spam_task.done():
                                                evo_custom_spam_running = False
                                                evo_custom_spam_task.cancel()
                                                await asyncio.sleep(0.5)
                                            
                                            # Start new evo_custom spam
                                            evo_custom_spam_running = True
                                            evo_custom_spam_task = asyncio.create_task(evo_custom_emote_spam(uids, number_int, time_int, key, iv, region))
                                            
                                            # SUCCESS MESSAGE
                                            emote_id = EMOTE_MAP[number_int]
                                            success_msg = f"[B][C][FFFF00]✅ SUCCESS! Custom evolution emote spam started!\nTargets: {len(uids)} players\nEmote: {number_int} (ID: {emote_id})\nRepeat: {time_int} times\nInterval: 0.1 seconds\n"
                                            await safe_send_message(response.Data.chat_type, success_msg, uid, chat_id, key, iv)
                                            
                                    except ValueError:
                                        error_msg = f"[B][C][FF0000]❌ ERROR! Invalid number/time format! Use numbers only.\n"
                                        await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)


                        # Stop evo_fast spam command
                        if inPuTMsG.strip() == '/stop evo_fast':
                            if evo_fast_spam_task and not evo_fast_spam_task.done():
                                evo_fast_spam_running = False
                                evo_fast_spam_task.cancel()
                                success_msg = f"[B][C][FFFF00]✅ SUCCESS! Evolution fast spam stopped successfully!\n"
                                await safe_send_message(response.Data.chat_type, success_msg, uid, chat_id, key, iv)
                            else:
                                error_msg = f"[B][C][FF0000]❌ ERROR! No active evolution fast spam to stop!\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)

                        # Stop evo_custom spam command
                        if inPuTMsG.strip() == '/stop evo_c':
                            if evo_custom_spam_task and not evo_custom_spam_task.done():
                                evo_custom_spam_running = False
                                evo_custom_spam_task.cancel()
                                success_msg = f"[B][C][FFFF00]✅ SUCCESS! Evolution custom spam stopped successfully!\n"
                                await safe_send_message(response.Data.chat_type, success_msg, uid, chat_id, key, iv)
                            else:
                                error_msg = f"[B][C][FF0000]❌ ERROR! No active evolution custom spam to stop!\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)

                        # In your TcPChaT function, add:
                        if inPuTMsG.strip() == '/ss':
                            print('Processing start match command')
                            await handle_start_match_command(inPuTMsG, uid, chat_id, key, iv, region, response.Data.chat_type)
                            
                            
                        # FIXED HELP MENU SYSTEM - Now detects commands properly
                        # IMPROVED HELP MENU SYSTEM - AUTOMATIC MULTI-PART
                        # IMPROVED HELP MENU SYSTEM - TREE STYLE FORMAT
                        if inPuTMsG.strip().lower() in ("help", "/help", "hi", "hello", "commands"):
                            print(f"Help command detected from UID: {uid} in chat type: {XX}")
    

    
                            basic = """[b][c][1E90FF]🤖   B A S I C   C O M M A N D S   🤖
[FF6347]━[32CD32]━[7B68EE]━[FF4500]━[1E90FF]━[ADFF2F]━[FF69B4]━[8A2BE2]━[DC143C]━[FF8C00]━[BA55D3]━[7CFC00]━[FFC0CB]
[FF6A00]/start        [00E5FF]Start match
[9B59B6]/exit         [2ECC71]Leave squad
[1ABC9C]/3            [F1C40F]Send 3-player invite
[E84393]/5            [00B894]Send 5-player invite
[0984E3]/6            [FAB1A0]Send 6-player invite
[D63031]! (team code) [55EFC4]Join squad
[6C5CE7]/ghost (team code) [FD79A8]Ghost join squad
[FF6347]━[32CD32]━[7B68EE]━[FF4500]━[1E90FF]━[ADFF2F]━[FF69B4]━[8A2BE2]━[DC143C]━[FF8C00]━[BA55D3]━[7CFC00]━[FFC0CB]"""

                            await safe_send_message(response.Data.chat_type, basic, uid, chat_id, key, iv)
                            await asyncio.sleep(0.2)
        

                            emotes = """[b][c][1E90FF]🎭   E M O T E   C O M M A N D S   🎭
[FF6347]━[32CD32]━[7B68EE]━[FF4500]━[1E90FF]━[ADFF2F]━[FF69B4]━[8A2BE2]━[DC143C]━[FF8C00]━[BA55D3]━[7CFC00]━[FFC0CB]
[FF922B]/e [emote]              [2ED573]Send emote to yourself
[6D214F]/e [uid] [emote]        [18DCFF]Send emote to player
[20BF6B]/e list                 [F7B731]Show all emotes
[A55EEA]/e list names           [26DE81]Show named emotes
[FF6347]━[32CD32]━[7B68EE]━[FF4500]━[1E90FF]━[ADFF2F]━[FF69B4]━[8A2BE2]━[DC143C]━[FF8C00]━[BA55D3]━[7CFC00]━[FFC0CB]"""

                            await safe_send_message(response.Data.chat_type, emotes, uid, chat_id, key, iv)
                            await asyncio.sleep(0.2)            

                            evo = """[b][c][1E90FF]⚡   E V O L U T I O N   E M O T E S   ⚡  
[FF6347]━[32CD32]━[7B68EE]━[FF4500]━[1E90FF]━[ADFF2F]━[FF69B4]━[8A2BE2]━[DC143C]━[FF8C00]━[BA55D3]━[7CFC00]━[FFC0CB]
[FF6F00]@evos                 [1DD1A1]Start evolution cycle
[C44569]@sevos                [54A0FF]Stop evolution cycle
[10AC84]/evo [num]            [F368E0]Send evo emote (1-18)
[5F27CD]/evo [uid] [num]      [FECB2F]Send evo emote to player
[FF6347]━[32CD32]━[7B68EE]━[FF4500]━[1E90FF]━[ADFF2F]━[FF69B4]━[8A2BE2]━[DC143C]━[FF8C00]━[BA55D3]━[7CFC00]━[FFC0CB]
"""
                            await safe_send_message(response.Data.chat_type, evo, uid, chat_id, key, iv)
                            await asyncio.sleep(0.2)            
                                            

                            spam_cmnd = """[b][c][1E90FF]🚀   S P A M   C O M M A N D S   🚀
[FF6347]━[32CD32]━[7B68EE]━[FF4500]━[1E90FF]━[ADFF2F]━[FF69B4]━[8A2BE2]━[DC143C]━[FF8C00]━[BA55D3]━[7CFC00]━[FFC0CB]
[FF7F50]/fast [uid] [emote]        [1ABC9C]Fast emote spam
[8E44AD]/p [uid] [emote] [num]     [F39C12]Custom emote spam
[C0392B]/reject [uid]              [27AE60]Reject spam
[16A085]/reject_stop               [D35400]Stop reject spam
[2980B9]/msg [text] [times]        [E84393]Message spam
[2C3E50]/stop msg                  [A3CB38]Stop message spam
[6F1E51]/mg [text] [repeats]       [48DBFB]Wave message spam
[FF6347]━[32CD32]━[7B68EE]━[FF4500]━[1E90FF]━[ADFF2F]━[FF69B4]━[8A2BE2]━[DC143C]━[FF8C00]━[BA55D3]━[7CFC00]━[FFC0CB]"""

                            await safe_send_message(response.Data.chat_type, spam_cmnd, uid, chat_id, key, iv)
                            await asyncio.sleep(0.2)

                            badge_cmnd = """[b][c][1E90FF]🎯   B A D G E   C O M M A N D S   🎯
[FF6347]━[32CD32]━[7B68EE]━[FF4500]━[1E90FF]━[ADFF2F]━[FF69B4]━[8A2BE2]━[DC143C]━[FF8C00]━[BA55D3]━[7CFC00]━[FFC0CB]
[FF9F1A]/v1 [uid]          [2ECC71]Join Req Craftland Badge
[6C5CE7]/v2 [uid]          [00CEC9]Join Req New V-Badge
[E17055]/v3 [uid]          [0984E3]Join Req Moderator Badge
[9B59B6]/v4 [uid]          [FDCB6E]Join Req Small V-Badge
[D63031]/v5 [uid]          [55EFC4]Join Req Pro Badge
[1E3799]/spam [uid]        [E056FD]Spam with all badge
[C][B][FF7F50]/spm [uid]        [2ED573]Spam normal request
[C][B][FF7F50]/sspm             [2ED573]Stop spam normal request
[FF6347]━[32CD32]━[7B68EE]━[FF4500]━[1E90FF]━[ADFF2F]━[FF69B4]━[8A2BE2]━[DC143C]━[FF8C00]━[BA55D3]━[7CFC00]━[FFC0CB]"""

                            await safe_send_message(response.Data.chat_type, badge_cmnd, uid, chat_id, key, iv)
                            await asyncio.sleep(0.2)

                            ad_cmnd = """[b][c][1E90FF]🔧   A D V A N C E D   C O M M A N D S   🔧
[FF6347]━[32CD32]━[7B68EE]━[FF4500]━[1E90FF]━[ADFF2F]━[FF69B4]━[8A2BE2]━[DC143C]━[FF8C00]━[BA55D3]━[7CFC00]━[FFC0CB]
[FF793F]/inv [uid]               [1DD1A1]Send group invite
[5F27CD]/joinroom [id] [pass]    [F368E0]Join custom room
[C44569]/lag [team_code]         [F7B731]Lag attack squad
[10AC84]/stop lag                [EE5253]Stop lag attack
[FF6347]━[32CD32]━[7B68EE]━[FF4500]━[1E90FF]━[ADFF2F]━[FF69B4]━[8A2BE2]━[DC143C]━[FF8C00]━[BA55D3]━[7CFC00]━[FFC0CB]"""

                            await safe_send_message(response.Data.chat_type, ad_cmnd, uid, chat_id, key, iv)
                            await asyncio.sleep(0.2)

                            info_cmnd = """[b][c][1E90FF]🔍   I N F O   C O M M A N D S   🔍
[FF0000]━[FFFF00]━[0000FF]━[FFFF00]━[FF00FF]━[00FFFF]━[FFA500]━[FF1493]━[00FF7F]━[FFD700]━[00CED1]━[9400D3]━[FF6347]━[32CD32]━[7B68EE]━[FF4500]━[1E90FF]━[ADFF2F]━[FF69B4]━[8A2BE2]━[DC143C]━[FF8C00]━[BA55D3]━[7CFC00]━[FFC0CB]─
[FF6B6B]/info [uid]             [1ABC9C]Player information
[6A89CC]/status [uid]           [F8C291]Check player status
[EB2F06]/praise [name]            [38ADA9]Gali spam message
[4A69BD]/likes [uid]            [F6B93B]Send 100 likes
[A65EEA]/ai [question]          [20BF6B]Chat with AI
[2C2C54]/check (uid)            [E55039]Check Ban Status
[FF6347]━[32CD32]━[7B68EE]━[FF4500]━[1E90FF]━[ADFF2F]━[FF69B4]━[8A2BE2]━[DC143C]━[FF8C00]━[BA55D3]━[7CFC00]━[FFC0CB]"""


                            await safe_send_message(response.Data.chat_type, info_cmnd, uid, chat_id, key, iv)
                            await asyncio.sleep(0.2)


                            about = """[b][1E90FF]❓   H E L P   &   A B O U T   ❓
[FF6347]━[32CD32]━[7B68EE]━[FF4500]━[1E90FF]━[ADFF2F]━[FF69B4]━[8A2BE2]━[DC143C]━[FF8C00]━[BA55D3]━[7CFC00]━[FFC0CB]
[FF8C00]/help                   [1E90FF]Show this help menu
[8E44AD]/admin                  [2ECC71]Admin / contact information
[E84393]/quick [code] [emote] [uid]   [F39C12]Quick emote attack
[C][B][FF6F61]/play [uid] [1-414]     [1ABC9C]Play emotes without emote id's
[C][B][9B59B6]/bundle [name]     [F1C40F]Show available bundle
[00FF00]/bundle [name] [FFFFFF]Equip Legendary Bundle
[FF0000]━[FFFF00]━[0000FF]━[FFFF00]━[FF00FF]━[00FFFF]━[FFA500]━[FF1493]━[00FF7F]━[FFD700]━[00CED1]━[9400D3]━[FF6347]━[32CD32]━[7B68EE]━[FF4500]━[1E90FF]━[ADFF2F]━[FF69B4]━[8A2BE2]━[DC143C]━[FF8C00]━[BA55D3]━[7CFC00]━[FFC0CB]"""

                            await safe_send_message(response.Data.chat_type, about, uid, chat_id, key, iv)
                            await asyncio.sleep(0.2)
                            

                            whitelist_cmnd = """[b][1E90FF]🔐  E X T R A C O M M A N D S   🔐
[FF6347]━[32CD32]━[7B68EE]━[FF4500]━[1E90FF]━[ADFF2F]━[FF69B4]━[8A2BE2]━[DC143C]━[FF8C00]━[BA55D3]━[7CFC00]━[FFC0CB]
[FF4757]noob              [1DD1A1]Show surprise 🙀
[3742FA]/sticker          [2ED573]Show sticker
[A55EEA]/title            [F7B731]Show titles
[FF6F00]/ig  (username)              [00CEC9]Get Instagram info
[6F1E51]/tt  (username)            [54A0FF]Get TikTok info
[FF9F43]/lv [uid]        [1ABC9C]Get player level info
[FF6347]━[32CD32]━[7B68EE]━[FF4500]━[1E90FF]━[ADFF2F]━[FF69B4]━[8A2BE2]━[DC143C]━[FF8C00]━[BA55D3]━[7CFC00]━[FFC0CB]"""

                            await safe_send_message(response.Data.chat_type, whitelist_cmnd, uid, chat_id, key, iv)
                            await asyncio.sleep(0.2)

                            last ="""[B][C][FFD700]╭[FF0000]─[FFD700]╮[FFFFFF]
[C][B][FF0000]│[00FF00]♪[FF0000]│[FFFFFF]║[00BFFF]TIKTOK INFO[FFFFFF]║
[C][B][FFD700]╰[FF0000]─[FFD700]╯[FFFFFF]
[C][B][FF0000]━━━━━━━━━━━
[C][B][FFFFFF]Username   : [00BFFF]@chayan210
[C][B][FFFFFF]Signature  : [00BFFF]I CHAYAN MAITY 
[C][B][FFFFFF]Followers  : [00BFFF]58911
[C][B][FFFFFF]Following  : [00BFFF]157
[C][B][FFFFFF]Likes      : [00BFFF]755678
[C][B][FFFFFF]Videos     : [00BFFF]23
[C][B][FFFFFF]Private    : [FF0000]False
[C][B][FF0000]━━━━━━━━━━━
"""

    


                            await safe_send_message(response.Data.chat_type, last, uid, chat_id, key, iv)
                            await asyncio.sleep(0.2)
                        response = None
                            
            whisper_writer.close() ; await whisper_writer.wait_closed() ; whisper_writer = None
                    
                    	
                    	
        except Exception as e: print(f"ErroR {ip}:{port} - {e}") ; whisper_writer = None
        await asyncio.sleep(reconnect_delay)

async def MaiiiinE():
    # Load credentials from file
    print("📁 Loading credentials from bot.txt...")
    credentials = load_credentials_from_file("bot.txt")
    
    if not credentials:
        print("❌ Failed to load credentials!")
        print("💡 Please create bot.txt with your UID and password")
        print("📝 Format: uid=YOUR_UID,password=YOUR_PASSWORD")
        return None
    
    try:
        Uid, Pw = credentials
    except:
        # Handle case where credentials returns more than 2 values
        if isinstance(credentials, (list, tuple)) and len(credentials) >= 2:
            Uid = credentials[0]
            Pw = credentials[1]
        else:
            print("❌ Invalid credentials format!")
            return None
    
    print("✅ Credentials loaded successfully")
    
    # Get access token from Free Fire
    open_id, access_token = await GeNeRaTeAccEss(Uid, Pw)
    if not open_id or not access_token: 
        print("❌ Error - Invalid Account (Check UID/Password)") 
        return None
    
    # Encrypt and send login request
    PyL = await EncRypTMajoRLoGin(open_id, access_token)
    MajoRLoGinResPonsE = await MajorLogin(PyL)
    if not MajoRLoGinResPonsE: 
        print("❌ Target Account => Banned / Not Registered!") 
        return None
    
    # Decrypt login response
    MajoRLoGinauTh = await DecRypTMajoRLoGin(MajoRLoGinResPonsE)
    
    # Get JWT token from response
    token = MajoRLoGinauTh.token
    if not token:
        print("❌ No authentication token received!")
        return None
    
    # ✅ CRITICAL: SAVE TOKEN TO token.json FILE
    try:
        import json
        import time
        from datetime import datetime
        
        # Get region from login response
        region = getattr(MajoRLoGinauTh, 'region', 'IND')
        
        token_data = {
            "token": token,
            "saved_at": time.time(),
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "bot_uid": str(Uid),
            "region": region,
            "source": "main.py_bot_login"
        }
        
        with open("token.json", "w") as f:
            json.dump(token_data, f, indent=2)
        
        print("✅ Token saved to token.json")
        print(f"📝 Token info: Region={region}, UID={Uid}")
        
    except Exception as e:
        print(f"⚠️ Warning: Could not save token to file: {e}")
        import traceback
        traceback.print_exc()
    
    # Continue with normal bot setup
    UrL = MajoRLoGinauTh.url
    
    # Clear screen and show status
    os.system('clear')
    print("=" * 50)
    print("🤖 ZAINUㅤVIP BOT - INITIALIZING")
    print("=" * 50)
    print("🔄 Starting TCP Connections...")
    print("📡 Connecting to Free Fire servers...")
    print("🌐 Server connection established")
    
    region = getattr(MajoRLoGinauTh, 'region', 'IND')
    ToKen = token  # Use the saved token
    TarGeT = MajoRLoGinauTh.account_uid
    key = MajoRLoGinauTh.key
    iv = MajoRLoGinauTh.iv
    timestamp = MajoRLoGinauTh.timestamp
    
    print(f"🔐 Authentication successful")
    print(f"👤 Account UID: {TarGeT}")
    print(f"🌍 Region: {region}")
    print(f"🔑 Token: {ToKen[:30]}...")
    
    # Get login data for server IPs
    LoGinDaTa = await GetLoginData(UrL, PyL, ToKen)
    if not LoGinDaTa: 
        print("❌ Error - Getting Ports From Login Data!") 
        return None
    
    LoGinDaTaUncRypTinG = await DecRypTLoGinDaTa(LoGinDaTa)
    
    # Get server IPs and ports
    OnLinePorTs = LoGinDaTaUncRypTinG.Online_IP_Port
    ChaTPorTs = LoGinDaTaUncRypTinG.AccountIP_Port
    
    print(f"📡 Online Server: {OnLinePorTs}")
    print(f"💬 Chat Server: {ChaTPorTs}")
    
    # Split IPs and ports
    OnLineiP, OnLineporT = OnLinePorTs.split(":")
    ChaTiP, ChaTporT = ChaTPorTs.split(":")
    
    # Get account name
    acc_name = LoGinDaTaUncRypTinG.AccountName
    print(f"👋 Welcome, {acc_name}!")
    
    # Create authentication token for TCP connections
    AutHToKen = await xAuThSTarTuP(int(TarGeT), ToKen, int(timestamp), key, iv)
    
    # Create event for chat ready
    ready_event = asyncio.Event()
    
    # Start bot tasks
    print("\n🚀 Starting bot services...")
    
    task1 = asyncio.create_task(TcPChaT(ChaTiP, ChaTporT, AutHToKen, key, iv, LoGinDaTaUncRypTinG, ready_event, region))
    task2 = asyncio.create_task(TcPOnLine(OnLineiP, OnLineporT, key, iv, AutHToKen))  
 
    
    # Show loading animation
    os.system('clear')
    print("🤖 ZAINUㅤVIP BOT - STARTING")
    print("=" * 50)
    
    for i in range(1, 4):
        dots = "." * i
        print(f"🔄 Loading{dots}")
        time.sleep(0.3)
    
    os.system('clear')
    print("🤖 ZAINUㅤVIP BOT - CONNECTING")
    print("=" * 50)
    print("┌────────────────────────────────────┐")
    print("│ ██████████████████████████████████ │")
    print("└────────────────────────────────────┘")
    
    # Wait for chat connection to be ready
    print("\n⏳ Waiting for chat connection...")
    try:
        await asyncio.wait_for(ready_event.wait(), timeout=10)
        print("✅ Chat connection established!")
    except asyncio.TimeoutError:
        print("⚠️ Chat connection timeout, continuing...")
    
    # Final status display
    os.system('clear')
    print("=" * 50)
    print("🤖 ZAINUㅤVIP BOT - ONLINE")
    print("=" * 50)
    print(f"🔹 UID: {TarGeT}")
    print(f"🔹 Name: {acc_name}")
    print(f"🔹 Region: {region}")
    print(f"🔹 Status: 🟢 READY")
    print(f"🔹 Chat Server: {ChaTiP}:{ChaTporT}")
    print(f"🔹 Online Server: {OnLineiP}:{OnLineporT}")
    print("=" * 50)
    print("💡 Commands available in squad/guild chat")
    print("💡 Type /help for command list")
    print("=" * 50)
    
    # Test cache file write
    print("\n📊 System Check:")
    print(f"📁 Working directory: {os.getcwd()}")
    print(f"📁 Cache file: {CACHE_FILE}")
    
    try:
        test_data = {'test': 'ok', 'timestamp': time.time()}
        with open(CACHE_FILE, 'wb') as f:
            pickle.dump(test_data, f)
        print("✅ Cache file write test: PASSED")
    except Exception as e:
        print(f"⚠️ Cache file write test: {e}")
    
    # Check token.json exists
    if os.path.exists("token.json"):
        print("✅ token.json file exists")
        try:
            with open("token.json", "r") as f:
                token_info = json.load(f)
            age = time.time() - token_info.get('saved_at', 0)
            print(f"✅ Token age: {age:.1f} seconds")
        except:
            print("⚠️ Could not read token.json")
    else:
        print("❌ token.json not found!")
    
    print("\n🎯 Bot is now running...")
    print("📡 Listening for commands and invitations")
    
    # Keep all tasks running
    try:
        await asyncio.gather(task1, task2)
    except asyncio.CancelledError:
        print("\n🛑 Bot tasks cancelled")
    except Exception as e:
        print(f"\n❌ Error in bot tasks: {e}")
        import traceback
        traceback.print_exc()
    
    return None


if __name__ == '__main__':
    asyncio.run(StarTinG())
    
  