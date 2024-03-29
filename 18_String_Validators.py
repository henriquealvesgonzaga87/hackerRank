# Output Format
#
# In the first line, print True if  has any alphanumeric characters. Otherwise, print False.
# In the second line, print True if  has any alphabetical characters. Otherwise, print False.
# In the third line, print True if  has any digits. Otherwise, print False.
# In the fourth line, print True if  has any lowercase characters. Otherwise, print False.
# In the fifth line, print True if  has any uppercase characters. Otherwise, print False.
#
# Sample Input
#
# qA2
# Sample Output
#
# True
# True
# True
# True
# True
s = input().strip()
print(any(char.isalnum() for char in s))
print(any(char.isalpha() for char in s))
print(any(char.isdigit() for char in s))
print(any(char.islower() for char in s))
print(any(char.isupper() for char in s))

