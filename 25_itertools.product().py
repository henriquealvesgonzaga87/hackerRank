from itertools import product
# >>>
# >>> print list(product([1,2,3],repeat = 2))
# [(1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (3, 3)]
# >>>
# >>> print list(product([1,2,3],[3,4]))
# [(1, 3), (1, 4), (2, 3), (2, 4), (3, 3), (3, 4)]
# >>>
# >>> A = [[1,2,3],[3,4,5]]
# >>> print list(product(*A))
# [(1, 3), (1, 4), (1, 5), (2, 3), (2, 4), (2, 5), (3, 3), (3, 4), (3, 5)]
# >>>
# >>> B = [[1,2,3],[3,4,5],[7,8]]
# >>> print list(product(*B))
# [(1, 3, 7), (1, 3, 8), (1, 4, 7), (1, 4, 8), (1, 5, 7), (1, 5, 8), (2, 3, 7), (2, 3, 8), (2, 4, 7), (2, 4, 8),
# (2, 5, 7), (2, 5, 8), (3, 3, 7), (3, 3, 8), (3, 4, 7), (3, 4, 8), (3, 5, 7), (3, 5, 8)]
# Sample Input
#
#  1 2
#  3 4
# Sample Output
#
#  (1, 3) (1, 4) (2, 3) (2, 4)

resultado = []
x = input().split(' ')
y = input().split(' ')
a = []
b = []
for i in range(len(x)):
    if x[i].isdigit():
        a.append(int(x[i]))
for j in range(len(y)):
    if y[j].isdigit():
        b.append(int(y[j]))
resultado = list(product(a, b))
for i in resultado:
    print(i, end=' ')
