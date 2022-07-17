from socket   import socket, AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR
from re       import findall as re_findall, I as re_I, S as re_S
from base64   import b64encode as b64en, b64decode as b64de
from ssl      import SSLContext, PROTOCOL_TLSv1_2, SSLError, SSLWantReadError
from hashlib  import sha256 as SHA256
from binascii import a2b_hex as a2b
from OpenSSL  import SSL

from .config  import configw, configr
from .cipher  import create_key, encrypt, decrypt

def sha256(data :bytes):
    hexTables = SHA256()
    hexTables.update(data)
    return hexTables.hexdigest()

def match_host_port(data :bytes):
    host, port = re_findall(
        b"host: ([a-zA-Z0-9-.]+)"
        b"(?:\:(\d+))?", data, re_I)[0]
    if not port:
        return host.decode(), 0
    return host.decode(), int(port)

def handler_socket(handler_host :str, handler_port :int, handler_listen :int):
    sock = socket(AF_INET, SOCK_STREAM, 0)
    sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    sock.bind((handler_host, handler_port))
    sock.listen(handler_listen)
    return sock.accept()

def client_socket(target_host :str, target_port :int):
    basic_socket = socket(AF_INET, SOCK_STREAM, 0)
    ssl_socket = SSLContext(PROTOCOL_TLSv1_2).wrap_socket(
    socket(AF_INET, SOCK_STREAM, 0), server_hostname = target_host)
    try:
        ssl_socket.connect((target_host, target_port))
    except SSLError:
        ssl_socket.close()
        basic_socket.connect((target_host, target_port))
        return basic_socket
    return ssl_socket

def socket_recv(socket_fd :socket):
    data = res = socket_fd.recv(1024)
    socket_fd.setblocking(0)
    while True:
        try:
            data = socket_fd.recv(4096)
            if not data: break
            res += data
        except BlockingIOError:
            break
        except SSLWantReadError:
            print("SSL/TLS套接字报错: SSLWantReadError.")
            break
    socket_fd.setblocking(1)
    return res




