'''Task
The provided code stub reads and integer, , from STDIN. For all non-negative integers , print .

Example

The list of non-negative integers that are less than  is . Print the square of each number on a separate line.'''

if __name__ == '__main__':
    n = int(input())
    check_list = [i for i in range(0, n)]
    print(check_list)
    for v, i in enumerate(check_list):
        print(v**2)
