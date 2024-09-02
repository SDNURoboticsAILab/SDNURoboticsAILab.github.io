# -*- coding: utf-8 -*-

import os

# 要插入的内容
insert_content = """---
comments: true
---

"""

# 获取当前目录
current_directory = os.getcwd()

# 遍历当前目录下的所有文件
for filename in os.listdir(current_directory):
    if filename.endswith('.md'):
        file_path = os.path.join(current_directory, filename)

        try:
            # 读取文件内容
            with open(file_path, 'r', encoding='utf-8') as file:
                existing_content = file.read()

            # 插入新内容
            new_content = insert_content + existing_content

            # 写回文件
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(new_content)

            print(f"文件 {filename} 已更新。")
        except UnicodeDecodeError:
            print(f"文件 {filename} 包含非 UTF-8 编码的字符，跳过处理。")

print("所有可处理的 .md 文件已更新。")