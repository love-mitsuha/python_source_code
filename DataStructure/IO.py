# 读入单个数字 类似cin
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
# 读入一个矩阵
def read_matrix():
    """
    多行输入：
    第一行为给定list的大小（比如：有n行数）
    用n，m接受输入大小
    用lis接受下面输入的矩阵
    """
    n, m = map(int, input().strip().split())
    lis = []
    for i in range(n):
        lis.append(list(map(int, input().split())))
    return n,m,lis # 返回维数和本体
# 读入一行返回int列表
def read_line_int():
    line = list(map(int, input().strip().split()))
    return line
# 读入一行返回分割int列表
def read_line_int_split():
    s=input()
    line=[]
    for i in range(len(s)):
        line.append(int(s[i]))
    return line



def main():
    m=read_matrix()
    print(m)
    return


if __name__== "__main__":
    main()
