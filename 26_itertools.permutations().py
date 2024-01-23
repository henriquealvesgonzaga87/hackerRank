from itertools import permutations

texto = input().split(' ')
a = texto[0]
b = int(texto[1])

resultado = sorted(permutations(a, b))
for perm in resultado:
    print(''.join(perm))
