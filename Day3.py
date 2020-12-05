file = open("day3input.txt")
lines = file.readlines()
x = 0
y = 0
count = 0
length = len(lines[0]) -1 # -1 is to remove the \n character from the string

print(repr(lines[0]))
# part 1
while(y < len(lines)):
    if(lines[y][x%length] == '#'):
        count+=1
    x +=3
    y+=1

print(count)

#part 2

file.close()