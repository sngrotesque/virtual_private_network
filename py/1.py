def hexdump(src :bytes):
    length, result, digits = 32, [], 2
    for i in range(0, len(src), length):
        s = src[i : i+length]
        hexa = ''.join(["%02X "%x for x in s])
        text = "".join([chr(x if 0x20 <= x < 0x7F else 0x2E) for x in s])
        result.append("%08X  %-*s %s" % (i, length * (digits + 1), hexa, text))
    print('\n'.join(result))


with open("./CSDN/proxy.py", "rb") as f:
    data = f.read()

hexdump(data)


