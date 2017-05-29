#!/usr/bin/python
# Filename: backup_ver3.py

import os
import time

# 1. The files and directories to be backed up are specified in a list.
current_path = os.getcwd()
print(current_path)

# 要备份的文件或目录，可以是多个，存放在列表里
source = [f'{current_path}\\tmp', f'{current_path}\\Code']
print(f"source path is {' '.join(source)}")

# 备份到目标地址
target_dir = f'{current_path}\\backup'

# 以当天的日期创建文件夹
today = target_dir + os.sep + time.strftime('%Y%m%d')
# The current time is the name of the rar archive
now = time.strftime('%m%d_%H%M%S')
print(today, now)

# Take a comment from the user to create the name of the zip file
comment = input('Enter a comment --> ')
if len(comment) == 0: # check if a comment was entered
    target = today + os.sep + now + '.zip'
else:
    target = today + os.sep + now + '_'+comment.replace(' ', '_') + '.zip'

# Create the subdirectory if it isn't already there
if not os.path.exists(today):
    os.mkdir(today) # make directory
    print('Successfully created directory', today)
else:
    print(f'{today} directory already exists')

# 5. We use the zip command to put the files in a zip archive
rar_exe_path = r'"%ProgramFiles(X86)%\WinRAR\RAR.exe"'
rar_command = '"{}" a {} {} '.format(rar_exe_path, target, ' '.join(source))

# Run the backup
if os.system(rar_command) == 0:
    print('Successful backup to', target)
else:
    print('Backup FAILED')
