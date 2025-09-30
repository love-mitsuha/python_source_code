import math
class BinomialNode:
    def __init__(self,value):
        self.value=value
        self.degree=0
        self.child=[]

# 连接阶相同的根节点xy
# 因最小堆 取xy中较小的点作根节点
def link(root_x:BinomialNode, root_y:BinomialNode)->BinomialNode:
    if root_x.value < root_y.value:
        root_x.child.append(root_y)
        root_x.degree+=1
        return root_x
    else:
        root_y.child.append(root_x)
        root_y.degree+=1
        return root_y
# 二项堆 用于频繁合并堆
# 由一组不同高度的二项树组成 每颗二项树结点数为2^k
class BinomialHeap:
    def __init__(self,iteration=None):
        if iteration is None:
            self.heap = {}
        elif type(iteration)==dict:
            self.heap=iteration
        elif type(iteration)==list:
            self.heap={}
            for num in iteration:
                self.insert(num)
    # 获取最小值
    def get_min(self):
        num_min=math.inf
        for k,v in self.heap.items():
            if num_min>v.value:
                num_min=v.value
        return num_min
    # 插入一个值
    def insert(self,value):
        node=BinomialNode(value)
        while node.degree in self.heap:
            node=link(node,self.heap[node.degree])
            self.heap.pop(node.degree-1)
        self.heap[node.degree]=node
    # 弹出最小值
    def pop_min(self):
        num_min = math.inf
        k_min=-1
        root=None
        for k, v in self.heap.items():
            if num_min > v.value:
                num_min = v.value
                k_min=k
                root=v
        self.heap.pop(k_min)
        for node in root.child:
            while node.degree in self.heap:
                node=link(node,self.heap[node.degree])
                self.heap.pop(node.degree-1)
            self.heap[node.degree]=node
        return num_min
    # 合并两个二项堆
    def union(self,other):
        dic = {}
        tree_degree_x = []
        tree_degree_y = []
        for k, v in self.heap.items():
            tree_degree_x.append(k)
        for k, v in other.heap.items():
            tree_degree_y.append(k)
        tree_degree_x.sort()
        tree_degree_y.sort()
        for k in tree_degree_x:
            root = self.heap[k]
            while k in dic:
                root = link(self.heap[k], dic[k])
                dic.pop(k)
                k = root.degree
            dic[k] = root
        for k in tree_degree_y:
            root = other.heap[k]
            while k in dic:
                root = link(other.heap[k], dic[k])
                dic.pop(k)
                k = root.degree
            dic[k] = root
        self.heap=dic

def main():
    nums=[3,4,1,2,6]
    heap=BinomialHeap(nums)
    heap.union(BinomialHeap([10,2,3,4,50]))
    return
if __name__=="__main__":
    main()