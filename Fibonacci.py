def is_fibonacci(A):
    if A==0:
        return 0
    if A==1:
        return 1
    else:
        return is_fibonacci(A-1)+is_fibonacci(A-2)
A=int(input())
print(is_fibonacci(A))

"""
Input 1:
A = 2

Input 2:
A = 9


Output 1:
1

Output 2:
34
"""

