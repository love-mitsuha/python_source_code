# 最小成本排序

import re
import copy

def main():
    #file = open("../instruction.txt", "r")
    #s = file.read()

    n=input()
    s=input()
    #print(s)
    numbers=[int(num)for num in re.findall(r'\d+\.?\d*',s)]
    #print(numbers)
    numbers_dict={num:idx+1 for idx,num in enumerate(numbers)}
    #print(numbers_dict)
    numbers_sort=copy.deepcopy(numbers)
    numbers_sort.sort()
    #print(numbers_sort)
    numbers_sort_dict={num:idx+1 for idx,num in enumerate(numbers_sort)}
    #print(numbers_sort_dict)

    visited=set()
    cost=0
    for current in numbers:
        if current in visited:
            continue
        circle=set() # 构建圆
        idx_start = numbers_dict[current] # 初始节点
        cnt=1 # 初始有一个结点
        while 1:
            visited.add(current)
            circle.add(current)
            idx_target = numbers_sort_dict[current]
            if idx_target==idx_start: # 如果到达自己则终结
                break
            current=numbers[idx_target-1]
            cnt=cnt+1
        if cnt==1:
            continue
        elif cnt==2:
            cost=cost+sum(circle)
        else:
            cost1=sum(circle)+(cnt-2)*min(circle)
            outer=min(numbers)
            cost2=sum(circle)+min(circle)+(cnt+1)*outer
            if cost1<cost2:
                cost=cost+cost1
            else:
                cost=cost+cost2
    print(cost)

if __name__== "__main__":
    main()
