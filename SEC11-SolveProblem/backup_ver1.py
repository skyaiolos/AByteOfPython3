#!/usr/bin/python
# Filename: backup_ver1.py

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

# 3. The files are backed up into a zip file.
# 4. The name of the rar archive is the current date and time
target = target_dir + os.sep + time.strftime('%Y%m%d%H%M%S') + '.zip'

print(f'os.sep is :  {os.sep}')
print(target_dir)
print(target)
# 5. We use the rar command to put the files in a rar archive
# rar_exe_path = r'C:\Program Files (x86)\WinRAR\RAR.exe'
rar_exe_path = r'"%ProgramFiles(X86)%\WinRAR\RAR.exe"'

# cmd > RAR.exe A <target path> <source path>
# <Commands>
#   a             Add files to archive
rar_command = '"{}" a {} {} '.format(rar_exe_path, target, ' '.join(source))

# Run the backup
print(rar_command)
print()

if __name__ == '__main__':
    print("-----The backup process is start ------")
    if os.system(rar_command) == 0:
        print('Successful backup to', target)
    else:
        print('Backup FAILED')
