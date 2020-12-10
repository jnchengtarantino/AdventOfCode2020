from itertools import permutations
file = open("test.txt")
lines = file.readlines()
data = list(map(int,lines))

data.append(0)
data.sort()
# dif1=0
# dif2=0
# dif3=0
# data.append(data[-1] + 3)
# for i in range(1, len(data)):
#     if data[i] - data[i-1] == 1: dif1 += 1
#     elif data[i] - data[i-1] == 2: dif2 += 1
#     elif data[i] - data[i-1] == 3: dif3 += 1

temp = [1]+[0]*data[-1]
print(temp)
for i in data[1:]: 
    temp[i] = temp[i-3] + temp[i-2] + temp[i-1]
    print()
    print(temp)
print(str(temp[-1]))
# print(str(dif1) + " 1 jolt * " + str(dif3) + " 3 jolt = " + str(dif1*dif3))
   
file.close()