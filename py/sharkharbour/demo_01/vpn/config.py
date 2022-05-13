from os.path import exists
from os import remove
from json import dumps, loads

fn = "user_config.json"

def config_update():
    def JSON_formatting(config_data :dict):
        temp = dumps(config_data)
        temp = temp.replace("{", "{\n\t")
        temp = temp.replace(", \"", ",\n\t\"")
        temp = temp.replace("}", "\n}")
        return temp
    if exists(fn):
        print("配置文件已存在.")
        return 0

    configure = {}

    while True:
        try:
            local_port = int(input("请输入端口[1024-65535]: "))
            if local_port >= 1024 and local_port <= 65535:
                break
            print("端口范围输入错误，请重新输入！")
        except:
            print("端口范围输入错误，请重新输入！")
    password = input("请输入密码[1-256字节]: ").encode('UTF-8')
    while True:
        try:
            listen = int(input("最大连接数[数字]: "))
            break
        except:
            print("请确认你输入正确！请重新输入。")

    configure['local_host'] = "0.0.0.0"
    configure['local_port'] = local_port
    configure['password']   = password
    configure['listen']     = listen

    return JSON_formatting(configure).encode()

def config_write(config_data :str):
    if config_data != 0:
        with open(fn, "w", encoding = "utf-8") as f:
            f.write(config_data)

def config_read():
    with open(fn, "r", encoding = "utf-8") as f:
        config_data = f.read()
    return loads(config_data)

def config_check():
    try:
        config_data = config_read()
        return config_data
    except FileNotFoundError:
        exit("[x] 未配置VPN，请检查。")

def config_detele():
    try:
        remove(fn)
        print("删除完成.")
    except FileNotFoundError:
        exit("[x] 未配置VPN，请检查。")

