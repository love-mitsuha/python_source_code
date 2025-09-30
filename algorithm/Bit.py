# 对相同长度的列表每一位进行异或运算
def xor(a,b):
    return [i^j for i, j in zip(a, b)]

# 模二除法
# data是数据位
# crc_divisor是多项式
def mod2_div(data,crc_divisor):
    length=len(crc_divisor)
    dividend = data[:length]
    for i in range(length, len(data)):
        # 被除数首位是1则要进行除法
        if dividend[0] == 1:
            dividend = xor(dividend,crc_divisor)
        dividend.pop(0)
        dividend.append(data[i])
    # 最后一次进行除法
    if dividend[0] == 1:
        dividend = xor(dividend,crc_divisor)
    # 余数要舍弃第一位
    remainder = dividend[1:]
    # 余数是否为零 可用于判断是否有误
    return all(b == 0 for b in remainder)
