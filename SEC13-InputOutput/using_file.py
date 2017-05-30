#!/usr/bin/python
# Filename: using_file.py
"""
如何工作：
首先，我们通过指明我们希望打开的文件和模式来创建一个 file 类的实例。模
式可以为读模式（’r’）、写模式（’w’）或追加模式（’a’）。事实上还有多得多的模式
可以使用，你可以使用 help(file) 来了解它们的详情。默认情况下，open() 认为文件
是’t’ext 文件，且用’r’ead 模式打开。
在我们的例子中，我们首先用写模式打开文件，然后使用 file 类的 write 方法来
写文件，最后我们用 close 关闭这个文件。
接下来，我们再一次打开同一个文件来读文件。如果我们没有指定模式，读模式
会作为默认的模式。在一个循环中，我们使用 readline 方法读文件的每一行。这个方
法返回包括行末换行符的一个完整行。所以，当一个空的字符串被返回的时候，即表
示文件末已经到达了，于是我们停止循环。
默认情况下，print() 函数将文本和自动生成的新行打印到屏幕。我们指定 end=”
来制约新行的产生，因为从文件中读出的行已经用了换行符。最后，关闭文件。
现在，来看一下 poem.txt 文件的内容来验证程序读写的确都是正常的。

"""

poem = '''\
Programming is fun
When the work is done
if you wanna make your work also fun:
    use Python!
'''
f = open('poem.txt', 'w', encoding='utf-8')
f.write(poem)
f.close()

with open('poem.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    for line in lines:
        if len(line) == 0:
            break
        print(line, end='')
