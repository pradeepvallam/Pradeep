tup = [('John', ('Physics', 80)), ('Daniel', ('Science', 90)), ('John', ('Science', 95)), ('Mark',('Maths', 100)), ('Daniel', ('History', 75)), ('Mark', ('Social', 95))]
out = {}

for i in range(0,len(tup)):
    temp = [tup[i]]
    for s,(subject,marks) in temp:
        if s not in out:
            out[s] = [(subject,marks)]
        else:
            out[s].append((subject,marks))
print(out)




