import math
from utils import IO as io

def solution(value,weight,w):
    m=len(value)
    # dp[i][j]前i种商品在背包容量为j时的最大价值
    dp=[[0 for i in range(w+1)]for j in range(m+1)]
    for i in range(1,m+1):
        for j in range(1,w+1):
            if j-weight[i-1]<0:
                dp[i][j]=dp[i-1][j]
                continue
            dp[i][j]=max(dp[i-1][j],dp[i-1][j-weight[i-1]]+value[i-1])
    return dp[m][w]

def main():
    n=io.read_int()
    w=io.read_int()
    value=[]
    weight=[]
    for i in range(n):
        value.append(io.read_int())
        weight.append(io.read_int())
    print(solution(value,weight,w))

if __name__ == "__main__":
        main()