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


        def II() -> int:
            return int(input())


        def MII():
            return map(int, input().split())


        def LI():
            return input().split()


        def LII() -> list[int]:
            return list(map(int, input().split()))


        # 读取单个字符串的字符列表
        def LCI():
            return  list(input())


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
        # 最小堆
        from heapq import merge, heapify, heappop, heappush, heappushpop, nlargest, nsmallest
        from queue import PriorityQueue
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
    fsum = lambda x, y: x + y
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
def kmp_search(s,pattern):
    n=len(s)
    m=len(pattern)
    # 求next数组
    # 表示当前字符如果不匹配时应当返回到第几个数
    nex=[0]*(m+1)
    # i指向当前扫描的字符
    # j指向可能匹配的前缀
    i,j=1,0
    while i<m:
        # 前缀中没有可匹配的串或者匹配成功时:
        if j==0 or pattern[i-1]==pattern[j-1]:
            i+=1
            j+=1
            if pattern[i-1]!=pattern[j-1]:
                nex[i]=j
            # 如果i与j的字符一样
            # 需要将nex[i]更新到j的上一个模式匹配串
            # 此时字符nex[i]与nex[j]指向字符一定不一样
            else:
                nex[i]=nex[j]
        else:
            # 因为j与nex[j]也一定有相同前缀匹配
            # 所以寻找j之前的模式匹配串 继续循环判断
            # 直到某个k与i代表字符相等或找不到前缀了
            j=nex[j]
    # 求子串
    i,j=1,1
    while i<=n and j<=m:
        # 当主串第i位与模式串第一位不等 主串向后移一位
        # 如果匹配则同时向后移
        # 此时nex[1]=0发挥了作用 因为0+1=1刚好使模式串重新从1开始计数
        if j==0 or s[i-1]==pattern[j-1]:
            i+=1
            j+=1
        else:
            j=nex[j]
    if j>=m:
        return i-m-1
    else:
        return -1
def solve():
    m,n=MII()
    matrix=[['0']*(n+1)]
    ans=0
    for _ in range(m):
        line=['0']+LCI()
        matrix.append(line)
    #print(matrix)
    layer_num=min(m,n)//2
    for i in range(layer_num):
        width=n-2*i
        height=m-2*i
        tlx=tly=1+i
        brx=n-i
        bry=m-i
        layer=matrix[tly][tlx:brx+1]
        for j in range(1,height-1):
            layer.append(matrix[tly+j][brx])
        layer+=matrix[bry][tlx:brx+1][::-1]
        for j in range(1,height-1):
            layer.append(matrix[bry-j][tlx])
        mode=['1','5','4','3']
        length=len(layer)
        layer+=layer[:3]
        for k in range(length):
            for w in range(4):
                if layer[k+w]!=mode[w]:
                    break
                elif w==3:
                    ans+=1
    print(ans)
t=II()
for _ in range(t):
    solve()