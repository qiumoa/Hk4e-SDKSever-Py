import rsa

from base64 import b64decode
from settings.loadconfig import get_config

#=====================加密解密=====================#
def decrypt_sdk_authkey(version, message):
   return rsa.decrypt(b64decode(message), rsa.PublicKey.load_pkcs1(get_config()["Crypto"]["rsa"]["authkey"][version])).decode()

def decrypt_rsa_password(message):
   return rsa.decrypt(b64decode(message), rsa.PrivateKey.load_pkcs1(get_config()["Crypto"]["rsa"]["password"])).decode()