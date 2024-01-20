import textwrap
# Sample Input 0
#
# ABCDEFGHIJKLIMNOQRSTUVWXYZ
# 4
# Sample Output 0
#
# ABCD
# EFGH
# IJKL
# IMNO
# QRST
# UVWX
# YZ


def wrap(string, max_width):
    texto = textwrap.wrap(string, max_width)
    return '\n'.join(texto)


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)

# string, max_width = input(), int(input())
# result = textwrap.wrap(string, max_width)
# for i in result:
#     print(i)
