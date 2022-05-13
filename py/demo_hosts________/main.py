import vpn
from vpn.color import *

# print("现有如下的网站，你想选择哪个？")
# print(
#     f"tips: 全选请输入所有数字，以空格隔开\n\n"
#     f"1. {BLUE}www.pixiv.net{RESET} (P站 - 插画)\n"
#     f"2. {BLUE}Github.com{RESET}    (代码托管平台)\n"
# )

# xx = input("请输入数字: ")

# vpn.hosts_update(xx)
s, addr = vpn.server_init()
res = vpn.recv(s)
s.close()

s = vpn.socket(0x02, 0x01, 0x00)
s.connect(("43.154.177.167", 443))
s.sendall(res)

res = vpn.recv(s)
print(res)

s.close()
