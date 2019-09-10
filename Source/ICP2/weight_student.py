weight = []
weight_kg = []
b = 0.45359237
N = int(input("Enter total number of studemts: "))

for i in range(N):
    a = int(input("enter the weight: "))
    weight.append(a)
    weight_kg.append(weight[i-1]*b)
    print(weight)
    print(weight_kg)

