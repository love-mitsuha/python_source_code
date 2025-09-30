import queue
import math
# 无向无权图
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

    def __init__(self,adj_matrix):
        self.vertex_num=len(adj_matrix)
        self.adj_matrix=adj_matrix

    # 栈实现深搜
    def dfsTraverse_stack(self):
        visited = [False] * self.vertex_num
        for i in range(self.vertex_num):
            if not visited[i]:
                self.dfs_stack(i,visited)
    # 从起点begin开始访问
    def dfs_stack(self,begin,visited):
        vertex_num=self.vertex_num
        st=[begin]
        visited[begin]=True
        print(begin)
        while st:
            u=st[-1] # 查看栈顶元素
            v=-1
            for i in range(vertex_num):
                if self.adj_matrix[u][i] and not visited[i]: # 存在边v-i且结点i未被访问过
                    v=i
                    break
            if v!=-1:
                visited[v]=True
                print(v)
                st.append(v)
            else:
                st.pop()

    # 递归实现深搜
    def dfsTraverse(self):
        visited=[False]*self.vertex_num
        for i in range(self.vertex_num):
            if not visited[i]:
                self.dfs(i,visited)
    def dfs(self,begin,visited):
        visited[begin]=True
        print(begin)
        for i in range(self.vertex_num):
            if self.adj_matrix[begin][i] and not visited[i]:
                self.dfs(i,visited)

    # 队列实现广搜
    def bfsTraverse(self):
        visited = [False] * self.vertex_num
        for i in range(self.vertex_num):
            if not visited[i]:
                self.bfs(i,visited)
    def bfs(self,begin,visited):
        que=queue.Queue()
        d=[0]*self.vertex_num
        que.put(begin)
        visited[begin]=True
        d[begin]=depth=1
        while not que.empty():
            u=que.get()
            print(u)
            for i in range(self.vertex_num):
                if self.adj_matrix[u][i] and not visited[i]:
                    visited[i]=True
                    que.put(i)
                    d[i]=d[u]+1

    # 基于广搜 拓扑排序
    def topologicalSort(self):
        vertex_num=self.vertex_num
        adj_matrix=self.adj_matrix
        visited=[False]*vertex_num
        inDegree=[0]*vertex_num
        # 初始化结点入度
        for i in range(vertex_num):
            for j in range(vertex_num):
                if adj_matrix[i][j]:
                    inDegree[j]+=1
        begin=[]
        for i in range(vertex_num):
            if inDegree[i]==0:
                begin.append(i)
        self.bfs_topo(begin,visited,inDegree)
    def bfs_topo(self,begin,visited,inDegree):
        # 初始队列包含begin结点(顶点)
        que=begin
        while len(que)>=1:
            u=que.pop()
            visited[u]=True
            print(u) # 任务u入度为0 拓扑排序入列
            # 任务u做完后 由u指向的所有邻接点的入度都减一
            # 如果有邻接点的入度为零 则入队作下一轮的拓扑排序顶点 即(u)
            for v in range(self.vertex_num):
                if self.adj_matrix[u][v] and u!=v:
                    inDegree[v]-=1
                    if inDegree[v]==0 and not visited[v]:
                        que.append(v)

    # prev父结点 current当前结点
    # order深搜顺序 timer计时器
    # lowest 生成树中连接的最远的祖先结点
    # 生成深度搜索树
    def art_dfs(self,prev,current,visited,parent,order,lowest,timer):
        timer+=1 # 每次进入新结点计时器加1
        visited[current]=True
        order[current]=lowest[current]=timer # 记录
        for i in range(self.vertex_num):
            # 搜索所有邻边
            if self.adj_matrix[current][i]:
                child=i
                # 如果还未访问就递归访问
                if not visited[child]:
                    parent[child]=current
                    self.art_dfs(current,child,visited,parent,order,lowest,timer)
                    # 访问完成后要更新当前lowest 因为当前结点可通过子结点连接最远祖先 即存在回边
                    lowest[current]=min(lowest[current],lowest[child])
                # 如果是非父结点的祖先结点
                elif child!=prev:
                    # 则与祖先结点的order值进行比较
                    lowest[current]=min(lowest[current],order[child])
    # 关节点搜索
    def art_search(self):
        vertex_num=self.vertex_num
        visited=[False]*vertex_num
        parent=[0]*vertex_num
        order=[0]*vertex_num
        lowest=[0]*vertex_num
        ret=[]
        timer=0
        self.art_dfs(-1,0,visited,parent,order,lowest,timer)
        np=0
        for i in range(1,vertex_num):
            p=parent[i]
            if p==0:np+=1
            elif order[p]<=lowest[i]:
                ret.append(p)
        if np>1:print(0)
        for num in ret:
            print(num)