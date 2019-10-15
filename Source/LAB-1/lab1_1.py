a = input("Please enter a string: ")
b = ""
for i in range(0,len(a)):
    if a[i] not in b:
        b = b + a[i]
print(b)

