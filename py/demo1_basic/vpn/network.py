from socket import socket
from threading import Thread as thread

# 所有数据一律转为二进制数据（除了字典类型数据）
def dtob(data :object):
    if type(data) == str:
        return data.encode()
    elif type(data) == set or \
        type(data) == list or \
        type(data) == tuple:
        return "".join([str(x) for x in data]).encode()
    else:
        return data

# 封装的初始化服务端Socket
def server_init(host :str, port :int):
    s = socket(0x02, 0x01, 0x00)
    s.setsockopt(0xFFFF, 0x04, 1)
    s.bind((host, port))
    s.listen(5)
    return s.accept()

# 封装的初始化客户端Socket
def client_init(host :str, port :int):
    s = socket(0x02, 0x01, 0x00)
    s.connect((host, port))
    return s

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



