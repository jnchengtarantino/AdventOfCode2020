file = open("day19input.txt")
lines = file.readlines()

def check(sub, targets, rules):
    # print("string " + sub + " targets " + str(targets))
    if len(sub) == 0 or len(targets) == 0: 
        return (True if len(targets) == len(sub) else False)
    
    if rules[targets[0]] == [['a']]: 
        if sub[0] == 'a': return(check(sub[1:], targets[1:], rules))
        else: return False
    elif rules[targets[0]] == [['b']]: 
        if sub[0] == 'b': return(check(sub[1:], targets[1:], rules))
        else: return False
    else:
        return any(check(sub, r + targets[1:], rules) for r in rules[targets[0]])
 
rules = {}
tests = []
i = 0
while ":" in lines[i]:
    k, v = lines[i].strip().split(":")
    v = v.replace('"', "")
    if "|" in v: 
        v = v.strip().split("|")
        v[0] = v[0].strip().split(" ")
        v[1] = v[1].strip().split(" ")
    else: 
        v = [v.strip().split(" ")]
    rules[k] = v
    i += 1
    rules['8'] = [['42'],['42','8']]
    rules['11'] = [['42','31'],['42','11','31']]

for j in range(i+1, len(lines)): tests.append(lines[j].strip())
print(rules)
print(tests)
count = 0
for test in tests: 
    if check(test, ['0'], rules): count += 1 
    
print(count)
file.close()