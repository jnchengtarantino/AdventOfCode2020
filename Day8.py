file = open("day8input.txt")
lines = file.readlines()

for replace in range(len(lines)):
    acc = 0
    run = []
    i = 0

    while (i in range(len(lines))):
        if i in run:
            print("line " + str(replace) + "tested, not the issue")
            break
        else: 
            [instruction, amount] = lines[i].strip().split(" ")
            # print(lines[i].strip() + " : " + str(acc))
            if instruction == "nop":
                if i == replace:
                    run.append(i)
                    i += int(amount)
                    continue
                run.append(i)
                i += 1
                continue
            elif instruction == "jmp":
                if i == replace:
                    run.append(i)
                    i += 1
                    continue
                run.append(i)
                i += int(amount)
                continue
            else: #acc
                run.append(i)
                acc += int(amount)
                i += 1
                continue
    else:
        print("error found on line " + str(replace) + " : " + lines[replace])
        print(str(acc))
        break

file.close()