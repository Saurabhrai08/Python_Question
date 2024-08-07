num=5 


def factorial(n):
    fact =1

    for i in range (1, n+1):

        fact *= i

    return fact

factorial(num)

print("Factorial of 5 is",factorial(num))

    