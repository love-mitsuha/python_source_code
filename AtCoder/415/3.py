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
def read_line():
    line = list(map(int, input().strip().split()))
    return line
# 读入一行返回分割int列表
def read_line_int_split():
    s=input()
    line=[]
    for i in range(len(s)):
        line.append(int(s[i]))
    return line

def bfs():
    n = read_int()
    s = read_line_int_split()
    # 记录已经达到过的状态
    # 如果为True说明已经不可达 不必再判断
    state = [False] * (pow(2, n) - 1)
    que = [0]
    while que:
        u = que.pop()
        if u == pow(2, n) - 1:
            print("Yes")
            return
        for i in range(n):
            # 为真则说明已经加入过药品i
            if (u >> i) & 1:
                continue
            # 加入药品i
            v = u | (1 << i)
            # 如果有毒或者已经到达过当前状态则跳过
            # 当前状态曾经到达过时 说明该状态之后不会有合法的加入顺序
            if s[v - 1] == 1 or state[v - 1]:
                continue
            state[v - 1] = True
            que.append(v)
    print("No")

def dynamic():
    n = read_int()
    s = read_line_int_split()
    # dp[i]表示状态i能否安全到达
    dp=[False]*(pow(2,n))
    dp[0]=True
    for i in range(1,pow(2,n)):
        for j in range(n):
            # 如果状态i中有药品j
            if (i>>j)&1:
                # 则当前状态是否可达取决于没有添加药品j时的状态与s中的值
                if s[i-1]!=1 and dp[i^(1<<j)]:
                    dp[i]=True
    if dp[pow(2,n)-1]:
        print("Yes")
    else:print("No")

# bfs
def main():
    t=read_int()
    for i in range(t):
        dynamic()

if __name__== "__main__":
    main()
