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
class PageDirectory:
    def __init__(self,frames_num,page_size,pd_unit_num,pt_unit_num,strategy):
        self.directory={}
        self.frames_num=frames_num
        self.page_size=page_size
        self.pd_unit_num=pd_unit_num
        self.pt_unit_num=pt_unit_num
        self.strategy=strategy
        # 空闲队列 由页目录管理
        self.free_frames=deque(range(frames_num))
        self.replacer = OrderedDict()
        self.replace=0
    def access(self,vpn):
        page_dir_idx=vpn//self.pt_unit_num
        if page_dir_idx>self.pd_unit_num:
            fprint("invalid address(too big)")
            return False
        # 如果目录中访问过页表 再进一步访问页表
        if page_dir_idx in self.directory:
            # 如果命中
            if self.directory[page_dir_idx].access(vpn):
                if self.strategy=="LRU":
                    self.replacer.move_to_end(vpn)
                return True
            else:
                return False
        else:
            # 如果还没有访问过说明肯定没有数据
            # 同时要新建页表
            self.directory.setdefault(page_dir_idx,PageTable(self.page_size,self.pt_unit_num,self.strategy))
            return False
    def update(self,vpn):
        page_dir_idx=vpn//self.pt_unit_num
        page_table_idx=vpn%self.pt_unit_num
        # 如果有空闲块
        if self.free_frames:
            frame_id=self.free_frames.popleft()
        else:
            # 替换出物理块
            victim_vpn,_=self.replacer.popitem(last=False)
            victim_page_dir_idx = victim_vpn // self.pt_unit_num
            victim_page_table_idx = victim_vpn % self.pt_unit_num
            frame_id=self.directory[victim_page_dir_idx].remove(victim_page_table_idx)
            self.replace+=1
        self.directory[page_dir_idx].update(page_table_idx,frame_id)
        # 加入替换结构
        self.replacer[vpn]=None
    def get(self,vpn):
        page_dir_idx = vpn // self.pt_unit_num
        page_table_idx = vpn % self.pt_unit_num
        return self.directory[page_dir_idx].get(page_table_idx)
# 页表项
class PageField:
    def __init__(self):
        self.present=False # 存在位
        self.frame_id=None # 分配的物理块号
        self.cnt=0 # LRU

class PageTable:
    def __init__(self, page_size, pt_unit_num, strategy):
        self.page_size=page_size
        self.pt_unit_num=pt_unit_num
        self.page_table={}
        self.strategy=strategy
    def access(self,vpn):
        page_table_idx=vpn%self.pt_unit_num
        if page_table_idx>=self.pt_unit_num:
            fprint("invalid address")
            return False
        # 命中
        if page_table_idx in self.page_table and self.page_table[page_table_idx].present:
            return True
        # 不命中
        else:
            return False
    # 更新操作 为虚拟页赋新的物理块
    def update(self,page_table_idx,frame_id):
        page_field=self.page_table.setdefault(page_table_idx,PageField())
        page_field.present=True
        page_field.frame_id=frame_id
    # 撤销操作 返回物理块号
    def remove(self,page_table_idx):
        page_field=self.page_table.get(page_table_idx)
        frame_id=page_field.frame_id
        page_field.frame_id=None
        page_field.present=False
        return frame_id
    # 获得物理块号
    def get(self,page_table_idx):
        return self.page_table[page_table_idx].frame_id

class TLB:
    def __init__(self,tlb_unit_num,strategy):
        self.tlb_unit_num=tlb_unit_num
        self.strategy=strategy
        self.replacer=OrderedDict()
        self.tlb={}
        self.replace=0
    def access(self,vpn):
        # 如果命中
        if vpn in self.tlb:
            if self.strategy=="LRU":
                self.replacer.move_to_end(vpn)
            return True
        else:
            return False
    # 获取物理块号
    def get(self,vpn):
        return self.tlb[vpn]
    def update(self,vpn,frame_id):
        # 如果没有空闲
        if len(self.tlb)==self.tlb_unit_num:
            victim_vpn,_=self.replacer.popitem(last=False)
            self.tlb.pop(victim_vpn)
            self.replace+=1
        self.tlb.setdefault(vpn,frame_id)
        self.replacer[vpn]=None

class PageSystem:
    def __init__(self,frames_num,page_size,pd_unit_num,pt_unit_num,tlb_unit_num,tlb_strategy,page_strategy):
        self.page_size=page_size
        self.page_directory=PageDirectory(frames_num,page_size,pd_unit_num,pt_unit_num,page_strategy)
        self.tlb=TLB(tlb_unit_num,tlb_strategy)
        # 统计
        self.access_cnt=0
        self.tlb_hit=0
        self.page_hit=0
        self.page_miss=0
    def access(self,address):
        vpn=address//self.page_size
        self.access_cnt+=1
        # tlb命中
        if self.tlb.access(vpn):
            self.tlb_hit+=1
            self.page_hit+=1
            fprint("TLB HIT",end=" ")
            fprint(f"{self.tlb.get(vpn)}")
        # tlb未命中但页表命中
        elif self.page_directory.access(vpn):
            self.page_hit+=1
            frame_id=self.page_directory.get(vpn)
            self.tlb.update(vpn,frame_id)
            fprint("TLB_MISS_PAGE_HIT",end=" ")
            fprint(f"{self.page_directory.get(vpn)}")
        # 都没有命中
        else:
            #TODO 从页表找到物理块号
            self.page_miss+=1
            self.page_directory.update(vpn)
            frame_id=self.page_directory.get(vpn)
            self.tlb.update(vpn,frame_id)
            fprint("TLB_MISS_PAGE_FAULT",end=" ")
            fprint(f"{frame_id}")

def main():
    line=LI()
    page_size=int(line[0])
    tlb_unit_num=int(line[1])
    tlb_strategy=line[2]
    pd_unit_num,pt_unit_num=MII()
    line=LI()
    frames_num=int(line[0])
    page_strategy=line[1]
    page_system=PageSystem(frames_num,page_size,pd_unit_num,pt_unit_num,tlb_unit_num,tlb_strategy,page_strategy)
    q=II()
    for _ in range(q):
        line=LI()
        page_system.access(int(line[1]))
    fprint(f"TLB_HIT_RATE {page_system.tlb_hit/page_system.access_cnt}")
    fprint(f"PAGE_HIT_RATE {page_system.page_hit/page_system.access_cnt}")
    fprint(f"PAGE_FAULTS {page_system.page_miss}")
    fprint(f"PAGE_REPLACEMENTS {page_system.page_directory.replace}")
    fprint(f"TLB_REPLACEMENTS {page_system.tlb.replace}")

if __name__=="__main__":
    main()
