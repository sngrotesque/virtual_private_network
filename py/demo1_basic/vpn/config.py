from os.path import exists
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

    local_port = input("请输入端口[1024-65535]: ")
    password = input("请输入密码[1-256字节]: ")
    listen = input("最大连接数[]: ")

    configure['local_host'] = "0.0.0.0"
    configure['local_port'] = int(local_port)
    configure['password']   = password
    configure['listen']     = listen

    return JSON_formatting(configure)

def config_write(config_data :str):
    if config_data != 0:
        with open(fn, "w") as f:
            f.write(config_data)

def config_read():
    with open(fn, "r") as f:
        config_data = f.read()
    return loads(config_data)

