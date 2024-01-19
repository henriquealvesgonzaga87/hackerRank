# Www.HackerRank.com → wWW.hACKERrANK.COM
# Pythonist 2 → pYTHONIST 2
# 1º receber uma string
# 2º iterar sobre a string
# 3º verificar se a letra é maiscula ou minúscula
# 4º imprimir a iteração omitindo os espaços

def swap_case(s):
    string = ''
    for c in s:
        if c.islower():
            string += c.upper()
        elif c.isupper():
            string += c.lower()
        else:
            string += c
    return string


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
