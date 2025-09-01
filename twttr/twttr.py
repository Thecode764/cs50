list = [
    "a", "e", "i", "o", "u"
]
text = input("Input: ")

print("Output: ",end="")

for i in text:
    if i.casefold() not in list:
        print(i, end="")