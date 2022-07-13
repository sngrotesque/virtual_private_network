from snvpn import *

s = SSLContext(PROTOCOL_TLSv1_2).wrap_socket(socket(), server_hostname="sngrotesque.com")
s.connect(("sngrotesque.com", 443))
s.sendall(
    (
        "CONNECT suggestion.baidu.com:443 HTTP/1.1\r\n"
        "Host: suggestion.baidu.com:443\r\n"
        "Proxy-Connection: keep-alive\r\n"
        "User-Agent: Android\r\n\r\n"
    ).encode()
)
print(s.recv(4096))

s.close()


