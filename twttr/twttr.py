list = [
    "a", "e", "i", "o", "u"
]
text = input("Input: ").lower()

print("Output: ",end="")

for i in text:
    if i not in list:
        print(i, end="")