file = open("day4input.txt")
lines = file.readlines()

dicts = []
temp_dict = {}

for line in lines:
    if line.strip() == "" :
        dicts.append(temp_dict)
        temp_dict = {}
    else:
        data = line.split(" ")
        for info in data:
            [key,val] = info.strip().split(":")
            temp_dict[key] = val

dicts.append(temp_dict)
allowedHcl = "0123456789abcdef"
allowedEcl= ["amb","blu","brn","gry","grn","hzl","oth"]
allowedPid = "0123456789"

count = 0
for entry in dicts:
    if "byr" in entry and "iyr" in entry and "eyr" in entry and "hgt" in entry and "hcl" in entry and "ecl" in entry and "pid" in entry:
        if not 1920 <= int(entry["byr"]) <= 2002:
            print("failed on byr " + entry["byr"])
            continue
        elif not 2010 <= int(entry["iyr"]) <= 2020:
            print("failed on iyr " + entry["iyr"])
            continue
        elif not 2020 <= int(entry["eyr"]) <= 2030:
            print("failed on eyr " + entry["eyr"])
            continue
        elif not ( (entry["hgt"][-2:] == "cm" and 150 <= int(entry["hgt"][:-2]) <= 193) or (entry["hgt"][-2:] == "in" and 59 <= int(entry["hgt"][:-2]) <= 76) ):
            print("failed on hgt " + entry["hgt"])
            continue
        elif not (entry["hcl"][:1] == "#" and len(entry["hcl"][1:]) == 6 and all(c in allowedHcl for c in entry["hcl"][1:])):
            print("failed on hcl " + entry["hcl"])
            continue
        elif not entry["ecl"] in allowedEcl:
            print("failed on ecl " + entry["ecl"])
            continue
        elif not (len(entry["pid"]) == 9 and all(c in allowedPid for c in entry["pid"])):
            print("failed on pid " + entry["pid"])
            continue
        else:
            count += 1
print(count)
file.close()