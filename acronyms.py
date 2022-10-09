
with open("acronyms.txt", "r") as f:
    paragraph = f.read()

dictionary = {}

for line in paragraph.split("\n"):
    text = line.split()
    a = ""
    for i in text:
        a = a+str(i[0]).upper()
    
    dictionary[a] = line

print(dictionary)