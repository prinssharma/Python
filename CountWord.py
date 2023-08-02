s = input("Enter any string : ")
count = 0
l = len(s)
for i in range(l):
    if s[i] == " ":
        count += 1
print(count+1)
print(s)