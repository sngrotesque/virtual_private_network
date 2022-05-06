import vpn

s = vpn.client_init("fanick.top", 80)
s.sendall(b"GET / HTTP/1.1\r\nHost: fanick.top\r\nUser-Agent: Android\r\n\r\n")
res = vpn.recv(s)
s.close()

c = vpn.encrypt(res, vpn.key, vpn.iv)

print(vpn.b64de(c))


