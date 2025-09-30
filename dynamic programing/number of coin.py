import math
from utils import IO as io
def solution(coins,n):
    m=len(coins) # 硬币种类
    # dp[i][j]数组含义是前i种硬币在支付j元时所需的最小硬币数量
    dp=[[0 for i in range(n+1)]for j in range(m+1)] # 数组包括了0 所以加一
    # 分为使用第i种硬币与不使用第i种硬币的情况
    # 比较两种情况选出最优的那个
    # 如果不选择 就和没有当前这个面值的硬币一样 所以直接使用dp[i-1][j]
    # 如果选择 则跳转到支付dp[i][j-coins[i-1]]的情况 这两个情况是一模一样的
    for i in range(1,n+1):
        dp[0][i]=math.inf # 初始化 使用零种硬币付钱不存在
    for i in range(1,m+1):
        for j in range(1,n+1):
            # 总金额小于当前面值时显然不可能使用
            if j-coins[i-1]<0:
                dp[i][j]=dp[i-1][j]
                continue
            dp[i][j]=min(dp[i-1][j],dp[i][j-coins[i-1]]+1)
    return dp[m][n]

def main():
    n=io.read_int()
    m=io.read_int()
    coins=[]
    for i in range(m):
        coins.append(io.read_int())
    print(solution(coins,n))
    return
if __name__ == "__main__":
        main()