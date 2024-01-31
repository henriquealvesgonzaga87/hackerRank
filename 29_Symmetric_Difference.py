#>> a = raw_input()
# 5 4 3 2
# >> lis = a.split()
# >> print (lis)
# ['5', '4', '3', '2']
# If the list values are all integer types, use the map() method to convert all the strings to integers.
#
# >> newlis = list(map(int, lis))
# >> print (newlis)
# [5, 4, 3, 2]

# Sample Input
#
# STDIN       Function
# -----       --------
# 4           set a size M = 4
# 2 4 5 9     a = {2, 4, 5, 9}
# 4           set b size N = 4
# 2 4 11 12   b = {2, 4, 11, 12}
# Sample Output
#
# 5
# 9
# 11
# 12

def difference_between_sets(input1, input2):
    lista_a = input1.split()
    nova_lista_a = list(map(int, lista_a))
    conjunto_a = set(nova_lista_a)
    lista_b = input2.split()
    nova_lista_b = list(map(int, lista_b))
    conjunto_b = set(nova_lista_b)
    resultado = [conjunto_a - conjunto_b, conjunto_b - conjunto_a]
    resultado_lista = []
    for i, v in enumerate(resultado):
        for j in v:
            resultado_lista.append(j)
    lista_ordenada = sorted(resultado_lista)
    return lista_ordenada


len_a = int(input())
a = input()
len_b = int(input())
b = input()
lista_resultado = difference_between_sets(a, b)
for c in lista_resultado:
    print(c)
