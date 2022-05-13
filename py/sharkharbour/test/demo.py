from socket import *
from threading import Thread

def loop(s: socket):
    while True:
        try:
            res = s.recv(4096)
            if res:
                print(res)
            
            c = socket()
            c.connect(("www.baidu.com", 443))
            c.sendall(res)
            res = s.recv(c.recv(40960))
            
            s.sendall(res)
        except:
            pass

def main():
    host, port = "0.0.0.0", 1080
    s = socket(AF_INET, SOCK_STREAM, 0)
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    s.bind((host, port))
    s.listen(5)
    
    while True:
        try:
            s, addr = s.accept()
        except OSError:
            s = socket(AF_INET, SOCK_STREAM, 0)
            s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
            s.bind((host, port))
            s.listen(5)
            s, addr = s.accept()
        
        th = Thread(target = loop, args = (s, ))
        th.start()

if __name__ == "__main__":
    main()
