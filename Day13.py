from sympy.ntheory.modular import crt

file = open("day13input.txt")
lines = file.readlines()
# data = list(map(int,lines))

# departure = int(lines.pop(0))
# tentBuses = lines.pop(0).strip().split(",")

# buses = []
# for element in tentBuses:
#     if element != "x":
#         buses.append(int(element))
#         print(buses)
    
# it = 0
# earliest = [None] *len(buses)
# itTime = [None] *len(buses)
# while any(time is None for time in earliest) :
#     it += 1
#     for i in range(len(buses)):
#         if buses[i] * it >= departure and earliest[i] is None:
#             earliest[i] = buses[i] * it
#             itTime[i] = it
    
# index = earliest.index(min(earliest))
# earlyBus = buses[index]

# print(earliest)
# print("Bus " + str(earlyBus) + ", iteration " + str(itTime[index]) + ", time " + str(itTime[index]* earlyBus))
# print((itTime[index]*earlyBus - departure) * earlyBus)

buses = lines[1]
moduli = []
residues = []
for i, bus in enumerate(buses.split(',')):
  if bus != 'x':
    bus = int(bus)
    moduli.append(bus)
    residues.append(bus - i)

print(crt(moduli, residues)[0])

file.close()