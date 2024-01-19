if __name__ == '__main__':
    my_list = []
    count = 0
    N = int(input())
    for i in range(0, N):
        command = input().split(" ")
        if command[0] == "insert":
            my_list.insert(int(command[1]), int(command[2]))
        if command[0] == "print":
            print(my_list)
        if command[0] == "remove":
            my_list.remove(int(command[1]))
        if command[0] == "append":
            my_list.append(int(command[1]))
        if command[0] == "sort":
            my_list = sorted(my_list)
        if command[0] == "pop":
            my_list.pop()
        if command[0] == "reverse":
            my_list = my_list[::-1]
