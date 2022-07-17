from snvpn import *

proxy_socket, client_addr = handler_socket("0.0.0.0", 1080, 30)
res = socket_recv(proxy_socket)
proxy_socket.close()

print(len(res))

