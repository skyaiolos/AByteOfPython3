"""
#  Script Description:
    5.11.2. 从 ZIP 文件中读取数据
    调用 read 方法就可以从 ZIP 文档中读取数据. 它接受一个文件名作为参数,
    返回字符串. 如 Example 5-21 所示.

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