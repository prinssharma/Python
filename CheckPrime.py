import math

def is_prime(n):
    if n<=1:
        return False
    else:
        for i in range (2,int(math.sqrt(n))+1):
            if n % i == 0:
                return False
    return True

a = int(input("Enter a number : "))

if is_prime(a):
    print(a, "is a prime number")
else:
    print(a,"is not a prime number")