user_file = input("File name: ").lower().strip()

if user_file.endswith(".gif"):
    print("image/gif")

elif user_file.endswith(".jpg") or user_file.endswith(".jpeg"):
    print("image/jpeg")

elif user_file.endswith(",txt"):
    print("text/plane")

elif user_file.endswith(".zip"):
    print("application/zip")

elif user_file.endswith(".pdf"):
    print("application/pdf")
    
elif user_file.endswith(".png"):
    print("image/png")

else:
    print("application/octet-stream")