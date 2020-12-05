import math
file = open("day5input.txt")
lines = file.readlines()
max = 0
seats = list(range(0, 127*8+7))

#part 1
for line in lines:
    upperRow = 127
    lowerRow = 0
    midRow = (upperRow + lowerRow)/2
    upperCol = 7
    lowerCol = 0
    midCol = (upperCol+lowerCol)/2
    for c in line.strip():
        if c == 'F':
            upperRow = math.floor(midRow)
            midRow = (upperRow+lowerRow)/2
        elif c == 'B':
            lowerRow = math.ceil(midRow)
            midRow = (upperRow+lowerRow)/2
        elif c == 'L':
            upperCol = math.floor(midCol)
            midCol = (upperCol+lowerCol)/2
        elif c == 'R':
            lowerCol = math.ceil(midCol)
            midCol = (upperCol+lowerCol)/2
    id = (midRow*8) + midCol
    print("row " + str(midRow) + " col " + str(midCol) + " id " + str(id))
    if id > max:
        max = id
    if id in seats:
        seats.remove(int(id))

print(max)
print(seats)

#part 2
        
file.close()