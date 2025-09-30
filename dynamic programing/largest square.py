from utils import IO as io
def solution(c,h,w):
    # dp[i][j]表示向左上方扩展可形成的最大正方形边长
    dp=[[0 for i in range(w)]for j in range(h)]
    # 初始化
    for i in range(h):
        if c[i][0]==0:
            dp[i][0]=1
    for j in range(w):
        if c[0][j]==0:
            dp[0][j]=1
    # dp循环
    for i in range(1,h):
        for j in range(1,w):
            if c[i][j]==0:
                dp[i][j]=min(dp[i-1][j],dp[i-1][j-1],dp[i][j-1])+1
            else:
                dp[i][j]=0
    value=max(max(row)for row in dp)
    return value**2

def main():
    h,w,c = io.read_matrix()
    print(solution(c, h, w))
    return

if __name__ == "__main__":
    main()