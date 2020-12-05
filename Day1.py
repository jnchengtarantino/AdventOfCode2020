file = open("day1input.txt")
lines = file.readlines()

for i in range(len(lines)):
    for j in range(0, i):
        if (int(lines[i]) + int(lines[j]) == 2020):
            statement =  lines[i]+ " * " + lines[j] + " = "  + str(int(lines[i])*int(lines[j]))
            print(statement)
        
file.close()