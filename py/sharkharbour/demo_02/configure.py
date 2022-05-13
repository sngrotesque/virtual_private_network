from json import loads
from os.path import exists
from os import (
    removedirs as rm_dir, system as syscmd,
    geteuid, mkdir, remove, popen
)
import re

RED,  BLUE,    GREEN = "\x1b[91m", "\x1b[96m", "\x1b[92m"
GOLD, MAGENTA, WHITE = "\x1b[93m", "\x1b[95m", "\x1b[97m"
RED_Dark,  BLUE_Dark,    GREEN_Dark = "\x1b[31m", "\x1b[36m", "\x1b[32m"
GOLD_Dark, MAGENTA_Dark, WHITE_Dark = "\x1b[33m", "\x1b[35m", "\x1b[37m"
BLACK, GREY,   RESET = "\x1b[30m", "\x1b[90m", "\x1b[0m"

preface = (
    f"sharkharbour {RED}[v0.0.1]{RESET}\n"
    "---- SN-Grotesque ----\n\n"
    f"{GREEN}1{RESET}. 开始配置sharkharbour\n"
    f"{GREEN}2{RESET}. 卸载清除sharkharbour\n"
    "——————————————\n"
    f"{GREEN}3{RESET}. 查看配置信息\n"
    f"{GREEN}4{RESET}. 显示连接信息\n"
    f"{GREEN}5{RESET}. 修改用户配置\n"
    f"{GREEN}6{RESET}. 手动修改配置\n"
    "——————————————\n"
    f"{GREEN}7{RESET}. 启动sharkharbour\n"
    f"{GREEN}8{RESET}. 停止sharkharbour\n"
    "——————————————\n"
    f"{GREEN}10{RESET}. 帮助文档\n"
)

help_document = (
    "[关于实现]\n"
    f"\t这个脚本是用{BLUE}Python3{RESET}实现的，后续有可能会使用C语言实现。\n\n"
    "[关于密码]\n"
    f"\t密码{RED}不足{RESET}{BLUE}256{RESET}字节的会填充为256字节\n"
    "\t填充方式: 7F 60 51 ... AC 9D 8E\n\n"
    "[关于协议]\n"
    "\t此脚本只会使用TCP/IP协议，如需UDP协议请自行添加。\n"
    "\n"
)

def root_check():
    if geteuid() != 0:
        exit(f"[!] {RED}错误{RESET}，当前用户非root用户")

def print_doc(data, length = 32, text = ""):
    data_length = len(data)
    print(f"\n--{text}---------------------------------------------------------------------------------------------")
    for x in range(data_length):
        if x == 0:
            print("| ", end="")
        print("%02X "%data[x], end="")
        if (x+1) % length == 0 and x != data_length - 1:
            print("|\n| ", end="")
        if x == data_length - 1:
            print("|")
    print("---------------------------------------------------------------------------------------------------\n")

class config:
    def __init__(self, data = None):
        self.config_file_name = "user_config.json"
        self.config_directory = "/usr/local/sharkharbour/"
        self.config_path = "/usr/local/sharkharbour/user_config.json"
        self.data = data
    
    @property
    def update(self):
        print(f"{GOLD}[!]{RESET} 开始配置[{WHITE}sharkharbour{RESET}]...\n")
        local_host = "0.0.0.0"
        print(
            f"{GOLD}[!]{RESET} 正在配置端口...\n"
            f"{GOLD}[!]{RESET} 请尽量不要使用以下端口，因为可能会与系统服务产生冲突\n"
            f"    {BLUE}[21]{RESET}: FTP服务,  {BLUE}[22]{RESET}:  SSH服务, {BLUE}[25]{RESET}:  SMTP\n"
            f"    {BLUE}[80]{RESET}: HTTP服务, {BLUE}[443]{RESET}: SSL服务, {BLUE}[3306]{RESET}: Mysql\n"
        )
        while True:
            try:
                local_port = input("请输入(默认8964): ")
                local_port = 8964 if not local_port else local_port
                local_port = int(local_port)
                if local_port < 1 or local_port > 65535:
                    print(f"[X] {RED}错误{RESET}，范围须为[1~65535]，请重新输入")
                else:
                    print(f"\n--------------\n| 端口: {local_port}\n--------------\n")
                    break
            except ValueError:
                print(f"[X] {RED}错误{RESET}，请输入数字")
        print(
            f"{GOLD}[!]{RESET} 正在配置密码...\n"
            f"{GOLD}[!]{RESET} 密码字节长度必须大于等于1且小于等于256 (超出无效)\n"
            f"{GOLD}[!]{RESET} 支持中文, 编码(UTF-8)，中文字符为3字节"
        )
        password = input("请输入(默认: sngrotesque): ")
        if not password:
            password = "sngrotesque"
        print_doc(password.encode(), text = "密码")
        
        print(
            f"{GOLD}[!]{RESET} 正在配置加密方式...\n"
            f"    {BLUE}1{RESET}. shr_2048\n"
            f""
        )
        while True:
            try:
                user_xx = input('请输入数字(默认: 1): ')
                if not user_xx:
                    user_xx = 1
                else:
                    user_xx = int(user_xx)
                
                if user_xx == 1:
                    method = "shr_2048"
                print(f"\n--------------\n| 加密方式: {method}\n--------------\n")
                break
            except ValueError:
                print(f"[X] {RED}错误{RESET}，请输入数字")
        
        while True:
            try:
                print(f"{GOLD}[!]{RESET} 正在配置最大连接数")
                listen = input("请输入(默认5): ")
                if not listen:
                    listen = 5
                else:
                    listen = int(listen)
                print(f"\n-------------------\n| 最大连接数: {listen}\n-------------------\n")
                break
            except ValueError:
                print(f"[X] {RED}错误{RESET}，请输入数字")
        data = (
            '{\n'
            f'    "local_host": "{local_host}",\n'
            f'    "local_port": {local_port},\n\n'
            f'    "password":   "{password}",\n'
            f'    "method":     "{method}",\n\n'
            f'    "listen_n":   {listen}\n'
            '}'
        )
        return data
    
    @property
    def write(self):
        if not exists(self.config_path):
            mkdir(self.config_directory)
            with open(self.config_path, "w", encoding="utf-8") as f:
                f.write(self.data)
        else:
            exit(f"[X] {RED}错误{RESET}, 配置文件已存在")
    
    @property
    def read(self):
        if self.check:
            with open(self.config_path, "r", encoding="utf-8") as f:
                data = f.read()
            return loads(data)
        else:
            exit(f"[X] {RED}错误{RESET}, 配置文件不存在")
    
    @property
    def check(self):
        if exists(self.config_path):
            return True
        else:
            return False

    @property
    def remove(self):
        if exists(self.config_path):
            print(f"确定要清除{WHITE}[sharkharbour]{RESET}吗?")
            temp = input("请输入[y / N]: ")
            if not temp or temp.upper() == 'N':
                print(f"[!] 已取消卸载{WHITE}[sharkharbour]{RESET}.")
                return 0
            elif temp.upper() == 'Y':
                remove(self.config_path)
                rm_dir(self.config_directory)
                print(f"[!] 已清除{WHITE}sharkharbour{RESET}")
            else:
                print(f"[X] {RED}错误输入{RESET}")
        else:
            print(f"[X] {RED}错误{RESET}, 配置文件不存在")

def main_func():
    root_check()
    
    print(preface)
    user_xx = input("请输入: ")
    
    if user_xx == "1":
        if not config().check:
            command = [
                "apt update",
                "apt install vim",
                "python3 -m pip install --upgrade pip",
                "python3 -m pip install pycryptodome"
            ]
            for x in command:
                syscmd(x)
            
            config_data = config().update
            config(data=config_data).write
            print(f"[!] {GOLD}配置完成{RESET}")
        else:
            exit(f"[X] {RED}配置文件已存在{RESET}")
    elif user_xx == "2":
        config().remove
    elif user_xx == "3":
        data = config().read
        syscmd("clear")
        print(
            f"-----------{WHITE}[sharkharbour]{RESET} 配置信息------------\n"
            f"| 本地监听IP:    {BLUE}{data['local_host']}{RESET}\n"
            f"| 本地监听端口:  {BLUE}{data['local_port']}{RESET}\n"
            f"| \n"
            f"| 密码:          {BLUE}{data['password']}{RESET}\n"
            f"| 加密方式:      {BLUE}{data['method']}{RESET}\n"
            f"| \n"
            f"| 最大连接数:    {BLUE}{data['listen_n']}{RESET}\n"
            f"----------------------------------------------"
        )
    elif user_xx == "4":
        data = config().read
        connection = popen(f"netstat -ant | grep \":{data['local_port']}\"").read()
        connection = re.findall(r"\d+\.\d+\.\d+\.\d+\:\d+[\s\t]+(\d+\.\d+\.\d+\.\d+)", connection, re.S)
        print("--连-接-信-息------------------------")
        for x in connection:
            print(f"  IPv4: {BLUE}{x}{RESET}")
    elif user_xx == "5":
        pass
    elif user_xx == "6":
        if config().check:
            syscmd(f"vim /usr/local/sharkharbour/user_config.json")
        else:
            exit(f"[X] {RED}错误{RESET}, 配置文件不存在")
    elif user_xx == "7":
        pass
    elif user_xx == "8":
        pass
    elif user_xx == "10":
        print(help_document)
    else:
        print(f"[X] {RED}错误{RESET}, 请输入正确的数字")

if __name__ == "__main__":
    main_func()
