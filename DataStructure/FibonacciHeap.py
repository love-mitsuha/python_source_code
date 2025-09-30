import random
class FibonacciNode:
    def __init__(self,value,name=None):
        self.name=name
        self.value=value
        self.left:FibonacciNode=self # 指向自己
        self.right:FibonacciNode=self
        self.degree=0 # 子节点个数
        self.child:FibonacciNode|None=None # 初始值为空
        self.parent:FibonacciNode|None=None
        self.mark=False
def _remove_from_list(node:FibonacciNode):
    if node.parent is not None:
        node.parent.degree-=1
        if node.parent.child is node:
            # 如果父节点孩子不止node
            if node.right is not node:
                node.parent.child = node.right
            # 如果父节点孩子只有node
            else:
                node.parent.child = None
    node.left.right=node.right
    node.right.left=node.left
    node.left=node.right=node
    node.parent=None
    node.mark=False
    return node
# 合并两棵子树
# 将值较大的数作为值较小的树的子树
def _merge(smaller:FibonacciNode,bigger:FibonacciNode):
    bigger = _remove_from_list(bigger)
    # 取出较小树孩子列表
    bigger.parent=smaller
    bigger.mark=False
    if smaller.child is None:
        smaller.child=bigger
        bigger.left = bigger.right = bigger
    else:
        child=smaller.child
        child_left=child.left
        child_left.right=bigger
        child.left=bigger
        bigger.left=child_left
        bigger.right=child
    # 升阶
    smaller.degree+=1

class FibonacciHeap:
    def __init__(self,iteration=None):
        self.min_node:FibonacciNode|None=None
        self.cnt=0
        self.finder:dict[str,FibonacciNode]={}
        if iteration is None:
            self.min_node=None
        elif type(iteration) is list:
            for num in iteration:
                node=FibonacciNode(num,f'{num}')
                self.insert(node)
                self.finder[f'{num}']=node
            self._consolidate()

    def _add_to_root_list(self,node:FibonacciNode):
        if self.min_node is None:
            self.min_node=node
        else:
            node.left = self.min_node.left
            node.right = self.min_node
            self.min_node.left.right = node
            self.min_node.left = node

    # 在最小节点左边插入
    def insert(self,node:FibonacciNode):
        self.finder[node.name]=node
        if self.min_node is None:
            self.min_node=node
        else:
            left=self.min_node.left
            left.right = node
            node.left = left
            self.min_node.left = node
            node.right = self.min_node
        if node.value<self.min_node.value:
            self.min_node=node
        self.cnt+=1
    def pop_min(self):
        if self.min_node is None:
            return None
        elif self.min_node.child is None:
            self.finder.pop(self.min_node.name)
            self.cnt -= 1
            # 如果只有这一个节点了
            if self.min_node is self.min_node.right:
                ret=self.min_node.value
                self.min_node=None
                return ret
            self.min_node=self.min_node.right
            ret = _remove_from_list(self.min_node.left).value
            # 后续找最小根
            start=self.min_node
            current=self.min_node.right
            while current is not start:
                if current.value<self.min_node.value:
                    self.min_node=current
                current=current.right
            return ret
        else:
            self.finder.pop(self.min_node.name)
            root = self.min_node
            child = root.child
            temp = [child]
            current = child.right
            while current is not child:
                temp.append(current)
                current = current.right
            for node in temp:
                self._add_to_root_list(_remove_from_list(node))
            _remove_from_list(root)
            self.min_node=temp[0] # 随便找一个暂时作为最小节点
            self._consolidate()
            self.cnt-=1
            return root.value

    # 合并所有同阶树
    # 更新min_node
    def _consolidate(self):
        start=self.min_node
        current=start.right
        temp = [start]
        while current is not start:
            temp.append(current)
            current=current.right
        self.min_node=None
        dic= {}
        for node in temp:
            _remove_from_list(node)
            current=node
            while current.degree in dic:
                if current.value<dic[current.degree].value:
                    smaller=current
                    bigger=dic[current.degree]
                else:
                    smaller=dic[current.degree]
                    bigger=current
                dic.pop(current.degree)
                _merge(smaller,bigger)
                current=smaller
            dic[current.degree]=current
        for node in dic.values():
            node.left=node.right=node
            node.mark=False
            node.parent=None
            if self.min_node is None:
                self.min_node=node
            else:
                self._add_to_root_list(node)
                if node.value<self.min_node.value:
                    self.min_node=node
    # 将指定的节点值减小为value
    def decrease_key(self,name,value):
        node=self.finder[name]
        if value>node.value:
            print("only decrease!")
            return
        node.value=value
        node_parent=node.parent
        if node_parent is not None and value<node_parent.value:
            # 移除node
            self._add_to_root_list(_remove_from_list(node))
            current=node_parent
            # 级联切割
            while current.parent is not None and current.mark:
                current_parent=current.parent
                self._add_to_root_list(_remove_from_list(current))
                current=current_parent
            if current.parent is not None:
                current.mark=True
        if self.min_node is None or node.value<self.min_node.value:
                self.min_node=node



def main():
    nums=[i for i in range(100)]
    heap=FibonacciHeap(nums)
    heap.decrease_key('99',1)
    heap.decrease_key('98',23)
    heap.decrease_key('97',38)
    heap.decrease_key('96',47)
    heap.decrease_key('95',56)
    heap.decrease_key('43',41)
    heap.decrease_key('91',6)
    heap.decrease_key('23',14)
    heap.decrease_key('34',31)
    heap.decrease_key('45',24)
    heap.decrease_key('56',56)
    for i in range(100):
        print(heap.pop_min())

    return
if __name__=="__main__":
    main()