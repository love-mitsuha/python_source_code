# 并查集 将0——n-1的数进行划分

class DisjointSet:
    def __init__(self,n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def findSet(self,x):
        # 递归查找根节点 路径压缩
        if x!=self.parent[x]:
            self.parent[x]=self.findSet(self.parent[x])
        # 压缩完成后返回根节点 此时集合内所有元素直接指向根节点
        return self.parent[x]

    def unite(self,x,y):
        root_x=self.findSet(x)
        root_y=self.findSet(y)
        if self.rank[root_x]<self.rank[root_y]:
            self.parent[root_x]=root_y
            self.rank[root_y]+=1
        else:
            self.parent[root_y]=root_x
            self.rank[root_x]+=1

    def same(self,x,y):
        if self.findSet(x)==self.findSet(y):
            return True
        else:return False

def main():
    n,q=map(int,input().split())
    mySet=DisjointSet(n)
    for _ in range(q):
        idx,x,y=map(int,input().split())
        if idx==0:
            mySet.unite(x,y)
        elif idx==1:
            print(mySet.same(x,y))

if __name__== "__main__":
    main()