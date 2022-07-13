from snvpn import *

proxy_host = "0.0.0.0"
proxy_port = 1080

server_host = "127.0.0.1"
server_port = 8888

proxy_s = socket(AF_INET, SOCK_STREAM, 0)
proxy_s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
proxy_s.bind((proxy_host, proxy_port))
proxy_s.listen(30)
proxy_s, client_addr = proxy_s.accept()

server_s = socket(AF_INET, SOCK_STREAM, 0)
server_s.connect_ex((server_host, server_port))

server_s.sendall(proxy_s.recv(4096))

server_s.close()
proxy_s.close()
