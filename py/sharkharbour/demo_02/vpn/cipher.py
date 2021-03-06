from binascii import a2b_hex as htob
def btoh(data :bytes):
    return data.hex()

def FILL_2048_BITS(data :bytes, length = 256):
    data_length = len(data)
    data_temp = list(data[:length])
    padding_data = [
        0x7F, 0x60, 0x51, 0x42, 0x33, 0x24, 0x15, 0x06,
        0xF7, 0xE8, 0xD9, 0xCA, 0xBB, 0xAC, 0x9D, 0x8E
    ]
    padding_index = 0
    for x in range(length - data_length):
        if padding_index == 16:
            padding_index = 0
        data_temp.append(padding_data[padding_index])
        padding_index += 1
    return data_temp

from base64 import b64encode as b64en, b64decode as b64de
class shr_2048:
    def __init__(self, data :bytes, key :bytes):
        self.data = data
        self.key  = key
        self.iv   = [
            0x2D, 0x34, 0x27, 0xDB, 0x74, 0x6F, 0xA8, 0x81, 0x55, 0x3C, 0x5F, 0x02, 0x53, 0xFC, 0x8B, 0x1B, 
            0x98, 0x41, 0x48, 0x44, 0xE8, 0xD9, 0xF5, 0xAC, 0x2A, 0x78, 0xB9, 0xEF, 0x6F, 0x64, 0x9E, 0x57, 
            0x43, 0x04, 0x73, 0x1B, 0x79, 0x41, 0x10, 0xC0, 0x31, 0xC4, 0x1C, 0xCC, 0x69, 0x91, 0x23, 0x7A, 
            0x51, 0x66, 0xF8, 0x6B, 0xC9, 0x50, 0x41, 0x9D, 0xD4, 0xD6, 0xCC, 0xCE, 0x04, 0x6D, 0xE9, 0xCD, 
            0x0B, 0xA8, 0x9C, 0x36, 0x42, 0x9A, 0x11, 0x09, 0xAE, 0xFE, 0x27, 0x1A, 0x9B, 0x5C, 0xBD, 0x63, 
            0x96, 0x81, 0xB9, 0xB4, 0xC9, 0x86, 0xC0, 0xA3, 0x32, 0xFE, 0xD8, 0xAB, 0x64, 0x5D, 0x50, 0x7C, 
            0x51, 0x8B, 0xCB, 0xEF, 0x63, 0xC8, 0xFD, 0x90, 0x84, 0x46, 0x70, 0xF1, 0x3D, 0xBE, 0x81, 0x19, 
            0x08, 0x88, 0xC5, 0x2F, 0x96, 0x8C, 0x2D, 0xEA, 0x48, 0xD4, 0x7A, 0x56, 0xC2, 0x22, 0xC5, 0x89, 
            0x16, 0xE8, 0xFC, 0xFB, 0xB0, 0x58, 0x3A, 0x59, 0x9F, 0xB9, 0xB1, 0xCD, 0x58, 0xA4, 0xFA, 0x52, 
            0x95, 0x97, 0x55, 0x66, 0x2A, 0x0F, 0x0C, 0x20, 0x46, 0xB3, 0x6F, 0x34, 0xB3, 0xC9, 0x49, 0x06, 
            0xD6, 0x45, 0x3E, 0x68, 0x34, 0x87, 0xB2, 0x0D, 0xBC, 0x11, 0x46, 0xF0, 0x67, 0x40, 0x01, 0xC5, 
            0x9B, 0x3A, 0x59, 0xCF, 0x7E, 0x7D, 0x91, 0x67, 0xE7, 0x9C, 0x16, 0x54, 0xB8, 0x78, 0xD0, 0xF6, 
            0xC8, 0x65, 0x43, 0x76, 0xB4, 0x83, 0xAB, 0xB5, 0x2D, 0x33, 0x46, 0x29, 0x34, 0x66, 0x52, 0x3D, 
            0x4C, 0x14, 0xB7, 0x7F, 0x2B, 0x13, 0x49, 0xD7, 0xD1, 0xAB, 0x19, 0x57, 0x22, 0x52, 0x34, 0x59, 
            0x74, 0x61, 0xCD, 0x23, 0x4C, 0x98, 0x96, 0x9E, 0xEB, 0x9D, 0x56, 0xEE, 0xE0, 0xB8, 0x13, 0x3C, 
            0x8E, 0x06, 0xFF, 0xC8, 0x0A, 0xE0, 0xE9, 0x21, 0xF7, 0xFD, 0x78, 0x57, 0x04, 0xEE, 0xCD, 0xB3
        ]
    
    @property
    def encrypt(self):
        self.key = FILL_2048_BITS(self.key)
        data_length = len(self.data)
        index = 0
        data = ""
        for x in range(data_length):
            if index == 256:
                index = 0
            data += "%02X"%(self.data[x] ^ self.key[index] ^ self.iv[index])
            index += 1
        return b64en(htob(data))

    @property
    def decrypt(self):
        self.key = FILL_2048_BITS(self.key)
        self.data = b64de(self.data)
        data_length = len(self.data)
        index = 0
        data = ""
        for x in range(data_length):
            if index == 256:
                index = 0
            data += "%02X"%(self.data[x] ^ self.iv[index] ^ self.key[index])
            index += 1
        return htob(data)

# ????????????AES256????????????
# from Crypto.Cipher import AES
# class AES256_CFB:
#     def __init__(self, data, key):
#         self.data = data
#         self.key  = key
#         self.iv   = b"a^$@~i1387vxc793"
#     @property
#     def encrypt(self):
#         aes = AES.new(self.key, AES.MODE_CFB, self.iv)
#         return aes.encrypt(self.data)
#     @property
#     def decrypt(self):
#         aes = AES.new(self.key, AES.MODE_CFB, self.iv)
#         return aes.decrypt(self.data)



