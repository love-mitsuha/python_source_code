# -*- coding: utf-8 -*-
import os
import time
import queue
import hashlib
import threading
import requests
from contextlib import closing

def download_file(url: str, path: str) -> None:
    with closing(requests.get(url, stream=True)) as r:
        r.raise_for_status()
        chunk_size = 10 * 1024
        total_bytes = int(r.headers.get('content-length', 0))
        if os.path.exists(path) and os.path.getsize(path) >= total_bytes:
            print(f"{path} 已下载，跳过")
            return

        print(f"{path} 开始下载")
        with open(path, "wb") as f:
            p = ProgressData(size=total_bytes, unit='Kb', block=chunk_size, file_name=path)
            for chunk in r.iter_content(chunk_size=chunk_size):
                if not chunk:
                    continue
                f.write(chunk)
                p.output()

class ProgressData:
    def __init__(self, size: int, unit: str, block: int, file_name: str = '') -> None:
        self.file_name = file_name
        # 统一换算为 Kb
        self.block = block / 1000.0
        self.size = size / 1000.0
        self.unit = unit
        self.count = 0
        self.start = time.time()

    def output(self) -> None:
        now = time.time()
        self.count += 1
        elapsed = now - self.start
        speed = self.block / elapsed if elapsed > 0 else 0
        self.start = now

        loaded = self.count * self.block
        progress = min(loaded / self.size, 1.0)

        if loaded >= self.size:
            print(f"{self.file_name} 下载完成\n")
        else:
            bar = '/' * int((1 - progress) * 50)
            print(
                f"{self.file_name} 下载进度 {loaded:.2f}{self.unit}/"
                f"{self.size:.2f}{self.unit} "
                f"{progress:.2%} 下载速度 {speed:.2f}{self.unit}/s"
            )
            print(f"{bar:>50}")

# 全局任务队列
task_queue = queue.Queue()

def run() -> None:
    while True:
        task = task_queue.get(timeout=100)
        if task is None:
            print("全下完啦")
            break
        download_file(*task)

def get_url() -> None:
    # TODO: 在此处将真正的 (url, path) 对加入 task_queue
    # 示例：
    # urls = ["http://example.com/video1.mp4", "http://example.com/video2.mp4"]
    # for u in urls:
    #     name = hashlib.md5(u.encode()).hexdigest()
    #     path = f"./downloads/{name}.mp4"
    #     task_queue.put((u, path))
    # 结束信号：假设启动了 4 个线程，就放 4 个 None
    for _ in range(4):
        task_queue.put(None)

if __name__ == "__main__":
    # 1. 填充下载任务
    get_url()

    # 2. 启动线程
    threads = []
    for _ in range(4):
        t = threading.Thread(target=run, daemon=True)
        t.start()
        threads.append(t)

    # 3. 等待所有线程结束
    for t in threads:
        t.join()
