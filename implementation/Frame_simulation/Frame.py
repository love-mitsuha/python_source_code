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

        import queue
        import bisect
        import typing
        from collections import Counter, defaultdict, deque, OrderedDict
        from copy import deepcopy
        from functools import cmp_to_key, lru_cache, reduce
        # 最小堆
        from heapq import merge, heapify, heappop, heappush, heappushpop, nlargest, nsmallest
        from queue import PriorityQueue
        from itertools import accumulate, combinations, permutations, count, product
        from operator import add, iand, ior, itemgetter, mul, xor
        from string import ascii_lowercase, ascii_uppercase, ascii_letters
        from typing import *
        from algorithm import Bit

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
class Frame:
    def __init__(self):
        self.data=deque()
    def add(self,bit):
        if type(bit)==int:
            self.data.append(bit)
        else:
            self.data.extend(bit)
    def pop(self):
        return self.data.pop()
    def clear(self):
        self.data.clear()
    def __len__(self):
        return len(self.data)
    def __getitem__(self, item):
        return self.data[item]


class FrameSender:
    def __init__(self):
        self.crc_divisor=[1,1,0,1]
        self.length=len(self.crc_divisor)
        self.frame=Frame()
        self.data=[]
    def pack(self):
        self.frame.clear()
        self.frame.add([0,1,1,1,1,1,1,0])
        length=len(self.data)
        cnt=0
        for i in range(length):
            self.frame.add(self.data[i])
            if self.data[i]==1:
                cnt+=1
                if cnt==5:
                    self.frame.add(0)
                    cnt=0
            else:
                cnt=0
        self.frame.add([0,1,1,1,1,1,1,0])
    def crc(self,data):
        data=data+[0]*(self.length-1)
        dividend=data[:self.length]
        for i in range(self.length,len(data)):
            if dividend[0]==1:
                dividend=Bit.xor(dividend,self.crc_divisor)
            dividend.pop(0)
            dividend.append(data[i])
        # 最后一次
        if dividend[0]==1:
            dividend=Bit.xor(dividend,self.crc_divisor)
        return dividend[1:]
    def generate_crc(self,data):
        self.data=data+self.crc(data)
    def print(self):
        print(list(self.frame.data))
    def send(self):
        return self.frame

# 先定界 再去除零
# 功能分离
class FrameReceiver:
    def __init__(self):
        self.data=[]
        self.cnt=0 # 1 cnt
        self.state="search"
        self.buffer=[]
        self.shift_reg=0
        self.skip_next=False
        self.crc_divisor=[1,1,0,1]
        self.length=len(self.crc_divisor)
    def un_stuff(self):
        self.buffer=self.buffer[:-8]
        length = len(self.buffer)
        cnt=0
        ret=[]
        for i in range(length):
            if cnt==5:
                cnt=0
                continue
            ret.append(self.buffer[i])
            if self.buffer[i]==1:
                cnt+=1
            else:
                cnt=0
        return ret
    def unpack(self,frame):
        length=len(frame)
        self.shift_reg = 0
        self.cnt=0
        self.skip_next=False
        i=0
        flag=0x7e
        while i <length:
            bit=frame[i]
            self.shift_reg = ((self.shift_reg << 1) | bit) & 0xff
            if self.state=="search":
                if self.shift_reg==flag:
                    self.state="in frame"
                    self.buffer.clear()
            elif self.state=="in frame":
                # 帧尾
                if self.shift_reg==flag:
                    self.buffer.append(bit)
                    raw=self.un_stuff()
                    self.data.append(raw)
                    self.buffer.clear()
                    self.state="search"
                # 未去除零的数据
                else:
                    self.buffer.append(bit)
            i+=1

    def check_crc(self, received):
        return Bit.mod2_div(received,self.crc_divisor)

    def output(self):
        for i in range(len(self.data)):
            print(self.data[i])


def main():
    sender=FrameSender()
    receiver=FrameReceiver()
    data=[0,0,1,1,1,0,0,1]
    sender.generate_crc(data)
    print(sender.data)
    sender.pack()
    sender.print()
    receiver.unpack(sender.frame)
    print(sender.data)
    print(receiver.check_crc(sender.data))

    return
if __name__=="__main__":
    main()
