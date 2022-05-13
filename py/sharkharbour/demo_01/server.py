import vpn

print(vpn.preface)
xx = int(input("请输入[1-8]: ")); print("")

if xx == 1:
    data = vpn.config_update()
    vpn.config_write(data)
elif xx == 2:
    vpn.config_detele()
elif xx == 3:
    config_data = vpn.config_check()
    right_fence = "|"
    print(
        "|--------------------------------------------------------------------------------\n"
        f"| 监听IP:  \t{config_data['local_host']}\t\t\t{right_fence}\n"
        f"| 监听端口:\t{config_data['local_port']}\n"
        f"| 密码:    \t{config_data['password']}\n"
        f"| 最大连接:\t{config_data['listen']}\n"
    )
elif xx == 4:
    pass
elif xx == 5:
    pass
elif xx == 6:
    pass
elif xx == 7:
    pass
elif xx == 8:
    pass
elif xx == 10:
    print(vpn.help_document_text)
elif xx == 11:
    print(vpn.official_website)
else:
    print("错误选项.")




