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
class CacheGroup:
    def __init__(self,_num,c1,c2,strategy):
        self.num=_num
        self.cache1=Cache(c1,1,strategy)
        self.l1_hit=0
        self.cache2=Cache(c2,2,strategy)
        self.l2_hit=0
        self.replace_cnt=0

    def access(self, id_block):
        if self.cache1.access(id_block):
            fprint("HIT_L1")
            self.l1_hit+=1
        elif self.cache2.access(id_block):
            fprint("HIT_L2")
            self.l2_hit+=1
            id_subs = self.cache1.update(id_block)
            self.cache2.remove(id_block)
            # 将L1替换下的块移动至L2
            if id_subs!=-1:
                self.cache2.update(id_subs)
                self.replace_cnt+=1
        else:
            fprint("MISS")
            id_subs = self.cache1.update(id_block)
            if id_subs != -1:
                self.cache2.update(id_subs)
                self.replace_cnt+=1
        self.cache1.traverse()
        self.cache2.traverse()
    def mode_change(self,strategy):
        self.cache1.mode_change(strategy)
        self.cache2.mode_change(strategy)
    def resize(self,c1,c2):
        self.cache1.resize(c1)
        self.cache2.resize(c2)

class Cache:
    def __init__(self, _capacity, _level,_strategy):
        self.strategy=_strategy
        self.data= [0] * _capacity
        self.valid= [False] * _capacity
        self.cnt= [0] * _capacity
        self.capacity= _capacity
        self.level=_level
        self.que=deque()

    def access(self,id_block):
        flag=False # 标记是否找到
        if self.strategy=="LRU":
            for i in range(self.capacity):
                if self.data[i] == id_block and self.valid[i]:
                    self.cnt[i] = 0  # 重置访问时间
                    flag = True
                elif self.valid[i]:
                    self.cnt[i] += 1
        else:
            for index in self.que:
                if self.data[index]==id_block and self.valid[index]:
                    flag=True
                    break
        if flag:
            return True
        else:
            return False

    def update(self,id_block):
        if self.strategy=="LRU":
            temp = []
            for i in range(self.capacity):
                if not self.valid[i]:
                    self.data[i] = id_block
                    self.valid[i] = True
                    self.cnt[i] = 0
                    return -1
                else:
                    temp.append((-self.cnt[i], i))
            heapify(temp)
            _, index = heappop(temp)
            id_subs = self.data[index]
            self.data[index] = id_block
            self.valid[index] = True
            self.cnt[index] = 0
            return id_subs
        else:
            for i in range(self.capacity):
                if not self.valid[i]:
                    self.data[i] = id_block
                    self.valid[i] = True
                    self.cnt[i] = 0
                    self.que.append(i)
                    return -1
            index=self.que.popleft()
            id_subs = self.data[index]
            self.data[index] = id_block
            self.valid[index] = True
            self.que.append(index)
            return id_subs

    def traverse(self):
        if self.strategy=="LRU":
            temp = []
            for i in range(self.capacity):
                if self.valid[i]:
                    temp.append((-self.cnt[i], i))  # 最大堆 添负号
                    self.cnt[i] += 1
            heapify(temp)
            length = len(temp)
            fprint(f"L{self.level}:", end="")
            for i in range(length):
                _, index = heappop(temp)
                fprint(f" {self.data[index]}", end="")
            fprint()
        else:
            length=len(self.que)
            fprint(f"L{self.level}:", end="")
            for i in range(length):
                index=self.que.popleft()
                fprint(f" {self.data[index]}", end="")
                self.que.append(index)
            fprint()

    def remove(self,id_block):
        if self.strategy=="LRU":
            for i in range(self.capacity):
                if self.data[i] == id_block:
                    self.valid[i] = False
                    return
        else:
            length=len(self.que)
            for i in range(length):
                index=self.que.popleft()
                if self.data[index]!=id_block:
                    self.que.append(index)
                else:
                    self.valid[index]=False

    def mode_change(self,_strategy):
        self.strategy=_strategy
        if self.strategy=="FIFO":
            temp = []
            self.que.clear()
            for i in range(self.capacity):
                if self.valid[i]:
                    temp.append((-self.cnt[i],i))
            heapify(temp)
            length=len(temp)
            for i in range(length):
                _,index=heappop(temp)
                self.que.append(index)
        else:
            self.cnt=[0]*self.capacity
            length=len(self.que)
            for i in range(length):
                index=self.que.popleft()
                self.cnt[index]=length-i

    def resize(self,c):
        self.data=self.data+[0]*(c-self.capacity)
        self.valid=self.valid+[False]*(c-self.capacity)
        self.cnt=self.cnt+[0]*(c-self.capacity)
        self.capacity=c

def main():
    line=LI()
    c1=int(line[0])
    c2=int(line[1])
    strategy=line[2]
    q=II()
    caches=CacheGroup(2,c1,c2,strategy)
    access_cnt=0
    for _ in range(q):
        line=LI()
        if line[0]=="ACCESS":
            access_cnt+=1
            id_block=line[1]
            caches.access(id_block)
        elif line[0]=="SET_STRATEGY":
            caches.mode_change(line[1])
        else:
            c1,c2=int(line[1]),int(line[2])
            caches.resize(c1,c2)

    fprint(f"L1_HIT_RATE: {caches.l1_hit/access_cnt}")
    fprint(f"L2_HIT_RATE: {caches.l2_hit/access_cnt}")
    fprint(f"REPLACEMENTS: {caches.replace_cnt}")
if __name__=="__main__":
    main()
