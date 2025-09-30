# 最大堆为基础的优先级队列
class MaximumHeap:
    def __init__(self,nums):
        self.nums=[0]+nums # 下标从1开始
        self.length=len(nums)
        self.buildMaxHeap()

    def buildMaxHeap(self):
        for idx in range(self.length//2,0,-1):
            self.maxHeapify(idx)

    def maxHeapify(self,idx):
        l=2*idx
        r=2*idx+1
        largest=idx
        if l<=self.length and self.nums[largest]<self.nums[l]:
            largest=l
        if r<=self.length and self.nums[largest]<self.nums[r]:
            largest=r
        if largest!=idx:
            # 如果父结点不是最大 则与最大子结点对换
            self.nums[idx],self.nums[largest]=self.nums[largest],self.nums[idx]
            self.maxHeapify(largest) # 递归向下 因为换下去的数有可能更小

    def pop(self):
        ret=self.nums[1]
        self.nums[1]=self.nums[self.length]
        self.length-=1
        self.maxHeapify(1)
        return ret

    def push(self,value):
        self.length+=1
        self.nums.append(value)
        idx=self.length
        while idx>1 and self.nums[idx]>self.nums[idx//2]:
            self.nums[idx],self.nums[idx//2]=self.nums[idx//2],self.nums[idx] # 交换父结点与新增结点
            idx=idx//2

    # 堆排序 清空堆中元素
    def sort(self):
        nums=[]
        while self.length>0:
            nums.append(self.pop())
        return nums

class MinimumHeap:
    def __init__(self,nums):
        self.nums=[0]+nums # 下标从1开始
        self.length=len(nums)
        self.buildMinHeap()

    def __getitem__(self, item):
        return self.nums[item+1] # 下标从1开始

    def __setitem__(self, key, value):
        self.nums[key+1]=value # 下标从1开始

    def buildMinHeap(self):
        for idx in range(self.length//2,0,-1):
            self.minHeapify(idx)

    def minHeapify(self, idx):
        l=2*idx
        r=2*idx+1
        smallest=idx
        if l<=self.length and self.nums[smallest]>self.nums[l]:
            smallest=l
        if r<=self.length and self.nums[smallest]>self.nums[r]:
            smallest=r
        if smallest!=idx:
            self.nums[idx],self.nums[smallest]=self.nums[smallest],self.nums[idx]
            self.minHeapify(smallest) # 递归调用

    def pop(self):
        ret=self.nums[1]
        self.nums[1]=self.nums[self.length]
        self.length-=1
        self.minHeapify(1)
        return ret

    def push(self,value):
        self.length+=1
        self.nums.append(value)
        idx=self.length
        while idx>1 and self.nums[idx]<self.nums[idx//2]:
            self.nums[idx],self.nums[idx//2]=self.nums[idx//2],self.nums[idx] # 交换父结点与新增结点
            idx=idx//2

    # 堆排序 清空堆中元素
    def sort(self):
        nums=[]
        while self.length>0:
            nums.append(self.pop())
        return nums

def main():
    nums=[1,3,5,1,32,1,5,6,5,4,3,2,1,0]
    minimumHeap=MinimumHeap(nums)
    print(minimumHeap.sort())


if __name__ == "__main__":
    main()