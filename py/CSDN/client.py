#!/usr/bin/python
from sys import argv
from socket import socket

def receive_from(s :socket):
    buffer = ""
    s.settimeout(1)
    try:
        while True:
            data = s.recv(4096)
            if not data:
                break
            buffer += data
    except:
        pass
    return buffer

def main():
    server_ip = argv[1]
    server_port = int(argv[2])
    client = socket(0x02, 0x01, 0x00)
    client.connect((server_ip, server_port))

    while True:
        data = receive_from(client)
        if data:
            print(data)

if __name__ == "__main__":
    main()

