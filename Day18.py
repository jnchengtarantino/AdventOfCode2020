def solve(working):
    while "(" in working:
        start = working.find("(")
        i = start + 1
        count = 1
        while count > 0:
            if working[i] == "(" : count += 1
            elif working[i] == ")" : count -= 1
            i += 1
        end = i
        working = working[:start] + str(solve(working[start+1:end-1])) + working[end:]
    
    workingL = working.split(" ")
    while "+" in workingL:
        pos = workingL.index("+")
        workingL[pos] = str(int(workingL[pos-1]) + int(workingL[pos+1]))
        workingL.pop(pos+1)
        workingL.pop(pos-1)

    for i in range(len(workingL)):
        if i == 0: current = int(workingL[i])
        if workingL[i] == "*": 
            current *= int(workingL[i+1])
    return current

file = open("day18input.txt")
lines = file.readlines()

sum = 0
for line in lines:
    sum += solve(line.strip())

print(sum)
file.close()