from random import choice


# 十六进制转储
def hexdump(src :bytes):
    length, result, digits = 32, [], 2
    for i in range(0, len(src), length):
        s = src[i : i+length]
        hexa = ''.join(["%02X "%x for x in s])
        text = "".join([chr(x if 0x20 <= x < 0x7F else 0x2E) for x in s])
        result.append("%08X  %-*s %s" % (i, length * (digits + 1), hexa, text))
    print('\n'.join(result))

def add_key(_r :set, _n :int, _range :int):
    MMMAX = len(hex(_r[1]).replace("0x",""))
    arr = [f"%0{MMMAX}X"%x for x in range(_r[0], _r[1] + 1)]
    for x in range(_n):
        print(f"0x{choice(arr)}, ", end="")
        if (x+1) % _range == 0:
            print()
    print()



