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

def hexdump(src :bytes):
    length, result, digits = 32, [], 2
    for i in range(0, len(src), length):
        s = src[i : i+length]
        hexa = ''.join(["%02X "%x for x in s])
        text = "".join([chr(x if 0x20 <= x < 0x7F else 0x2E) for x in s])
        result.append("%08X  %-*s %s" % (i, length * (digits + 1), hexa, text))
    print('\n'.join(result))




