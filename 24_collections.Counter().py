# Sample Input
#
# 10
# 2 3 4 5 6 8 7 6 5 18
# 6
# 6 55
# 6 45
# 6 55
# 4 40
# 18 60
# 10 50
# Sample Output
#
# 200
# Explanation
#
# Customer 1: Purchased size 6 shoe for $55.
# Customer 2: Purchased size 6 shoe for $45.
# Customer 3: Size 6 no longer available, so no purchase.
# Customer 4: Purchased size 4 shoe for $40.
# Customer 5: Purchased size 18 shoe for $60.
# Customer 6: Size 10 not available, so no purchase.

from collections import Counter
qtde_sapatos = int(input())
lista_tamanhos = input().split(' ')
qtde_clientes = int(input())
qtde_por_tamanho = Counter(lista_tamanhos)
saldo = 0
# tamanho / valor
for cliente in range(qtde_clientes):
    s = input().split(' ')
    tamanho = s[0]
    valor = int(s[1])
    if qtde_por_tamanho[tamanho] <= 0:
        qtde_por_tamanho[tamanho] += 0
        saldo += 0
    else:
        qtde_por_tamanho[tamanho] -= 1
        saldo += valor

print(saldo)
