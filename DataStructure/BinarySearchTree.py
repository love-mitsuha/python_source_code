class Node:
    def __init__(self,value=None):
        self.value=value
        self.lchild=None
        self.rchild=None
        self.height=0
class BinarySearchTree:
    def __init__(self,iteration=None):
        self.root=None
        if type(iteration) is list:
            for num in iteration:
                self.insert(num)
        else:
            self.root=Node()
    def _search(self,node:Node|None,parent:Node|None,value):
        if node is None:
            return False,None,parent
        if value==node.value:
            return True,node,parent
        elif value<node.value:
            return self._search(node.lchild,node,value)
        else:
            return self._search(node.rchild,node,value)
    def search(self,value):
        return self._search(self.root,None,value)
    def _insert(self,node:Node|None,parent:Node|None,value):
        if node is None:
            node=Node(value)
            if value<parent.value:
                parent.lchild=node
            else:
                parent.rchild=node
        elif value<node.value:
            self._insert(node.lchild,node,value)
        else:
            self._insert(node.rchild,node,value)
    def insert(self,value):
        if self.root is None:
            self.root=Node(value)
        else:
            self._insert(self.root,None,value)
    # 以node为根节点的最小值
    def _get_min(self,node:Node|None,parent:Node|None):
        if node.lchild is None:
            return node,parent
        else:
            return self._get_min(node.lchild,node)
    # 按值删除
    def _delete(self,node,parent):
        # 如果是叶子节点 直接删除
        if node.lchild is None and node.rchild is None:
            if node is parent.lchild:
                parent.lchild=None
            else:
                parent.rchild=None
        # 如果有两个子节点
        # 将右子树的最小节点移至当前位置
        elif node.lchild is not None and node.rchild is not None:
            min_node, min_node_parent = self._get_min(node.rchild, node)
            node.value = min_node.value
            # 递归删除
            self._delete(min_node,min_node_parent)
        # 如果有一个子节点
        else:
            # 如果要删的是根节点
            if parent is None:
                if node.lchild:
                    self.root=node.lchild
                else:
                    self.root=node.rchild
            else:
                if node.lchild:
                    if node is parent.lchild:
                        parent.lchild = node.lchild
                    else:
                        parent.rchild = node.lchild
                else:
                    if node is parent.lchild:
                        parent.lchild = node.rchild
                    else:
                        parent.rchild = node.rchild
    def delete(self,value):
        flag, node, parent = self._search(self.root,None, value)
        if not flag:
            raise ValueError(f"{value} not found in BST")
        else:
            self._delete(node,parent)
    # 中序遍历
    def _traverse(self,node):
        if node is None:
            return
        self._traverse(node.lchild)
        print(f'{node.value}',end=" ")
        self._traverse(node.rchild)
    # 遍历打印
    def traverse(self):
        self._traverse(self.root)
        print()
def main():
    nums=[5,2,5,34,534,5,34,667,456,45,7]
    tree=BinarySearchTree(nums)
    tree.delete(5)
    tree.delete(7)
    tree.delete(5)
    tree.insert(4)
    tree.insert(67)
    tree.delete(67)
    tree.insert(78)
    tree.traverse()
    return
if __name__=="__main__":
    main()