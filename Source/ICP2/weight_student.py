weight = []
weight_kg = []
b = 0.45359237
N = int(input("Enter total number of studemts: "))

for i in range(N): #if N is 10 then i will be in range(0,10)
    a = int(input("enter the weight: "))
    weight.append(a) #adds the output value of a to the array weight in each iteration
    weight_kg.append(weight[i-1]*b) #converts the values in weight array to kg and adds them to weight_kg array
    print(weight)
    print(weight_kg)

