true_words = ["42", "forty two", "forty-two"]

user = input("Enter text: ")

if user in true_words:
    print("Yes")

else:
    print("No")