# -*- coding: utf-8 -*-
import re

phonePattern  = re.compile(r'(1)(3\d|4[5,7]|5[0-3,5-9]|8[0,2,3,6-9])\D*(\d{4})\D*(\d{4})$')
def isMobile(mobile):
    """
    现有的国内手机号网段：

    130,131,132,133,134,135,136,137,138,139,
    145，147
    150,151,152,153,155,156,157,158,159,
    180,182,183,186,187,188,189,
    以下是匹配的正则

    表达式(Python环境运行)：

    phonePattern  = re.compile(r'(1)(3\d|4[5,7]|5[0-3,5-9]|8[0,2,3,6-9])\D*(\d{4})\D*(\d{4})$')

    可以匹配的格式有（手机号码为虚拟）：

    13856563232

    +86-13856563232

    138-5678-3232

    138 5678-3232

    138 1528 1332

    138 1528x 1332
    """
    try:
        return (True if phonePattern.findall(mobile.strip()) else False)
    except:
        return False

if __name__ == '__main__':
    print isMobile('13856563232')
