import math
def read_int():
    def get_numbers():
        try:#防止奇怪的东西出现
            read_int.s = input().split()
            read_int.s_len = len(read_int.s)
            if read_int.s_len==0:get_numbers()#空行就继续
            read_int.cnt=0
            return 1#可以正常读
        except:#如果读到文件尾就不读了
            return 0
    if not hasattr(read_int, 'cnt'):
        if not get_numbers():return 0
    if read_int.cnt==read_int.s_len:
        if not get_numbers():return 0
    read_int.cnt+=1#下一个
    return eval(read_int.s[read_int.cnt - 1])#用eval,整数与小数通用，改成int或许会更快一点
def isPrime(num):
    # 处理边界情况
    if not isinstance(num, int) or num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    # 计算检查上限（包含边界）
    sqrt_num = math.isqrt(num)  # Python 3.8+ 整数平方根
    # 对于旧版本：sqrt_num = int(math.sqrt(num)) + 1
    # 优化检查：从3开始，步进2
    for i in range(3, sqrt_num + 1, 2):  # +1 确保包含边界
        if num % i == 0:
            return False
    return True

def gcd(x,y):
    if x<y:
        x,y=y,x
    if y==0:
        return x
    return gcd(y,x%y)

def power(x, y):
    if y==0:
        return 1
    res=power(x*x%1000000007,y//2)
    if y%2==1:
        res=res*x%1000000007
    return res

def main():
    x=read_int()
    y=read_int()
    print(power(x,y))
    return

if __name__== "__main__":
    main()

