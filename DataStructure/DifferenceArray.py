# 差分数组 高效维护对数组区间的同时加减一个数操作
class DiffArray:
    def __init__(self,_nums):
        self.nums=[0]+_nums
        self.length=len(_nums)
        self.difference=[0]*(self.length+1)
        for i in range(1,self.length+1):
            self.difference[i]=self.nums[i]-self.nums[i-1]
    # l,r分别为序号 v是更新值
    def update(self,l,r,v):
        self.difference[l]+=v
        self.difference[r+1]-=v
    # O(n)
    def find(self,idx):
        nums=[0]*(self.length+1)
        for i in range(1,self.length+1):
            nums[i]=nums[i-1]+self.difference[i]
        return nums[idx]
def main():
    a=[1,3,4,1,6,7,2,8,4,1,3,4]
    nums=DiffArray(a)
    nums.update(1,8,9)
    nums.update(2,6,-5)
    print(nums.find(5))
    return
if __name__== "__main__":
    main()