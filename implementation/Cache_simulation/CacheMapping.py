standard_input, packages, output_together = 1, 1, 0
dfs, hashing, read_from_file = 0, 0, 1
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

        import queue
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


    class FileIOManager:
        def __init__(self, meta_file="input.txt", output_file="output.txt"):
            self.input_stream = None
            self.output_stream = None
            self.input = None
            self.fprint = None

            try:
                # 从 meta_file 中读取实际输入文件名
                with open(meta_file, "r", encoding="utf-8") as meta:
                    file_name = meta.readline().strip().strip('"').strip("'")

                # 打开输入文件
                self.input_stream = open(file_name, "r", encoding="utf-8")
                self.input = lambda: self.input_stream.readline().strip()

                # 打开输出文件
                self.output_stream = open(output_file, "w", encoding="utf-8")
                self.fprint = lambda *args, **kwargs: print(*args, **kwargs, file=self.output_stream)

            except Exception as e:
                print(f"[FileIOManager] 文件初始化失败：{e}")
                exit(1)

        def close(self):
            if self.input_stream:
                self.input_stream.close()
            if self.output_stream:
                self.output_stream.close()


    if read_from_file:
        io = FileIOManager()
        input = io.input
        fprint = io.fprint

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

class Cache:
    def __init__(self,_size,_associativity):
        self.size=_size
        self.associativity=_associativity
        self.rows = self.size // self.associativity
        self.data= [[0]*self.associativity for _ in range(self.rows)]
        self.valid=[[False]*self.associativity for _ in range(self.rows)]
        self.cnt=[[0]*self.associativity for _ in range(self.rows)]
        self.replacements=0
    def access(self,id_block):
        flag=False
        row=id_block%self.rows
        for i in range(self.associativity):
            if self.data[row][i]==id_block and self.valid[row][i]:
                self.cnt[row][i]=0
                flag=True
            elif self.valid[row][i]:
                self.cnt[row][i]+=1
        if flag:
            return True
        else:
            self.update(id_block)
            return False
    def update(self,id_block):
        flag=False
        row = id_block % self.rows
        mx=-1
        index=-1
        for i in range(self.associativity):
            if not self.valid[row][i]:
                self.data[row][i]=id_block
                self.valid[row][i]=True
                self.cnt[row][i]=0
                flag=True
                break
        if not flag:
            for i in range(self.associativity):
                if mx<self.cnt[row][i]:
                    mx=self.cnt[row][i]
                    index=i
            self.data[row][index]=id_block
            self.valid[row][index]=True
            self.cnt[row][index]=0
            self.replacements+=1

def main():
    line=LI()
    cache=Cache(int(line[1]),int(line[2]))
    q=II()
    cnt=0
    for _ in range(q):
        line=LI()
        if cache.access(int(line[1])):
            fprint("HIT")
            cnt+=1
        else:
            fprint("MISS")
    fprint(f"HIT_RATE: {cnt/q}")
    fprint(f"REPLACEMENTS: {cache.replacements}")

if __name__=="__main__":
    main()