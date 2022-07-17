from snvpn import *

print("-------------------------------")

s = client_socket("127.0.0.1", 1080)
s.sendall("".join(["0" for x in range(409600)]).encode())
# s.recv(4096)
s.close()