import math
import heapq
import queue

#from DataStructure import io
def read_int():
    def get_numbers():
        try:#防止奇怪的东西出现
            read_int.s = input().split()
            read_int.s_len = len(read_int.s)
            if(read_int.s_len==0):get_numbers()#空行就继续
            read_int.cnt=0
            return 1#可以正常读
        except:#如果读到文件尾就不读了
            return 0
    if not hasattr(read_int, 'cnt'):
        if not get_numbers():return 0
    if read_int.cnt==read_int.s_len:
        if not get_numbers():return 0
    read_int.cnt+=1#下一个
    return eval(read_int.s[read_int.cnt - 1])#用eval,整数与小数通用，改成int或许会更快一点

class Tree:
    def __init__(self,vertex_num,edges):
        self.vertex_num=vertex_num
        self.edges=edges

    def dfs(self,current,distance,heap):
        for edge in self.edges[current]:
            v=edge[0]
            w=edge[1]
            if distance[v]==math.inf:
                distance[v]=distance[current]+w
                heapq.heappush(heap,(-distance[v],v)) # heapq只支持最小堆 要取负
                self.dfs(v,distance,heap)
    def bfs(self,begin,distance):
        que=[begin]
        while len(que)>=1:
            current=que.pop()
            for edge in self.edges[current]:
                v=edge[0]
                w=edge[1]
                if distance[v]==math.inf:
                    distance[v]=distance[current]+w
                    que.append(v)
    # 求树直径 深搜栈会爆
    def diameter(self):
        distance=[math.inf]*self.vertex_num
        distance[0]=0
        self.bfs(0,distance) # 默认0为广搜起点
        longest=0
        x=0 # x是从结点0开始到达的最远的边
        for i in range(self.vertex_num):
            if longest<distance[i]:
                longest=distance[i]
                x=i
        distance=[math.inf]*self.vertex_num
        distance[x]=0
        self.bfs(x,distance)
        longest=0
        y=0
        for i in range(self.vertex_num):
            if longest<distance[i]:
                longest=distance[i]
                y=i
        return distance[y] # x和y的距离 即树的直径

def main():
    n=read_int()
    edges=[[]for i in range(n)]
    for _ in range(n-1):
        s=read_int()
        t=read_int()
        w=read_int()
        edges[s].append((t,w))
        edges[t].append((s,w))
    tree=Tree(n,edges)
    print(tree.diameter())

if __name__== "__main__":
    main()