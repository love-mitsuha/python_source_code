# KD Tree
# 范围搜索二维平面点 无增删操作
# 优化TODO 剪枝 IO
# 52/100

def read():
    def get_numbers():
        try:#防止奇怪的东西出现
            read.s = input().split()
            read.s_len = len(read.s)
            if(read.s_len==0):get_numbers()#空行就继续
            read.cnt=0
            return 1#可以正常读
        except:#如果读到文件尾就不读了
            return 0
    if not hasattr(read, 'cnt'):
        if not get_numbers():return 0
    if read.cnt==read.s_len:
        if not get_numbers():return 0
    read.cnt+=1#下一个
    return eval(read.s[read.cnt-1])#用eval,整数与小数通用，改成int或许会更快一点


# 点的信息
class Point:
    def __init__(self,idx,x,y):
        self.id=idx
        self.x=x
        self.y=y
# 二叉树的结点
class Node:
    def __init__(self):
        self.location=0
        self.l=0
        self.r=0

class Tree2D:
    def __init__(self,n,points):
        self.n=n
        self.root=0 # 根节点编号为0
        self.nodes=[Node() for i in range(n)]
        self.points=points
        self.np=0

    def make2DTree(self,l,r,depth):
        if l>r:
            return
        mid=int((l+r)/2)
        t=self.np
        self.np=self.np+1

        if depth%2==0:
            self.points[l:r+1]=sorted(self.points[l:r+1],key=lambda p:p.x)
        else: self.points[l:r+1]=sorted(self.points[l:r+1],key=lambda p:p.y)

        self.nodes[t].location=mid
        self.nodes[t].l=self.make2DTree(l,mid-1,depth+1)
        self.nodes[t].r=self.make2DTree(mid+1,r,depth+1)
        return t

    def find(self,root,sx,tx,sy,ty,depth,ans):
        x=self.points[self.nodes[root].location].x
        y=self.points[self.nodes[root].location].y

        if sx<=x<=tx and sy<=y<=ty:
            ans.append(self.points[self.nodes[root].location])

        if depth%2==0:
            if self.nodes[root].l and sx<=x:
                self.find(self.nodes[root].l,sx,tx,sy,ty,depth+1,ans)
            if self.nodes[root].r and x<=tx:
                self.find(self.nodes[root].r,sx,tx,sy,ty,depth+1,ans)
        else:
            if self.nodes[root].l and sy<=y:
                self.find(self.nodes[root].l,sx,tx,sy,ty,depth+1,ans)
            if self.nodes[root].r and y<=ty:
                self.find(self.nodes[root].r,sx,tx,sy,ty,depth+1,ans)


def main():
    n=read()
    points=[]
    for i in range(n):
        # x=read()
        # y=read()
        x,y=map(int,input().split())
        point=Point(i,x,y)
        points.append(point)
    tree=Tree2D(n,points)
    tree.make2DTree(0,n-1,0) # 到这里
    q=read()
    for i in range(q):
        # sx=read()
        # tx=read()
        # sy=read()
        # ty=read()
        sx,tx,sy,ty=map(int,input().split())
        ans=[]
        tree.find(0,sx,tx,sy,ty,0,ans)
        ans.sort(key= lambda p:p.id)
        for item in ans:
            print(item.id)
        print()

    return

if __name__== "__main__":
    main()