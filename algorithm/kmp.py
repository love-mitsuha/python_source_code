# 匹配成功则返回在s中的首字母下标
# 失败则返回-1
def kmp_search(s,pattern):
    n=len(s)
    m=len(pattern)
    # 求next数组
    # 表示当前字符如果不匹配时应当返回到第几个数
    nex=[0]*(m+1)
    # i指向当前扫描的字符
    # j指向可能匹配的前缀
    i,j=1,0
    while i<m:
        # 前缀中没有可匹配的串或者匹配成功时:
        if j==0 or pattern[i-1]==pattern[j-1]:
            i+=1
            j+=1
            if pattern[i-1]!=pattern[j-1]:
                nex[i]=j
            # 如果i与j的字符一样
            # 需要将nex[i]更新到j的上一个模式匹配串
            # 此时字符nex[i]与nex[j]指向字符一定不一样
            else:
                nex[i]=nex[j]
        else:
            # 因为j与nex[j]也一定有相同前缀匹配
            # 所以寻找j之前的模式匹配串 继续循环判断
            # 直到某个k与i代表字符相等或找不到前缀了
            j=nex[j]
    # 求子串
    i,j=1,1
    while i<=n and j<=m:
        # 当主串第i位与模式串第一位不等 主串向后移一位
        # 如果匹配则同时向后移
        # 此时nex[1]=0发挥了作用 因为0+1=1刚好使模式串重新从1开始计数
        if j==0 or s[i-1]==pattern[j-1]:
            i+=1
            j+=1
        else:
            j=nex[j]
    if j>=m:
        return i-m-1
    else:
        return -1

def main():
    idx=kmp_search("aaabaaaab","aaaab")
    print(idx)
    return
if __name__== "__main__":
    main()
