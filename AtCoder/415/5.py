from utils import IO as io
# 答案有单调性 可以用二分求x
# 假设已知x 那么dp[i][j]设置成到达i行j列的最大金额值
# 因为钱越多 在往后走时越不可能饿死 贪心
neg_inf=-10**18
def check(x,h,w,cell,p):
    # dp[i][j]为到达i行j列的最大金额值
    dp = [[neg_inf]*w for _ in range(h)]
    dp[0][0]=x+cell[0][0]-p[0]
    if dp[0][0]<0:
        return False
    # dp
    for i in range(h):
        for j in range(w):
            if i==0 and j==0:
                continue
            from_left=neg_inf
            from_up=neg_inf
            # 从左侧来
            if j>0 and dp[i][j-1]>=0:
                from_left=dp[i][j-1]+cell[i][j]-p[i+j]
            if i>0 and dp[i-1][j]>=0:
                from_up=dp[i-1][j]+cell[i][j]-p[i+j]
            dp[i][j]=max(from_up,from_left)
    return dp[h-1][w-1]>=0

def main():
    h,w,cell=io.read_matrix()
    p=io.read_line_int()
    # ans=1e9 # 二分+动态规划 初始值为p中最值
    # l=0
    # r=sum(p)
    # while l<=r:
    #     mid=(l+r)>>1
    #     if check(mid,h,w,cell,p):
    #         r=mid-1
    #         ans=mid
    #     else:l=mid+1
    # print(ans)

    # 反向动态规划
    # dp[i][j]表示从位置ij开始走到右下终点时所需的最小金额
    # 从反向来看 ij所需的最小金额等于走向右边或者走向下面所需的最小金额加上当前位置的差价
    # 减去cell 加上p 因为这是反求当前位置的金额
    # 从i==h-1 j==w-1来看 就是求"还需补多少差价" 如果不需要补则为0
    dp=[[0]*w for _ in range(h)]
    for i in range(h-1,-1,-1):
        for j in range(w-1,-1,-1):
            if i<h-1 and j<w-1:
                dp[i][j]=max(min(dp[i+1][j],dp[i][j+1])-cell[i][j]+p[i+j],0)
            elif i<h-1:
                dp[i][j]=max(dp[i+1][j]-cell[i][j]+p[i+j],0)
            elif j<w-1:
                dp[i][j]=max(dp[i][j+1]-cell[i][j]+p[i+j],0)
            else:
                dp[i][j]=max(-cell[i][j]+p[i+j],0)
    print(dp[0][0])

if __name__== "__main__":
    main()