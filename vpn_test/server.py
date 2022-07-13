from snvpn import *

# 连接目标服务器时，如果是443端口或HTTPS服务，必要要用SSL模块构建套接字

server_host = "0.0.0.0"
server_port = 8888

target_host = ""
target_port = 0

server_s = socket(AF_INET, SOCK_STREAM, 0)
server_s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
server_s.bind((server_host, server_port))
server_s.listen(30)
server_s, client_addr = server_s.accept()

res = server_s.recv(4096)

target_host, target_port = match_host_port(res)

target_s = socket(AF_INET, SOCK_STREAM, 0)
target_s.connect((target_host, target_port))
target_s.sendall(res)

print(res)
print(target_s.recv(4096))

server_s.close()
target_s.close()




