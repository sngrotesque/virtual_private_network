import vpn

preface = (
    "SN_VPN 一键配置脚本 [v0.0.1]\n"
    "------- SN-Grotesque -------\n\n"
    "1. 开始配置SN_VPN\n"
    "2. 卸载清除SN_VPN\n"
    "——————————————\n"
    "3. 查看配置信息\n"
    "4. 显示连接信息\n"
    "5. 修改用户配置\n"
    "6. 手动修改配置\n"
    "——————————————\n"
    "7. 启动SN_VPN\n"
    "8. 停止SN_VPN\n"
    "——————————————\n"
    "10. 帮助文档\n\n"
)

print(preface)
xx = int(input("请输入[1-8]: "))

if xx == 1:
    data = vpn.config_update()
    vpn.config_write(data)

if xx == 10:
    print(vpn.help_document_text)


