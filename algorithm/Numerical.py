
# 计算n除以1-n的结果之和
def div(n,mod):
    ans=0
    l = 1
    while l <= n:
        # 计算当前块的右边界
        r = n // (n // l)
        # 计算当前块的贡献值（区间长度 × 公共值）
        term = (r - l + 1) * (n // l)
        # 更新答案（防止负数的模运算技巧）
        ans = (ans + term) % mod
        ans = (ans + mod) % mod  # 确保结果非负
        # 跳转到下一个块
        l = r + 1
    return ans

def main():
    print(div(5,10000))

if __name__== "__main__":
    main()