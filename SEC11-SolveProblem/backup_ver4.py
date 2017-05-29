import time
import zipfile
import os

source = [r'.\tmp\SEC11_Problem.txt',
          r'.\tmp\Solution_1.txt',
          r'.\tmp\Solution_2.txt',
          r'.\tmp\Solution_3.txt'
          ]

target_dir = r'.\backup'

today = target_dir + os.sep + time.strftime('%Y%m%d')
now = time.strftime('%m%d_%H%M%S')
target = today + os.sep + now + '.zip'

if not os.path.exists(today):
    os.mkdir(today)  # make directory
    print('Successfully created directory', today)

if __name__ == '__main__':
    for i in range(0, len(source)):
        with zipfile.ZipFile(target, 'a') as my_zip:
            my_zip.write(source[i])

    print('Successful backup to', target)
