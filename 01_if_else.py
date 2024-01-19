'''Task
Given an integer, , perform the following conditional actions:

If  is odd, print Weird
If  is even and in the inclusive range of  to , print Not Weird
If  is even and in the inclusive range of  to , print Weird
If  is even and greater than , print Not Weird
Input Format

A single line containing a positive integer, .'''

if __name__ == '__main__':
    n = int(input().strip())
    if n % 2 != 0:
        print("Weird")
    else:
        if n % 2 == 0 and n in range(2, 6):
            print("Not Weird")
        if n % 2 == 0 and n in range(6, 21):
            print("Weird")
        if n % 2 == 0 and n > 20:
            print("Not Weird")
