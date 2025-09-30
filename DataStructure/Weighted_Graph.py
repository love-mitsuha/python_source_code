from utils import IO
from utils import DisjointSet
import math
import heapq

class Graph:
    # 读取
    # n = io.read_int()
    # adj_matrix = [[False for i in range(n)] for j in range(n)]
    # for i in range(n):
    #     u = io.read_int()
    #     k = io.read_int()
    #     for j in range(k):
    #         v = io.read_int()
    #         adj_matrix[u - 1][v - 1] = True

    def __init__(self,vertex_num,adj_matrix,edges,storage_type):
        self.vertex_num=vertex_num
        if storage_type=="matrix":
            self.adj_matrix=adj_matrix
        elif storage_type=="list":
            # 选择邻接表是也会存储邻接矩阵
            self.adj_matrix=adj_matrix
            self.adj_list=[[]for i in range(self.vertex_num)]
            self.create_List()
        elif storage_type=="edges":
            self.edges=edges

    def create_List(self):
        for i in range(self.vertex_num):
            for j in range(self.vertex_num):
                if self.adj_matrix[i][j]!=math.inf:
                    self.adj_list[i].append((j,self.adj_matrix[i][j]))

    # 最小生成树
    # 默认从结点零开始
    def prim(self):
        vertex_num=self.vertex_num
        adj_matrix=self.adj_matrix
        visited=[False]*vertex_num
        distance=[math.inf]*vertex_num
        distance[0]=0
        while True:
            mincost=math.inf
            u=-1
            for i in range(vertex_num):
                # 寻找已连接结点与未连接节点间权值最小的边
                if distance[i]<mincost and not visited[i]:
                    mincost=distance[i]
                    u=i
            if u==-1:
                break # 没有结点加入 退出循环
            visited[u]=True
            for i in range(vertex_num):
                # distance代表已连接结点与未连接结点之间边的最小权值 下一次使用这条边连接结点
                # 核心
                if adj_matrix[u][i]<distance[i] and not visited[i]:
                    distance[i]=adj_matrix[u][i] # 每次加入结点distance可能改变
        weight_sum=0
        for i in range(vertex_num):
            if distance[i]!=math.inf:
                weight_sum+=distance[i]
        return weight_sum

    # 结点begin单源最短路径
    def dijkstra(self,begin):
        vertex_num = self.vertex_num
        adj_matrix = self.adj_matrix
        visited = [False] * vertex_num
        distance = [math.inf] * vertex_num
        distance[begin] = 0
        while True:
            mincost=math.inf
            u=-1
            for i in range(vertex_num):
                if distance[i]<mincost and not visited[i]:
                    mincost=distance[i]
                    u=i
            if u==-1:
                break
            visited[u]=True # 通过visited判断是否加入所有结点
            for i in range(vertex_num):
                # distance代表通过已连接结点集向未连接结点延伸的最短路径长度
                # 每次加入新结点distance都有可能改变 因为已连接结点集合更新了
                if distance[u]+adj_matrix[u][i]<distance[i] and not visited[i]:
                    distance[i]=distance[u]+adj_matrix[u][i]
        for i in range(vertex_num):
            print(distance[i])

    # 最小堆优化
    def dijkstra_heap(self,begin):
        vertex_num = self.vertex_num
        adj_matrix = self.adj_matrix
        visited = [False] * vertex_num
        distance = [math.inf] * vertex_num
        distance[begin]=0
        heap = [(0,begin)]
        heapq.heapify(heap) # 根据distance建最小堆
        while len(heap)>=1:
            u=heapq.heappop(heap)[1] # 最小堆寻找最短路径
            if visited[u]: # 由于存在重复入堆的情况 对于已经访问过的结点直接跳过
                continue
            visited[u]=True # 连接结点
            for i in range(vertex_num):
                if adj_matrix[u][i]!=math.inf and not visited[i] and distance[u]+adj_matrix[u][i]<distance[i]:
                    distance[i]=distance[u]+adj_matrix[u][i]
                    heapq.heappush(heap,(distance[i],i)) # 导致重复入堆
        for i in range(vertex_num):
            print(distance[i])

    # 弗洛伊德 求所有结点间最短路径
    def floyd(self):
        vertex_num=self.vertex_num
        adj_matrix=self.adj_matrix
        distance=adj_matrix
        for k in range(vertex_num):
            for i in range(vertex_num):
                if distance[i][k]==math.inf:
                    continue
                for j in range(vertex_num):
                    if distance[k][j]==math.inf:
                        continue
                    if distance[i][j]>distance[i][k]+distance[k][j]:
                        distance[i][j] = distance[i][k] + distance[k][j]
        # for i in range(vertex_num):
        #     if distance[i][i]<0:
        #         print("NEGATIVE CYCLE")
        #         return
        # for i in range(vertex_num):
        #     for j in range(vertex_num):
        #         if distance[i][j]==math.inf:
        #             print("INF",end=" " if j!=vertex_num-1 else "")
        #         else: print(distance[i][j],end=" " if j!=vertex_num-1 else "")
        #     print()

    # 最小生成树 堆优化
    # 互质集合 self中edges会被清空
    def kruskal(self):
        edges = self.edges
        heapq.heapify(edges) # 建堆
        length = 0
        dset = DisjointSet.DisjointSet(self.vertex_num) # 创建所有结点的单独集合 互质集合
        edge_num = len(edges)
        for i in range(edge_num):
            edge = heapq.heappop(edges) # 堆弹出当前最小边
            w = edge[0]
            u = edge[1]
            v = edge[2]
            # 如果边的两个结点不在同一个集合内
            if not dset.same(u, v):
                # 则合并这两个结点集
                dset.unite(u, v)
                length += w
        return length

def main():
    vertex_num=io.read_int()
    edge_num=io.read_int()
    edges=[]
    for i in range(edge_num):
        u=io.read_int()
        v=io.read_int()
        w=io.read_int()
        edges.append((w,u,v))
    graph=Graph(vertex_num,None,edges,"edges")
    print(graph.kruskal())

if __name__== "__main__":
    main()