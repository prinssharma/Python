n = int(input("Enter a number for the Fibonacci sequence: "))

a = 0
b = 1

if n >= 1:
    print("Fibonacci sequence: ")
    print(a,end=" ")

if n >= 2:
    print(b,end=" ")

for i in range(2, n):
    c = a + b
    print(c,end=" ")
    a = b
    b = c
