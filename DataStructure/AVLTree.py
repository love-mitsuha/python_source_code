from BinarySearchTree import BinarySearchTree
from template import *
class Node:
    def __init__(self,value=None):
        self.value=value
        self.lchild=None
        self.rchild=None
        self.height=0
class AVLTree(BinarySearchTree):
    def __init__(self, iteration=None):
        super().__init__()  # 调用父类初始化（如果父类也需要）
        self.root = None
        if type(iteration) is list:
            for num in iteration:
                self.insert(num)
    def get_height(self, node:Node):
        if node is None:
            return -1
        else:
            return node.height
    def singleRightRotate(self,node:Node):
        new_root=node.lchild
        node.lchild=new_root.rchild
        new_root.rchild=node
        node.height= max(self.get_height(node.lchild), self.get_height(node.rchild))+1
        new_root.height=max(self.get_height(new_root.lchild),self.get_height(new_root.rchild))+1
        return new_root
    def singleLeftRotate(self,node:Node):
        new_root=node.rchild
        node.rchild=new_root.lchild
        new_root.lchild=node
        node.height=max(self.get_height(node.lchild),self.get_height(node.rchild))+1
        new_root.height=max(self.get_height(new_root.lchild),self.get_height(new_root.rchild))+1
        return new_root
    def leftRightRotate(self,node:Node):
        node.lchild=self.singleLeftRotate(node.lchild)
        return self.singleRightRotate(node)
    def rightLeftRotate(self,node:Node):
        node.rchild=self.singleRightRotate(node.rchild)
        return self.singleLeftRotate(node)
    # 返回插入后的子树节点
    def _insert_avl(self,node:Node,value):
        if node is None:
            node=Node(value)
            return node
        elif value == node.value:
            return node
        elif value<node.value:
            node.lchild=self._insert_avl(node.lchild,value)
            if self.get_height(node.lchild)-self.get_height(node.rchild)>=2:
                # 左左 一次右旋
                if self.get_height(node.lchild.lchild) > self.get_height(node.lchild.rchild):
                    node = self.singleRightRotate(node)
                # 左右 先左旋后右旋
                else:
                    node = self.leftRightRotate(node)
        else:
            node.rchild=self._insert_avl(node.rchild,value)
            if self.get_height(node.rchild) - self.get_height(node.lchild) >= 2:
                # 右右 一次左旋
                if self.get_height(node.rchild.rchild) > self.get_height(node.rchild.lchild):
                    node = self.singleLeftRotate(node)
                # 右左 先右旋后左旋
                else:
                    node = self.rightLeftRotate(node)
        node.height=max(self.get_height(node.lchild),self.get_height(node.rchild))+1
        return node
    # 按值插入
    def insert(self,value):
        self.root=self._insert_avl(self.root,value)
        return self.root
    # 返回每次删除并进行平衡后的子树节点
    def _delete(self,node:Node,value):
        if node is None:
            return None
        elif value==node.value:
            # 如果只有右子树
            if node.lchild is None:
                return node.rchild
            # 如果只有左子树
            elif node.rchild is None:
                return node.lchild
            # 双子树时
            else:
                # 左子树高于右子树时
                if self.get_height(node.lchild)>self.get_height(node.rchild):
                    # 找到左子树的最大节点
                    r=node.lchild
                    while r.rchild is not None:
                        r=r.rchild
                    node=self._delete(node,r.value)
                    node.value=r.value
                    return node
                else:
                    # 找到右子树的最小节点
                    l=node.rchild
                    while l.lchild is not None:
                        l=l.lchild
                    node=self._delete(node,l.value)
                    node.value=l.value
                    return node
        # 值比当前节点小
        elif value<node.value:
            # 递归删除左侧值 只会造成右子树高
            node.lchild=self._delete(node.lchild,value)
            if self.get_height(node.rchild) - self.get_height(node.lchild) >= 2:
                # 右右 一次左旋
                if self.get_height(node.rchild.rchild)>self.get_height(node.rchild.lchild):
                    node=self.singleLeftRotate(node)
                # 右左 先右旋后左旋
                else:
                    node=self.rightLeftRotate(node)
        elif value>node.value:
            # 递归删除右侧值 只会造成左子树高
            node.rchild=self._delete(node.rchild,value)
            if self.get_height(node.lchild)-self.get_height(node.rchild)>=2:
                # 左左 一次右旋
                if self.get_height(node.lchild.lchild)>self.get_height(node.lchild.rchild):
                    node=self.singleRightRotate(node)
                # 左右 先左旋后右旋
                else:
                    node=self.leftRightRotate(node)
        node.height = max(self.get_height(node.lchild), self.get_height(node.rchild)) + 1
        return node
    # 按值删除
    def delete(self,value):
        self.root=self._delete(self.root,value)
def main():
    # nums=[1,3,2,45,645,6,2346,245,23,5,34567,7,341,4,124,12]
    # tree=AVLTree(nums)
    # tree.traverse()
    # for num in nums:
    #     tree.delete(num)
    #     tree.traverse()
    tree=AVLTree()
    insert_time = []
    delete_time = []
    for right_interval in range(1000, 500000, 50000):
        array = np.random.randint(1, 100, right_interval)
        since = time.time()
        for i in array:
            tree.insert(i)
        end = time.time() - since
        insert_time.append(end)
        print('AVL insert : ' + str(right_interval) + ' Data: ' + str(end) + 's')
    for right_interval in range(1000, 500000, 50000):
        array = np.random.randint(1, 100, right_interval)
        since = time.time()
        for i in array:
            tree.delete(i)
        end = time.time() - since
        delete_time.append(end)
        print('AVL delete : ' + str(right_interval) + ' Data: ' + str(end) + 's')
        for i in array:
            tree.insert(i)
if __name__=='__main__':
    main()