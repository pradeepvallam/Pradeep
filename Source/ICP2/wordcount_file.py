a = open('E:\python\demo.txt','r')
b = a.readline()

while b:
    cnt =1
    for c in b.split():
        print(c,":",cnt)
        cnt += 1

    b = a.readline()
a.close()
