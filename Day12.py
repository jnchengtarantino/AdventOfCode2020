import math
file = open("day12input.txt")
lines = file.readlines()

x = 0
y = 0
# ang = 0
waypoint = [10,1]
for line in lines:
    instruction = line[0]
    val = int(line.strip()[1:])
    if instruction == "N": waypoint[1] += val
    elif instruction == "S": waypoint[1] -= val
    elif instruction == "E": waypoint[0] += val
    elif instruction == "W": waypoint[0] -= val
    elif instruction == "L": 
        temp = waypoint[0]
        if val == 90:
            waypoint[0] = -waypoint[1]
            waypoint[1] = temp
        elif val == 180:
            waypoint[0] = -waypoint[0]
            waypoint[1] = -waypoint[1]
        elif val == 270:
            waypoint[0] = waypoint[1]
            waypoint[1] = -temp
    elif instruction == "R": 
        temp = waypoint[0]
        if val == 90:
            waypoint[0] = waypoint[1]
            waypoint[1] = -temp
        elif val == 180:
            waypoint[0] = -waypoint[0]
            waypoint[1] = -waypoint[1]
        elif val == 270:
            waypoint[0] = -waypoint[1]
            waypoint[1] = temp
    elif instruction == "F":
        # x += val * round(math.cos(math.radians(ang)))
        # y += val * round(math.sin(math.radians(ang)))
        x += val * waypoint[0]
        y += val * waypoint[1]
    print(str(x) + " " +str(y)+ " " + str(waypoint))

print("x = " + str(x) + ", y = " + str(y) + ", dist = " +str(abs(x)+abs(y)))
   
file.close()