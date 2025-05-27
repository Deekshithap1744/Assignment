with open("sample.txt", "w") as file:
    file.write("HI!\n")
with open("sample.txt", "a") as file:
    file.write("HELLO AGAIN!\n")

with open("sample.txt", "r") as file:    
    content = file.read()

print("File content from the beginning:")
print(content)