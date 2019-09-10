a = open('E:\python\demo.txt','r')
b = a.readline() #readline method reads the text in a file line by line

while b:
    cnt = 1 #this makes the count value to start from 1 for each loop
    for c in b.split(): #split methos splits each line at the whitespaces
        print(c,":",cnt) #each string in the line is displayed with the count
        cnt += 1

    b = a.readline() #after for loop executes the line this sends the next line to for loop
a.close()
