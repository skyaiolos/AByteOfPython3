#!/usr/bin/python
# user_input.py
"""
我们使用了切片特性来将文本逆转。我们已经知道了如何使用 seq[a:b] 代码从位
置 a 到位置 b 来形成切片。我们可以给其提供第三个参数，这个参数决定了切片的步
长。默认步长是 1，因为要返回文本的连续部分。给一个负的步长，如 -1 会将文本逆
转。
"""
import string


def get_reverse(text):
    return text[::-1]


def is_palindrome(text):
    text = text.lower()
    text = text.replace(' ', '')
    for char in string.punctuation:
        text = text.replace(char, '')
    print(get_reverse((text)))
    return text == get_reverse(text)


def main():
    something = input('Enter text:')
    if (is_palindrome(something)):
        print("Yes, {0} is a palindrome".format(something))
    else:
        print("No,{0} is not a palindrome".format(something))


if __name__ == '__main__':
    reverse_str = get_reverse('skyaiolos')
    print(reverse_str)

    main()
else:
    print("user_input.py was imported!")
