from .color import *

preface = (
    f"SN_VPN 一键配置脚本 {RED}[v0.0.1]{RESET}\n"
    "------- SN-Grotesque -------\n\n"
    f"{GREEN}1{RESET}. 开始配置SN_VPN\n"
    f"{GREEN}2{RESET}. 卸载清除SN_VPN\n"
    "——————————————\n"
    f"{GREEN}3{RESET}. 查看配置信息\n"
    f"{GREEN}4{RESET}. 显示连接信息\n"
    f"{GREEN}5{RESET}. 修改用户配置\n"
    f"{GREEN}6{RESET}. 手动修改配置\n"
    "——————————————\n"
    f"{GREEN}7{RESET}. 启动SN_VPN\n"
    f"{GREEN}8{RESET}. 停止SN_VPN\n"
    "——————————————\n"
    f"{GREEN}10{RESET}. 帮助文档\n"
    # f"{GREEN}12{RESET}. {RED}反馈BUG{RESET}\n\n"
)

help_document_text = (
    "[关于实现]\n"
    f"\t这个脚本是用{BLUE}Python3{RESET}实现的，后续有可能会使用C语言实现。\n\n"
    "[关于配置]\n"
    "\t端口范围从1024开始是为了防止你配置时与其他服务产生冲突。\n\n"
    "[关于密码]\n"
    f"\t{GOLD}支持中文密码{RESET} (使用编码: {BLUE}UTF-8{RESET}) 注: 中文字符为{BLUE}3字节{RESET}\n"
    f"\t密码字节长度请不要超过{RED}256字节{RESET}(超过部分无效)\n"
    "\t密码不足256字节(大于等于不填充)的会填充为256字节\n"
    "\t填充方式: 0F 1F 2F ... EF FF\n\n"
)
