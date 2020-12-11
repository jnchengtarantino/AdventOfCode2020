from copy import deepcopy
def count(data):
    count = 0
    for i in range(1,len(data) - 1):
        for j in range(1, len(data[i]) -1):
            if data[i][j] == "#": count += 1
    return count

def calc(data,copy):
    changed = False
    for i in range(1,len(data) - 1):
        for j in range(1, len(data[i]) -1):
            adj = 0
            # if data[i-1][j-1] == "#": adj += 1
            # if data[i-1][j] == "#": adj += 1
            # if data[i-1][j+1] == "#": adj += 1
            # if data[i][j-1] == "#": adj += 1
            # if data[i][j+1] == "#": adj += 1
            # if data[i+1][j-1] == "#": adj += 1
            # if data[i+1][j] == "#": adj += 1
            # if data[i+1][j+1] == "#": adj += 1
            current = "."
            [x,y] = [i-1,j-1]
            while current == ".":
                current = data[x][y]
                x -= 1
                y -= 1 
            if current == "#": adj += 1

            current = "."
            [x,y] = [i-1,j]
            while current == ".":
                current = data[x][y]
                x -= 1 
            if current == "#": adj += 1

            current = "."
            [x,y] = [i-1,j+1]
            while current == ".":
                current = data[x][y]
                x -= 1
                y += 1 
            if current == "#": adj += 1

            current = "."
            [x,y] = [i,j-1]
            while current == ".":
                current = data[x][y]
                y -= 1 
            if current == "#": adj += 1

            current = "."
            [x,y] = [i,j+1]
            while current == ".":
                current = data[x][y]
                y += 1 
            if current == "#": adj += 1

            current = "."
            [x,y] = [i+1,j-1]
            while current == ".":
                current = data[x][y]
                x += 1
                y -= 1 
            if current == "#": adj += 1

            current = "."
            [x,y] = [i+1,j]
            while current == ".":
                current = data[x][y]
                x += 1
            if current == "#": adj += 1

            current = "."
            [x,y] = [i+1,j+1]
            while current == ".":
                current = data[x][y]
                x += 1
                y += 1
            if current == "#": adj += 1
            
            if data[i][j] == "L" and adj == 0: 
                copy[i][j] = "#"
                changed = True
            if data[i][j] == "#" and adj >= 5:
                copy[i][j] = "L"
                changed = True
    return changed

def dataprint(data):
    for line in data:
        print(line)

file = open("day11input.txt")
lines = file.readlines()

lines.insert(0,len(lines[0].strip())*"~")
lines.append(len(lines[0].strip())*"~")

data = []
for line in lines:
    temp = "~" + line.strip() + "~"
    data.append([char for char in temp])

unstable = True
iteration = 0
while(unstable):
    print("iteration " + str(iteration))
    copy = deepcopy(data)
    unstable = calc(data, copy)
    data = deepcopy(copy)
    iteration += 1
    # dataprint(data)

print(count(data))
file.close()