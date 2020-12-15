file = open("day15input.txt")
lines = file.readlines()
# data = list(map(int,lines))

nums = list(map(int,lines[0].split(",")))
d = {}
for j in range(len(nums) - 1): d[nums[j]] = j + 1
prev = nums[-1]
i = len(nums) + 1
while(i < 30000000 + 1):
    new = None
    if prev in d:
        new = i - d[prev] - 1
    else:
        new = 0
    # print(d)
    # print("turn " + str(i) + " prev " + str(prev) + " new " + str(new))
    if i % 10000 == 0: print("reached i " + str(i))
    d[prev] = i - 1
    prev = new    
    i += 1
   
print(prev)
file.close()