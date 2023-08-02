s = input("Enter a String : ")

revString = ""
l = len(s)
for i in range(l-1,-1,-1):
    print(revString + s[i], end="")
    
