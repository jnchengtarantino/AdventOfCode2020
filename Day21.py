file = open("day21input.txt")
lines = file.readlines()

words = set({})
contenders = {}

for line in lines:
    inWords, inAllergens = line.strip().split("(")
    inWords = set(inWords.strip().split(" "))
    for w in inWords: 
        if w not in words: words.add(w)

    inAllergens = set(inAllergens.strip().replace("contains ","").replace(")","").replace(",","").split(" "))
    for a in inAllergens:
        if a not in contenders: contenders[a] = inWords
        else: contenders[a] = contenders[a].intersection(inWords)

# part 1
# nonContenders = set(words - set.union(*contenders.values()))
# count = 0
# for line in lines:
#     temp = line.split(" ")
#     for w in temp:
#         if w in nonContenders: count += 1
# print(count)

done = []
while any(len(s) > 1 for s in contenders.values()):
   for k,s in contenders.items():
       if len(s) == 1 and k not in done:
            for k2, s2 in contenders.items():
               if s.issubset(s2) and k2 is not k: contenders[k2] = s2 - s
            done.append(k)

done.sort()
fin = []
for k in done: fin.append(*contenders[k])
print(','.join(fin))
file.close()