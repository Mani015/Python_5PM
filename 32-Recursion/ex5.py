
# Factorial using Recursion:

def Factorial(n):
    if n==3:
        return 1
    else:
        return n * Factorial(n-1)
n = int(input('Enter one number:'))
print(Factorial(n))