import bisect
from utils import IO as io
# 只使用动态规划
def solution(nums):
    # nums中第一个元素为-1
    n=len(nums)
    # l[i]表示包括第i个数的最长子序列
    length=[0 for i in range(n)]
    for i in range(1,n):
        k=0
        for j in range(1,i):
            if nums[i]>nums[j] and length[j]>length[k]:
                k=j
        length[i]=length[k]+1
    return max(length)
# 二分查找+动态规划
def LIS(nums):
    length=1
    n=len(nums)
    l=[0 for i in range(n)]
    l[0] = nums[0]
    for i in range(1,n):
        if l[length-1]<nums[i]:
            l[length]=nums[i]
            length+=1
        else:
            l[bisect.bisect_left(l,nums[i],0,length)]=nums[i]
    return length

def main():
    n=io.read_int()
    nums=[]
    for i in range(n):
        nums.append(io.read_int())
    print(LIS(nums))

if __name__ == "__main__":
    main()
