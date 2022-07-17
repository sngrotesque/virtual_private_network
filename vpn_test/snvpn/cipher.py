from base64   import b64encode as b64en, b64decode as b64de
from binascii import a2b_hex as a2b
from random   import randint
from ctypes   import c_uint8 as uint8_t

EOF  = -1

def b2l(data: bytes):
    if type(data) != bytes:
        return EOF
    return list(data)

def l2b(data :list):
    return a2b("".join(["%02x"%x for x in data]))

def create_key():
    key = [randint(1, 255) for x in range(256)]
    return l2b(key)

def encrypt(data :bytes, key :bytes):
    data = b2l(data)
    key  = b2l(key)
    n    = len(data)
    keyindex = 0
    for x in range(n):
        data[x] = uint8_t((data[x] ^ key[uint8_t(keyindex).value]) - 0x4b).value ^ 0xFF
        keyindex += 1
    return l2b(data)

def decrypt(data :bytes, key :bytes):
    data = b2l(data)
    key  = b2l(key)
    n    = len(data)
    keyindex = 0
    for x in range(n):
        data[x] = uint8_t(((data[x] ^ 0xFF) + 0x4b) ^ key[uint8_t(keyindex).value]).value
        keyindex += 1
    return l2b(data)

