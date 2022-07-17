from snvpn import *
from os import urandom

data = (
    "Python，C，C++，Java，lua，Perl，Ruby，VB，C#，ASM，DOS，JS，TS，Objective-C，B，BCPL。\n"
    "以上编程语言都受到ALGOL 60语言的影响。\n"
    "其中，除了B，BCPL与C语言本身以外的所有语言，全部都由C语言编写而来。\n"
    "C语言在编程史上有着功不可没的传奇地位。"
).encode()

key = a2b(
    "bb9e50923f6022525793af91bbe41d4fe3188eab85c8d92cf6a7b51d22811ea9"
    "21fe4b2bf5b33e53a92d75fdc379287bf1c4b77080688c10b6e67108148785a2"
    "8f8448bbf65d6a1299eb75cdf020b7ce0fd38fdd309b74bb09614de6820f639a"
    "95606e1a58a511d3c714f3a6f35d7a6c851a182f7059339f68c1dffbfc7c3d61"
    "5a73de264df420d4ee0a65c909dbd2fe77f1291c12e837fe9dd36962ea9d55dd"
    "ebd1b484e41843c5ccc983e1776f1a1f48d995a17455c803a21cbe773837dc5a"
    "e9ca18c391bc87f04c7be84b35001da14369eb14a2833934dafc3c484d495720"
    "630a4753e64c4e4c1dcbb4a1fa87712784ee147dbced16f38686b12e01ff0317"
)

print(f"数据字节长度: {len(data)}\n密钥字节长度: {len(key)}\n")

res = encrypt(data, key)
print(res)


