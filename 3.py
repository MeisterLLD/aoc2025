lignes = open('3').read().splitlines()

def maxsubint(chaine, size):
    if size == 1:
        return max(chaine)

    n = len(chaine)
    ind1, max1 = max(enumerate(chaine[0:n-size+1]), key=lambda t: t[1])
    return max1 + maxsubint(chaine[ind1+1:], size-1)

tot1, tot2 = 0, 0
for ligne in lignes:
    tot1 += int(maxsubint(ligne, 2))
    tot2 += int(maxsubint(ligne, 12))
print('Part 1 :', tot1)
print('Part 2 :', tot2)