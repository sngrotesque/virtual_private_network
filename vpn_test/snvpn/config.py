from json import loads as jloads, dumps as jdumps

JSON_FILE_NAME = "snvpn_sharkharbour.json"

def config_format(data :dict):
    bytes_data = "{\n"
    data_len = len(data)
    num = 0
    for x in data:
        if type(data[x]) == str:
            bytes_data += f'\t"{x}": "{data[x]}"'
        else:
            bytes_data += f'\t"{x}": {data[x]}'
        if num != data_len - 1:
            bytes_data += ","
        bytes_data += "\n"
        num += 1
    bytes_data += "}"
    return bytes_data.encode()

def configw(data :dict):
    data = config_format(data)
    with open(JSON_FILE_NAME, "wb") as f:
        f.write(data)

def configr():
    with open(JSON_FILE_NAME, "rb") as f:
        data = f.read()
    return jloads(data)


