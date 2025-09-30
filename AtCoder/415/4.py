def read_line():
    line = list(map(int, input().strip().split()))
    return line
# 贪心
def main():
    line=read_line()
    n,m=line[0],line[1]
    a=[]
    for i in range(m):
        l=read_line()
        a.append((l[0]-l[1],l[0],l[1]))
    a.sort()
    cur=n
    ans=0
    for i in range(m):
        if cur>=a[i][1]:
            # 剩下最后一次交换
            cnt=(cur-a[i][1])//a[i][0]+1
            ans+=cnt
            cur-=a[i][0]*cnt
    print(ans)

if __name__== "__main__":
    main()


