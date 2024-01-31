#Sample Input

# STDIN                                       Function
# -----                                       --------
# 10                                          arr[] size N = 10
# 161 182 161 154 176 170 167 171 170 174     arr = [161, 181, ..., 174]
# Sample Output
#
# 169.375


def average(array):
    conjunto = set(array)
    media_conjunto = sum(conjunto) / len(conjunto)
    return media_conjunto


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
