"""
#  Script Description:
    5.11.1. 列出内容
    使用 namelist 和 infolist 方法可以列出压缩档的内容, 前者返回由文件名
    组成的列表, 后者返回由  ZipInfo 实例组成的列表. 如 Example 5-20 所示.

"""
__author__ = "爱的彼岸(QQ:3124724)"
__copyright__ = "Copyright 2017,3124724@qq.com"

# Create by Jianguo on 2017/5/29
# File name ->

import zipfile
import os

current_path = os.getcwd()
zip_path = f'{current_path}\\backup\\Demo_zip.zip'
print(zip_path)
file = zipfile.ZipFile(zip_path, 'r')

# list filenames in zip
for name in file.namelist():
    print(name)

print()

# list file information
for info in file.infolist():
    print(f'文件名称是：{info.filename},文件大小是：{info.file_size}')
