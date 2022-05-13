from socket import socket
from threading import Thread as thread

def server_init():
    s = socket(0x02, 0x01, 0x00)
    s.bind(("0.0.0.0", 443))
    s.listen()
    return s.accept()

def recv(s :socket):
    res = data = b""
    try:
        s.settimeout(1)
        while True:
            data = s.recv(4096)
            if not data:
                break
            res += data
    except:
        pass
    return res



