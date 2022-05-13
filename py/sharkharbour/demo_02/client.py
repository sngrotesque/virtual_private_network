from vpn.cipher import shr_2048
from json import loads
from socket import socket
from threading import Thread

RED,   BLUE,    GREEN = "\x1b[91m", "\x1b[96m", "\x1b[92m"
GOLD,  MAGENTA, WHITE = "\x1b[93m", "\x1b[95m", "\x1b[97m"
RED_Dark,  BLUE_Dark,    GREEN_Dark = "\x1b[31m", "\x1b[36m", "\x1b[32m"
GOLD_Dark, MAGENTA_Dark, WHITE_Dark = "\x1b[33m", "\x1b[35m", "\x1b[37m"
BLACK, GREY,    RESET = "\x1b[30m", "\x1b[90m", "\x1b[0m"

class s:
    def __init__(self, host = None, port = None, listen = None, key = None):
        self.host = host
        self.port = port
        self.listen = listen
        self.res  = None
        self.sock = None
        self.addr = None
        
        self.key  = key
    
    @property
    def client_init(self):
        self.sock = socket(0x02, 0x01, 0x00)
        self.sock.connect((self.host, self.port))
    
    def send(self, sendData :bytes):
        self.sock.sendall(sendData)
        # shr_2048(data = sendData, key = self.key).encrypt
    
    @property
    def recv(self):
        self.res = self.sock.recv(40960)
        # self.res = data = b""
        # try:
        #     self.sock.settimeout(1)
        #     while True:
        #         data = self.sock.recv(4096)
        #         if not data:
        #             break
        #         self.res += data
        # except:
        #     pass
        # # self.res = shr_2048(data = self.res, key = self.key).decrypt

    @property
    def close(self):
        self.sock.close()

def configure_read():
    path = "/usr/local/sharkharbour/user_config.json"
    with open(path, "r", encoding="utf-8") as f:
        config_data = loads(f.read())
    return config_data

def client_handler(data :s, config_data :dict):
    while True:
        data.send(b"hello!")
        data.recv
        print(data.res)
    data.close()


if __name__ == "__main__":
    config = configure_read()
    data = s(host = "192.168.1.10", port = 8080, key = config['password'].encode())
    data.client_init
    
    th = [Thread(target = client_handler, args = (data, config)) for x in range(5)]
    for x in th:
        x.start()
    for x in th:
        x.join()
