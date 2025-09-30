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
t=II()
for _ in range(t):
    n=II()
    x=[]
    y=[]
    x_inv=[]
    y_inv=[]
    points=[]
    cost_min=1e20
    for i in range(n):
        a,b=MII()
        x.append(a)
        y.append(b)
        x_inv.append(-a)
        y_inv.append(-b)
        points.append((a,b))
    if n==1:
        print(1)
        continue
    heapify(x)
    heapify(y)
    heapify(x_inv)
    heapify(y_inv)
    x_min=heappop(x)
    y_min=heappop(y)
    x_max=-heappop(x_inv)
    y_max=-heappop(y_inv)
    for i in range(n):
        a,b=points[i][0],points[i][1]
        width,height=0,0
        if a==x_max:
            width=-x_inv[0]-x_min+1
        elif a==x_min:
            width=x_max-x[0]+1
        else:
            width=x_max-x_min+1
        if b==y_max:
            height=-y_inv[0]-y_min+1
        elif b==y_min:
            height=y_max-y[0]+1
        else:
            height=y_max-y_min+1
        sq=width*height
        if n<=sq:
            cost_min=min(cost_min,sq)
        else:
            cost_min=min(cost_min,sq+min(width,height))
    print(cost_min)
