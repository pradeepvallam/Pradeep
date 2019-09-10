a = input("please enter a sentence: ")
c = int(len(a))
def string_alternative():  #creats function string_alternative
    print(a[0:c:2]) #displays the sentence through indexing where values at alternate indexes are not displayed
string_alternative() #calling the function from main

