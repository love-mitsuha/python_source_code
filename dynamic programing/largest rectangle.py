from utils import IO as io
def solution(h,w,c):
    # 表t代表从t[i][j]开始到正上方的最长长方形高度
    t=[[0 for i in range(w)]for j in range(h)]
    ret=0
    # 初始化
    for i in range(w):
        if c[0][i]==0:
            t[0][i]=1
    # dp求得t
    # t是直方图
    for j in range(w):
        for i in range(1,h):
            if c[i][j]==1:
                t[i][j]=0
            else:
                t[i][j]=t[i-1][j]+1
    for i in range(h):
        line=t[i]
        s=[]
        maxv=0
        for j in range(w):
            if len(s)==0:
                s.append((line[j],j))
            elif s[-1][0]<line[j]:
                s.append((line[j],j))
            elif s[-1][0]>line[j]:
                target=j
                while len(s)!=0 and s[-1][0]>=line[j]:
                    pre=s.pop()
                    area=pre[0]*(j-pre[1])
                    maxv=max(maxv,area)
                    target=pre[1]
                s.append((line[j],target))
        while len(s)!=0:
            cur=s.pop()
            area=cur[0]*(w-cur[1])
            maxv=max(maxv, area)
        ret=max(maxv,ret)
    return ret

def main():
    h,w,c=io.read_matrix()
    print(solution(h,w,c))

if __name__ == "__main__":
    main()


