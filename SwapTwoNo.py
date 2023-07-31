def swap_twoNo(x, y):
    
# without using 3rd variable
    x = x+y
    y=x-y
    x=x-y

# using third variable
    # z = x
    # x = y
    # y = z

    return x, y



a = int(input("Enter 1st number : "))
b = int(input("Enter 2nd number : "))

a, b = swap_twoNo(a, b)
print ("After swapping a=", a," and b=" , b )
