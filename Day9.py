file = open("day9input.txt")
lines = file.readlines()
data = list(map(int,lines))

mem = []
found = False

# for datum in data:
#     if len(mem) < 25 :
#         mem.append(datum)
#     else:
#         found = False
#         for num in mem:
#             for i in range(len(mem)):
#                 if (num + mem[i] == datum) and (num != mem[i]):
#                     # print("popping " + str(mem.pop(0)) )
#                     mem.append(datum)
#                     # print("appending " + str(datum))
#                     # print(str(mem))
#                     # print()
#                     found = True
#                     break
            
#             if found: break                    
#         if not found:
#             print("non fit found " + str(datum)+ " mem " + str(mem))
#             break
                    
for i in range(len(data)):
    for j in range(i+1,len(data)):
        if sum(data[i:j]) == 375054920:
            found = True
            temp = data[i:j]
            temp.sort()
            print(temp[0] + temp[-1])
    if found: break

   
file.close()