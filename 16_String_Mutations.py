# STDIN           Function
# -----           --------
# abracadabra     s = 'abracadabra'
# 5 k             position = 5, character = 'k'
# abrackdabra

def mutate_string(string, position, character):
        l = []
        for i in string:
            l.append(i)
        l[position] = character
        string = ''.join(l)
        return string


if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
