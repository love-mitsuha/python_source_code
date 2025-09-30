standard_input, packages, output_together = 1, 1, 0
dfs, hashing, read_from_file = 0, 0, 0
de = 1
if 1:
    if standard_input:
        import io, os, sys

        input = lambda: sys.stdin.readline().strip()

        import math

        inf = math.inf

        def I():
            return input()


        def II()->int:
            return int(input())


        def MII():
            return map(int, input().split())


        def LI():
            return input().split()


        def LII()->list[int]:
            return list(map(int, input().split()))


        def LFI():
            return list(map(float, input().split()))


        def GMI():
            return map(lambda x: int(x) - 1, input().split())

        def LGMI():
            return list(map(lambda x: int(x) - 1, input().split()))

    if packages:
        from io import BytesIO, IOBase

        import random
        import os

        import bisect
        import typing
        from collections import Counter, defaultdict, deque
        from copy import deepcopy
        from functools import cmp_to_key, lru_cache, reduce
        from heapq import merge, heapify, heappop, heappush, heappushpop, nlargest, nsmallest
        from itertools import accumulate, combinations, permutations, count, product
        from operator import add, iand, ior, itemgetter, mul, xor
        from string import ascii_lowercase, ascii_uppercase, ascii_letters
        from typing import *

        BUFSIZE = 4096

    if output_together:
        class FastIO(IOBase):
            newlines = 0

            def __init__(self, file):
                self._fd = file.fileno()
                self.buffer = BytesIO()
                self.writable = "x" in file.mode or "r" not in file.mode
                self.write = self.buffer.write if self.writable else None

            def read(self):
                while True:
                    b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
                    if not b:
                        break
                    ptr = self.buffer.tell()
                    self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
                self.newlines = 0
                return self.buffer.read()

            def readline(self):
                while self.newlines == 0:
                    b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
                    self.newlines = b.count(b"\n") + (not b)
                    ptr = self.buffer.tell()
                    self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
                self.newlines -= 1
                return self.buffer.readline()

            def flush(self):
                if self.writable:
                    os.write(self._fd, self.buffer.getvalue())
                    self.buffer.truncate(0), self.buffer.seek(0)


        class IOWrapper(IOBase):
            def __init__(self, file):
                self.buffer = FastIO(file)
                self.flush = self.buffer.flush
                self.writable = self.buffer.writable
                self.write = lambda s: self.buffer.write(s.encode("ascii"))
                self.read = lambda: self.buffer.read().decode("ascii")
                self.readline = lambda: self.buffer.readline().decode("ascii")


        sys.stdout = IOWrapper(sys.stdout)

    if dfs:
        from types import GeneratorType


        def bootstrap(f, stk=[]):
            def wrappedfunc(*args, **kwargs):
                if stk:
                    return f(*args, **kwargs)
                else:
                    to = f(*args, **kwargs)
                    while True:
                        if type(to) is GeneratorType:
                            stk.append(to)
                            to = next(to)
                        else:
                            stk.pop()
                            if not stk:
                                break
                            to = stk[-1].send(to)
                    return to

            return wrappedfunc

    if hashing:
        RANDOM = random.getrandbits(20)


        class Wrapper(int):
            def __init__(self, x):
                int.__init__(x)

            def __hash__(self):
                return super(Wrapper, self).__hash__() ^ RANDOM

    if read_from_file:
        file = open("input.txt", "r").readline().strip()[1:-1]
        fin = open(file, 'r')
        input = lambda: fin.readline().strip()
        output_file = open("output.txt", "w")


        def fprint(*args, **kwargs):
            print(*args, **kwargs, file=output_file)

    if de:
        def debug(*args, **kwargs):
            print('\033[92m', end='')
            print(*args, **kwargs)
            print('\033[0m', end='')

    fmax = lambda x, y: x if x > y else y
    fmin = lambda x, y: x if x < y else y
    mod = 998244353


    class lst_lst:
        def __init__(self, n) -> None:
            self.n = n
            self.pre = []
            self.cur = []
            self.notest = [-1] * (n + 1)

        def append(self, i, j):
            self.pre.append(self.notest[i])
            self.notest[i] = len(self.cur)
            self.cur.append(j)

        def iterate(self, i):
            tmp = self.notest[i]
            while tmp != -1:
                yield self.cur[tmp]
                tmp = self.pre[tmp]

# 线段树 快速进行区间操作 logN
# 下标为1 1--N
class TreeNode:
    def __init__(self,val=0):
        self.left=-1
        self.right=-1
        self.val=val
        self.length=0 # 当前区间覆盖长度
        self.lazy_tag=None # 将区间更新操作延迟到后续查询时再更新
class SegmentTree:
    # function为指定方法 用于具体更新聚合区间值
    def __init__(self,nums,function):
        self.size=len(nums)
        self.tree=[TreeNode()for _ in range(self.size*4+4)]
        self.nums=nums
        self.function=function
        if self.size>0:
            self.__build(1,1,self.size)

    def __build(self,index,left,right):
        self.tree[index].left=left
        self.tree[index].right=right
        self.tree[index].length=right-left+1
        # 到达叶结点
        if left==right:
            self.tree[index].val=self.nums[left-1]
            return
        mid=(left+right)//2
        left_index=index*2
        right_index=index*2+1
        # 分别建立左右子树后更新当前节点值
        self.__build(left_index,left,mid)
        self.__build(right_index,mid+1,right)
        self.__pushup(index)
    # 向上更新结点值
    # 用左右子区间值更新当前大区间值
    def __pushup(self,index):
        left_index=index*2
        right_index=index*2+1
        self.tree[index].val=self.function(self.tree[left_index].val,self.tree[right_index].val)
    # 更新单个叶结点
    def update_point(self,i,val):
        self.nums[i-1]=val
        self.__update_point(i,val,1,1,self.size)
    def __update_point(self,i,val,index,left,right):
        if self.tree[index].left==self.tree[index].right:
            self.tree[index].val=val
            return
        mid=(left+right)//2
        if i<=mid:
            left_index=index*2
            self.__update_point(i,val,left_index,left,mid)
        else:
            right_index=index*2+1
            self.__update_point(i,val,right_index,mid+1,right)
        self.__pushup(index)
    # 递归查询区间值
    def query_interval(self,q_left,q_right):
        return self.__query_interval(q_left,q_right,1,1,self.size)
    def __query_interval(self,q_left,q_right,index,left,right):
        if left>=q_left and right<=q_right:
            return self.tree[index].val
        if right<q_left or left>q_right:
            return 0

        # pushdown向下更新懒标记保持数据正确性
        self.__pushdown(index)

        mid=(left+right)//2
        left_index=index*2
        right_index=index*2+1
        res_left=res_right=0
        if q_left<=mid:
            res_left=self.__query_interval(q_left,q_right,left_index,left,mid)
        if q_right>=mid+1:
            res_right=self.__query_interval(q_left,q_right,right_index,mid+1,right)
        return self.function(res_left,res_right)


    def update_interval(self,q_left,q_right,val):
        self.__update_interval(q_left,q_right,val,1,1,self.size)
    # 分别为 查询区间左端点 查询区间右端点 更新值 结点索引 当前结点左端点 当前结点右端点
    def __update_interval(self,q_left,q_right,val,index,left,right):
        # 要更新区间完全包含当前结点范围 懒标记
        if left>=q_left and right<=q_right:
            self.tree[index].val=val*self.tree[index].length
            self.tree[index].lazy_tag=val
            return
        if right<q_left or left>q_right:
            return
        # 如果不完全包含则要向下传播懒标记
        # 并且要先更新懒标记以保证下方结点值正确
        self.__pushdown(index)
        mid=(left+right)//2
        left_index=index*2
        right_index=index*2+1
        if q_left<=mid:
            self.__update_interval(q_left,q_right,val,left_index,left,mid)
        if q_right>=mid+1:
            self.__update_interval(q_left,q_right,val,right_index,mid+1,right)
        # 更新当前结点值
        self.__pushup(index)

    # 向下更新左右结点val与懒标记
    def __pushdown(self,index):
        lazy_tag=self.tree[index].lazy_tag
        # 没有懒标记则返回
        if lazy_tag is None:
            return
        # 有懒标记则向下更新左右结点
        left_index=index*2
        right_index=index*2+1

        self.tree[left_index].lazy_tag=lazy_tag
        self.tree[left_index].val=lazy_tag*self.tree[left_index].length

        self.tree[right_index].lazy_tag=lazy_tag
        self.tree[right_index].val=lazy_tag*self.tree[right_index].length

        self.tree[index].lazy_tag=None # 消除懒标记

n,m=MII()
num=LII()
tree=SegmentTree(num,lambda a,b:a+b)
for _ in range(m):
    l,r=MII()
    e=tree.query_interval(l,r)
    avg=e*pow(r-l+1,mod-2,mod)%mod # avg=e/(r-l+1)
    tree.update_interval(l,r,avg)
for k in range(1,n+1):
    print(tree.query_interval(k,k),end=" ")