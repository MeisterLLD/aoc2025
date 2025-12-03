import re
lignes = open('1').read().splitlines()
d = {'R' : 1, 'L' : -1}
compteur = 50
tot1, tot2 = 0, 0

for ligne in lignes:
    signe = d[ligne[0]]
    val = int(re.search(r'(\d+)', ligne).group(0))
    for _ in range(val):
        compteur += signe
        if compteur == -1:
            compteur = 99
        if compteur == 100:
            compteur = 0
        if compteur == 0:
            tot2 += 1

    if compteur == 0:
        tot1 += 1

print('Part 1 :', tot1)
print('Part 2 :', tot2)