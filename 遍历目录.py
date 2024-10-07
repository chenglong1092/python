import os
import glob

directory = "C:/Users/10920/Desktop/测试同步"

# 获取目录中的所有内容
contents = os.listdir(directory)
# 遍历列表
# for item in contents:
#     item_path = os.path.join(directory, item)
#     if os.path.isfile(item_path):
#         print(f"文件：{item} ")
#     elif os.path.isdir(item_path):
#         print(f"目录:{item} ")


# for dirpath, dirnames, filenames in os.walk(directory):

#     for dirname in dirnames:
#         full_dir_path = os.path.join(dirpath, dirname)
#         print(full_dir_path)
#     for filename in filenames:
#         full_file_path = os.path.join(dirpath, filename)
#         print(full_file_path)


# 使用递归模式列出所有文件
files = glob.glob(directory + "/**/*", recursive=True)

for file in files:
    print(file)
    os.startfile(file)
