import re
file = open("day14input.txt")
lines = file.readlines()
# data = list(map(int,lines))
 # part 1
# mem = {}
# for line in lines:
#     if "mask" in line:
#         andMask = 2**36 -1
#         orMask = 0  
#         temp = line.split(" ")[2].strip()
#         print(temp)
#         for i in range(len(temp)):
#             if temp[i] == "1":
#                 orMask += 2**(35 - i)
#             elif temp[i] == "0":
#                 andMask -= 2**(35 - i)
#         print("Setting orMask " +str(orMask) +" "+ bin(orMask))
#         print("Setting andMask " +str(andMask) + " " + bin(andMask))
#     else:
#         address = line.split(" ")[0].strip()[4:-1]
#         val = int(line.split(" ")[2].strip())
#         print("Address " + str(address) + " og val " + str(val))
#         newVal = (val | orMask) & andMask
#         print("New val = " + str(newVal))
#         mem[address] = newVal

#part 2
mem = {}
mask = [0] * 32
for line in lines:
    if "mask" in line:
        mask = list(line.split(" ")[2].strip())
        print("Setting mask " + line.split(" ")[2].strip())
    else:
        address = int(line.split(" ")[0].strip()[4:-1])
        val = int(line.split(" ")[2].strip())
        print("og Address " + str(address) + " val " + str(val))
        print(bin(address))
        addL = list(map(int, bin(address)[2:]))
        #pad AddL
        while len(addL) < 36:
            addL.insert(0,0)
        addresses = [0]
        for i in range(len(mask)):
            if mask[i] == "0":
                addresses = [ a + ((2**(35 - i)) * addL[i]) for a in addresses]
            elif mask[i] == "1":
                addresses = [ a + ((2**(35 - i))) for a in addresses]
            elif mask[i] == "X":
                buffer = []
                for a in addresses:
                    newAddress = a + (2**(35 - i)) 
                    buffer.append(newAddress)
                for b in buffer:
                    addresses.append(b)

        for address in addresses:
            mem[address] = val

sum = 0
for entry in mem.values(): sum += entry
print(sum)

   
file.close()