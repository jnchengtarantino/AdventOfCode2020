file = open("day16input.txt")
lines = file.readlines()

i = 0
rules = {}
while(lines[i].strip() != ""):
    key, rule = lines[i].strip().split(":")
    ranges = rule.split("or")
    l = []
    for r in ranges:
        max, min = r.split("-")
        l.append((int(max), int(min)))
    rules[key] = l
    i += 1

i += 2
yourT = list(map(int, lines[i].split(",")))

i += 3
nearbyT = []
for line in lines[i:]:
    tempT = []
    nums = list(map(int, line.strip().split(",")))
    for num in nums: tempT.append(num)
    nearbyT.append(tempT)

filteredT = []
for t in nearbyT:
    validT = True
    for num in t:
        validN = False
        for field in rules.values():
            min1, max1 = field[0]
            min2, max2 = field[1]
            if min1 <= num <= max1 or min2 <= num <= max2:
                validN = True
                break
        if not validN:
            validT = False
            break
    if validT:
        filteredT.append(t)
filteredT.append(yourT)

potentialMap = {}
for k in rules: potentialMap[k] = list(range(len(yourT)))

for t in filteredT:
    for x, num in enumerate(t):
        for rule in rules:
            min1, max1 = rules[rule][0]
            min2, max2 = rules[rule][1]
            if x in potentialMap[rule] and not (min1 <= num <= max1 or min2 <= num <= max2):
                potentialMap[rule].remove(x)
                
while any([len(potentialMap[k]) > 1 for k in potentialMap]):
    for rule in potentialMap:
        if len(potentialMap[rule]) == 1:
            temp = potentialMap[rule][0]
            for r in potentialMap:
                if r is not rule and temp in potentialMap[r]: potentialMap[r].remove(temp)
    
print(potentialMap)

product = 1
for k in potentialMap:
    if "departure" in k: product *= yourT[potentialMap[k][0]]

print(product)
file.close()