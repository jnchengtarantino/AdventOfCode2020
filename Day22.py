def round(deck1, deck2):
    # print(str(deck1) + ' ' + str(deck2))
    p1 = deck1.pop(0)
    p2 = deck2.pop(0)
    if p1 <= len(deck1) and p2 <= len(deck2):
        print('recurse')
        r1,r2 = game([*deck1[:p1]], [*deck2[:p2]])
        print('done')
        if r1 == []:
            deck2.append(p2)
            deck2.append(p1)
        elif r2 == []:
            deck1.append(p1)
            deck1.append(p2)
    elif p1 > p2:
        deck1.append(p1)
        deck1.append(p2)
    elif p2 > p1:
        deck2.append(p2)
        deck2.append(p1)
    return (deck1,deck2)

def game(deck1, deck2):
    history = set()
    i = 0
    while len(deck1) > 0 and len(deck2) > 0:
        if (tuple(deck1),tuple(deck2)) in history:
            deck2 = []
        else:
            history.add((tuple(deck1),tuple(deck2)))
            deck1, deck2 = round(deck1, deck2)
            i += 1
    return (deck1,deck2)

def score(deck):
    count = 0
    for i, e in enumerate(deck): count += e * (len(deck) - i)
    return count

with open('day22input.txt') as f:
    lines = [line.replace('\n', ' ') for line in f.read().split('\n\n')]

decks = {}
decks[1] = [int(x) for x in lines[0].strip().split(' ')[2:]]
decks[2] = [int(x) for x in lines[1].strip().split(' ')[2:]]

decks[1], decks[2] = game(decks[1], decks[2])

print(score(decks[1]))
print(score(decks[2]))
