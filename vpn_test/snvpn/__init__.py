from socket   import socket, AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR
from re       import findall as re_findall, I as re_I, S as re_S
from base64   import b64encode as b64en, b64decode as b64de
from ssl      import SSLContext, PROTOCOL_TLSv1_2
from hashlib  import sha256 as SHA256
from binascii import a2b_hex as a2b
from .config  import config_write

def sha256(data :bytes):
    hexTables = SHA256()
    hexTables.update(data)
    return hexTables.hexdigest()

def match_host_port(data):
    try:
        host, port = re_findall(b"host: ([a-zA-Z0-9-.]+):(\d+)", data, re_I)[0]
    except IndexError:
        print(f"匹配域名和端口发生错误，以下是原数据\n{data}")
        exit(-1)
    return host.decode(), int(port)



