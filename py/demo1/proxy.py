from socket import SOL_SOCKET, SO_REUSEADDR, socket
from re import findall, I as re_I, S as re_S
from binascii import a2b_hex as a2b

def dtob(data):
    if type(data) == str:
        return data.encode()
    elif type(data) == set or \
        type(data) == list or \
        type(data) == tuple:
        return "".join([str(x) for x in data]).encode()
    else:
        return data

def server_init(host, port):
    s = socket(0x02, 0x01, 0x00)
    s.setsockopt(0xFFFF, 0x04, 1)
    s.bind((host, port))
    s.listen(5)
    return s.accept()






