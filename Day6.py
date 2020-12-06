import string
file = open("day6input.txt")
lines = file.readlines()

def intersection(lst1, lst2): 
    lst3 = [value for value in lst1 if value in lst2] 
    return lst3 

letters_sets =[] 
count = 0
group = 0 # Only for debugging purposes
for line in lines:
    if line.strip() == "":
        letters = letters_sets[0]
        for person in letters_sets: letters = intersection(letters, person)
        count += len(letters)
        print(str(len(letters)) + " for group " +str(group))
        group +=1
        letters_sets = []
    else:
        letters = [letter for letter in line.strip()]
        letters_sets.append(letters)

letters = letters_sets[0]
for person in letters_sets: letters = intersection(letters, person)
count += len(letters)
print(str(len(letters)) + " for group " +str(group))
group +=1
letters_sets = []
print(count)
       
file.close()