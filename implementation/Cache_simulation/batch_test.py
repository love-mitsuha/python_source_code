import os
import subprocess

# 所有测试数据文件名（放在同一目录下）
test_cases = [
    "data.txt",
    "data2.txt",
    "data3.txt",
    "data4.txt",
    "data5.txt"
]

# 主程序文件名
program_file = "CacheMapping.py"

# 输入文件入口（程序读取它来获取数据文件名）
meta_file = "input.txt"

# 输出文件（程序写入结果）
output_file = "output.txt"

# 输出结果保存目录
result_dir = "results"
os.makedirs(result_dir, exist_ok=True)

for case in test_cases:
    print(f"🔍 正在测试：{case}")

    # 写入 input.txt，指定当前测试数据文件
    with open(meta_file, "w", encoding="utf-8") as f:
        f.write(f"{case}\n")

    # 运行程序
    subprocess.run(["python", program_file])

    # 保存输出结果
    result_path = os.path.join(result_dir, f"{case}_output.txt")
    os.replace(output_file, result_path)

    print(f"✅ 输出已保存至：{result_path}\n")
