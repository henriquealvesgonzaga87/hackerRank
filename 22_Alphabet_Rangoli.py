def print_rangoli(size):
    # Cria uma lista com as letras do alfabeto
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    # Cria a metade superior do padrão
    lines = []
    for i in range(size):
        s = '-'.join(alphabet[size - 1:i:-1] + alphabet[i:size])
        line = (s.center(size * 4 - 3, '-'))
        lines.append(line)

    # Combina a metade superior e inferior para formar o padrão completo
    result = '\n'.join(lines[::-1] + lines[1:])

    print(result)


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
