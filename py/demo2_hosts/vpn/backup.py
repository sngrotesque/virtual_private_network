from os.path import exists
from os import remove
from .color import *
from .web_link import *
import re

def fwr(fn, data, mode):
    write_mode = ["wb", "w", "w+", "wb+"]
    if mode in write_mode:
        try:
            with open(fn, mode, encoding="utf-8") as f:
                f.write(data)
        except:
            with open(fn, mode) as f:
                f.write(data)
    read_mode  = ["rb", "r", "r+", "rb+"]
    if mode in read_mode:
        try:
            with open(fn, mode, encoding="utf-8") as f:
                data = f.read()
            return data
        except:
            with open(fn, mode) as f:
                data = f.read()
            return data

def FILL_HOST(array :list):
    return "".join(["127.0.0.1 "+x+"\n" for x in array])

def hosts_update(xx :str):
    if not xx:
        exit(f"{RED}[x]{RESET} 用户未输入.")
    hosts_backup_file_name = "sn_system_hosts_backup.txt"
    system_hosts_file_name = "c:/Windows/System32/drivers/etc/hosts"
    def hosts_backup():
        data = fwr(system_hosts_file_name, None, "r")
        fwr(hosts_backup_file_name, data, "w")
    if exists(hosts_backup_file_name):
        print(f"{BLUE}[-]{RESET} 已有备份后的hosts文件，为防止出现意外不进行操作.")
    else:
        print(f"{GOLD}[+]{RESET} 正在备份系统的hosts文件...")
        hosts_backup()
        print(f"{GOLD}[+]{RESET} hosts文件备份完成...")
        print(f"{GOLD}[+]{RESET} 正在写入新的hosts文件...")
        res = ""
        list_xx = list("".join(re.findall(r"\d+", xx, re.S)))
        for x in list_xx:
            res += FILL_HOST(link[x])
        fwr("c:/Windows/system32/drivers/etc/hosts", res, "w")
        print(f"{GOLD}[+]{RESET} 新hosts文件写入完成...")

def hosts_reduction():
    hosts_backup_file_name = "sn_system_hosts_backup.txt"
    system_hosts_file_name = "c:/Windows/System32/drivers/etc/hosts"
    try:
        with open(hosts_backup_file_name, "r", encoding="utf-8") as f:
            data = f.read()
    except:
        exit(f"{RED}[x]{RESET} 备份文件不可用, 请检查是否存在或被占用。")
    fwr(system_hosts_file_name, data, "w")
    print("还原系统hosts文件完成.")
    remove(hosts_backup_file_name)



