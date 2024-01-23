# This tool returns the phase of complex number  (also known as the argument of ).
# >>> phase(complex(-1.0, 0.0))
# 3.1415926535897931
# # This tool returns the modulus (absolute value) of complex number .
# >>> abs(complex(-1.0, 0.0))
# 1.0
# Sample Input
#   1+2j
# Sample Output
#  2.23606797749979
#  1.1071487177940904
from cmath import phase

print(complex(phase(1+2j)))
