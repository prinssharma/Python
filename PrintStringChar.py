s = input("Enter a string : ")

for i in s:
    print(i, end=" ")
print("Total character in string : ",len(s))


print("-----------------------")


l = len(s)
for i in range(l):
    print(s[i])