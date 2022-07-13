from json import loads as jloads, dumps as jdumps

def config_write(data :dict):
    with open("snvpn.json", "w", encoding = 'utf-8') as f:
        f.write("{\n")
        for x in data:
            f.write(f"\t\"{x}\": \"{data[x]}\",\n")
        f.write("}")


