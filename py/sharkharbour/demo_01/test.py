import vpn

with open("./server.py", "rb") as f:
    p = f.read()



key = "我的VPN配置是使用Python3实现"

c = vpn.encrypt(p, key, vpn.iv)
print(c)


print(vpn.decrypt(c, key, vpn.iv))




