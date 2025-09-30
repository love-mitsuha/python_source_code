# 插入排序
# i为未排序部分开头元素
# j用于查找插入位置 同时移动数组元素
def insertion_sort(nums):
    length=len(nums)
    for i in range(1,length):
        num=nums[i]
        j=i-1
        while j>=0 and nums[j]>num: # 由此可知是稳定排序
            nums[j+1]=nums[j]
            j=j-1
        nums[j+1]=num

# 折半插入排序
# 二分查找插入点
def half_insertion(nums):
    length = len(nums)
    for i in range(1,length):
        num=nums[i]
        l,r=0,i-1
        # 二分查找
        while l<=r:
            mid=(l+r)//2
            if num<nums[mid]:
                r=mid-1
            else:l=mid+1
        # 移动元素
        j=i-1
        while j>=r+1:
            nums[j+1]=nums[j]
            j=j-1
        nums[r+1]=num

# 希尔排序
# 增量函数除二衰减
def shell_sort(nums):
    length=len(nums)
    dk=length//2
    while dk>0:
        i=dk
        while i<length:
            v=nums[i] # 将要进行排序的值
            j=i-dk
            # 向前扫描排序 前面的值已经有序
            while j>=0 and nums[j]>v:
                nums[j+dk]=nums[j]
                j=j-dk
            nums[j+dk]=v
            i+=1
        dk=dk//2

# 冒泡排序
def bubble_sort(nums):
    length=len(nums)
    i=0
    while i<length-1:
        flag=False
        j=length-1 # 从后往前 携带最小的数
        while j>i:
            if nums[j-1]>nums[j]:
                nums[j-1],nums[j]=nums[j],nums[j-1] # 交换元素
                flag=True
            j-=1
        i+=1
        if not flag:
            break

# 快速排序
def partition(nums,l,r):
    pivot=nums[l] # 取第一个元素作轴
    # 外部l<r控制整体多次循环
    while l<r:
        # 内部也必须有l<r 防止l,r溢出
        while l<r and nums[r]>=pivot:
            r-=1
        nums[l]=nums[r]
        while l<r and nums[l]<=pivot:
            l+=1
        nums[r]=nums[l]
    nums[l]=pivot # 最后填枢轴值 此时l==r
    return l
def quick_sort(nums,l,r):
    if l<r:
        pivot=partition(nums,l,r)
        quick_sort(nums,l,pivot-1)
        quick_sort(nums,pivot+1,r)

# 不稳定
# 选择排序
def selection_sort(nums):
    length=len(nums)
    for i in range(length-1):
        min_=nums[i] # 未排序部分最小数
        k=i
        for j in range(i+1,length):
            if min_>nums[j]:
                min_=nums[j]
                k=j
        nums[i],nums[k]=nums[k],nums[i]

# 归并排序
# l mid r 均为下标
def merge(nums,l,mid,r):
    n1=mid-l+1 # 数组长度
    n2=r-mid
    left=nums[l:l+n1]
    right=nums[mid+1:mid+1+n2]
    i,j,k=0,0,l
    while k <=r and i<n1 and j<n2:
        if left[i]<=right[j]:
            nums[k]=left[i]
            i+=1
        else:
            nums[k]=right[j]
            j+=1
        k+=1
    # 若其中有一个列表已经循环完毕则直接复制另一个列表
    while i<n1:
        nums[k]=left[i]
        i+=1
        k+=1
    while j<n2:
        nums[k]=right[j]
        j+=1
        k+=1
def merge_sort(nums,l,r):
    if l<r:
        mid=(l+r)//2
        merge_sort(nums,l,mid)
        merge_sort(nums,mid+1,r)
        merge(nums,l,mid,r)

# 计数排序
# 只能排正整数
# time O(n+k) k为nums最大值
# 返回排序的数组 并非在原有数组改动
def counting_sort(nums):
    length=len(nums)
    count=[0]*(max(nums)+1)
    ret=[0]*length
    for i in range(length):
        count[nums[i]]+=1
    for i in range(1,len(count)):
        count[i]+=count[i-1]
    for i in range(length-1,-1,-1):
        ret[count[nums[i]]-1]=nums[i]
        count[nums[i]]-=1
    return ret

# 基数排序 稳定
def base_sort(nums):
    length=len(nums)
    q=[[]for i in range(10)]
    d=len(str(max(nums))) # 最大数字位数 也即分配收集次数
    for i in range(1,d+1): # 取第i位
        # 分配
        for _ in q:
            _.clear()
        for j in range(length):
            num=nums[j]
            num_str=str(num)
            base=0 if i>len(num_str) else int(num_str[-i])
            q[base].append(num)
        # 收集
        nums.clear()
        for j in range(10):
            nums+=q[j]


def main():
    q=[1,3,7,2,4,9,5,8,10,6]
    quick_sort(q,0,9)
    print(q)
    return



if __name__ == "__main__":
        main()