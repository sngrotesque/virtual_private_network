from .color import *

help_document_text = (
    "\n"
    "[关于实现]\n"
    f"\t这个脚本是用{BLUE}Python3{RESET}实现的，后续有可能会使用C语言实现。\n\n"
    "[关于配置]\n"
    "\t端口范围从1024开始是为了防止你配置时与其他服务产生冲突。\n\n"
    "[关于密码]\n"
    f"\t{GOLD}支持中文密码{RESET} (使用编码: {BLUE}UTF-8{RESET}) 注意: 一个中文字符为{BLUE}3字节{RESET}\n"
    f"\t密码字节长度请不要超过{RED}256字节{RESET}，因为超过的数算无效。\n"
    "\t密码不足256字节的话会被填充为256字节，填充方式如下:\n"
    "\t使用 0F 1F 2F 3F 4F 5F 6F 7F 8F 9F AF BF CF DF EF FF 轮流填充\n"
    "\t密码长度大于等于256字节的不做填充\n"
    
)


