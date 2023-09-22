# 文件目录
DB_PATH = "./data/sdk.db"
MI18N_PATH = './data/mi18n'
CONFIG_FILE_PATH = "./config.yaml"
GEOIP2_DB_PATH = "./data/GeoLite2-Country.mmdb"
AUTHVERIFY_KEY_PATH = "./data/key/authverify.pem"
PASSWDWORD_KEY_PATH = "./data/key/password.pem"

GACHA_TEXTMAP_PATH = './data/gacha/textmap'
GACHA_SCHEDULE_PATH = './data/gacha/schedule'

SHOPWINDOW_TIERS_PATH = "./data/shopwindow/tiers.json"
SHOPWINDOW_PAY_TYPES_PATH = "./data/shopwindow/pay_types.json"

ANNOUNCE_PATH = "./data/announce/list.json"
ANNOUNCE_CONTENT_PATH = "./data/announce/content.json"
ANNOUNCE_JS_PATH = "./static/js/announce/2_2e4d2779ad3d19e6406f.js"
ANNOUNCE_CSS_PATH = "./static/css/announce/2_cb04d2d72d7555e2ab83.css"
ANNOUNCE_FAVICON_PATH = "./static/favicon.ico"
ANNOUNCE_MAINJS_PATH = "./static/js/announce/main.js"
ANNOUNCE_VUEMIN_PATH = "./static/js/announce/vue.min.js"
ANNOUNCE_MAINH5JS_PATH = "./static/js/announce/main-h5log.js"
ANNOUNCE_FPTJS_PATH = "./static/js/announce/firebase-performance-standalone.js"

# 账号类型
ACCOUNT_TYPE_GUEST = 0
ACCOUNT_TYPE_NORMAL = 1

# 官服 B服
CHANNEL_ID_MIHOYO = 1
CHANNEL_ID_BILIBILI = 14

# 登录场景
SCENE_NORMAL = "S_NORMAL"        # 手机号+用户名 默认手机号
SCENE_ACCOUNT = "S_ACCOUNT"      # 手机号+用户名 默认用户名
SCENE_USER = "S_USER"            # 仅账号
SCENE_TEMPLE = "S_TEMPLE"        # 仅账号 无需注册

# 客户端平台
PLATFORM_TYPE = {
   0: "EDITOR",
   1: "IOS",
   2: "ANDROID",
   3: "PC",
   4: "PS4",
   5: "SERVER",
   6: "CLOUD_ANDROID",
   7: "CLOUD_IOS",
   8: "PS5",
   9: "CLOUD_WEB",
   10: "CLOUD_TV",
   11: "CLOUD_MAC",
   12: "CLOUD_PC",
   13: "CLOUD_THIRD_PARTY_MOBILE",
   14: "CLOUD_THIRD_PARTY_PC"
}

# 返回的状态码
RES_SUCCESS = 0
RES_FAIL = -1
RES_CANCEL = -2
RES_NO_SUCH_METHOD = -10
RES_LOGIN_BASE = -100
RES_LOGIN_FAILED = -101
RES_LOGIN_CANCEL = -102
RES_LOGIN_ERROR = -103
RES_LOGOUT_FAILED = -104
RES_LOGOUT_CANCEL = -105
RES_LOGOUT_ERROR = 106
RES_PAY_FAILED = -107
RES_PAY_CANCEL = -108
RES_PAY_ERROR = -109
RES_PAY_LAUNCH = -120
RES_PAY_UNKNOWN = -116
RES_EXIT_FAILED = -110
RES_EXIT_NO_DIALOG = -111
RES_EXIT_CANCEL = -112
RES_EXIT_ERROR = -113
RES_INIT_FAILED = -114
RES_INIT_ERROR = -115
RES_LOGIN_FORBIDDED = -117
RES_NEED_REALNAME = -118
RES_NEED_GUARDIAN = -119
RES_EOS_DLL_ERROR = -1001
RES_EOS_TOKEN_ERROR = -1002
RES_GOOGLE_PC_TOKEN_ERROR = -1003

RES_SDK_VERIFY_SUCC = 0
RES_SDK_VERIFY_FAIL = 1

# risky
RISKY_ACTION_NONE = "ACTION_NONE"
