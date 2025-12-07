lignes = open('7').read().splitlines()
splitters = [ ]
for i, ligne in enumerate(lignes):
    for j, char in enumerate(ligne):
        if char == '^':
            splitters.append((i,j))
        if char == 'S':
            start = (i,j)

def isactive(pos, splitters):
    p, q = pos
    if p == 2:
        return True

    if (p-1,q-1) not in splitters and (p-1,q) not in splitters and (p-1,q+1) not in splitters:
        return isactive((p-1,q), splitters)

    return (p-1,q) not in splitters

ans1 = sum([ int(isactive(pos, splitters)) for pos in splitters ])
print('Part 1 :', ans1)

splitters = set(splitters)
from functools import cache

@cache
def nbtimelines(pos):
    pmax = max( T[0] for T in splitters)
    p, q = pos
    if p > pmax:
        return 1

    if (p, q) not in splitters:
        return nbtimelines((p+1,q))

    return nbtimelines((p,q-1)) + nbtimelines((p, q+1))

print('Part 2 :', nbtimelines(start))