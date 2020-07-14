# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
import json
import os

def get_user_list(config, key):
    with open('{}/tg_bot/{}'.format(os.getcwd(), config), 'r') as json_file:
        return json.load(json_file)[key]


# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
class Config(object):
    LOGGER = True

    # REQUIRED
    API_KEY = 1012018820:AAF6XjqHCxWrR7cI_AE-woEws_WH7Cvjsxk
    OWNER_ID = 887023254
    OWNER_USERNAME = @Light_bring_er

    # RECOMMENDED
    SQLALCHEMY_DATABASE_URI =
    MESSAGE_DUMP = None  # 1233333333
    GBAN_LOGS = @bgfhjygbj
    LOAD = []
    NO_LOAD = ['translation', 'rss']   
    WEBHOOK = False ANYTHING 
    URL = None

    # OPTIONAL
    #ID Seperation format [1,2,3,4]
    SUDO_USERS = [964158165 1227877179 794636595 883281262 1299182841 723100827]
    DEV_USERS = 887023254
    SUPPORT_USERS = [964158165 1227877179 794636595 883281262 1299182841 723100827]
    WHITELIST_USERS = [964158165 1227877179 794636595 883281262 1299182841 723100827]
    CERT_PATH = None
    PORT = 8443
    DEL_CMDS = False  #Delete commands that users dont have access to, like delete /ban if a non admin uses it.
    STRICT_GBAN = False
    STRICT_GMUTE = False
    WORKERS = 8 
    BAN_STICKER = 'CAADAgADOwADPPEcAXkko5EB3YGYAg'  # banhammer marie sticker
    ALLOW_EXCL = False  # Allow ! commands as well as /
    CASH_API_KEY = None # 
    TIME_API_KEY = Noe  #
    API_OPENWEATHER = False #Get API_OPENWEATHER FROM OFFICAL SITE https://da.gd/VAW3
    AI_API_KEY =5e42c10d3f4d159de058fb5658082e04156b8e0e144527e931cafc68aba2534f8c3abed5c1f141863be41f90dc595006aa1b93661d881472358037787327b15d
    WALL_API = None # Get one from https://wall.alphacoders.com/api.php


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
