a = input("Please enter a string: ")
b = a.replace(a[2:4],'') #this replace the value at index 2 and 3 with null which is similar  to deleting them
c = a.replace(a[4],"") #deletes value at index 4
d = c.replace(c[2],"")
print(b[::-1]) #negative indexing start from the end of string so it displays the string in reverse order from start to end
print(d[::-1])
