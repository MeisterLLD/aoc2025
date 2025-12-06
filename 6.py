import re
from math import prod

lignes = open('6').read().splitlines()
regnum = r'(\d+)'
regop = r'[+*]'
n = len(lignes)-1
tab = [  list(map(int, re.findall(regnum, ligne)))  for ligne in lignes[0:n]]
m = len(tab[0])
ops = re.findall(regop, lignes[-1])

total = 0
for j in range(m):
    total += sum(   [tab[x][j] for x in range(n)] ) if ops[j] == '+' else prod(   [tab[x][j] for x in range(n)] )
print('Part 1 :', total)



total = 0
m = len(lignes[0])
j = m - 1
while j > 0:
    numbers = [ ]
    if lignes[0][j] + lignes[1][j] + lignes[2][j] + lignes[3][j] == '    ':
        j -= 1
    while (op:=lignes[4][j]) == ' ':
        numbers.append(int(lignes[0][j] + lignes[1][j] + lignes[2][j] + lignes[3][j]))
        j -= 1
    numbers.append(int(lignes[0][j] + lignes[1][j] + lignes[2][j] + lignes[3][j]))
    total += sum(numbers) if op == '+' else prod(numbers)
    j -= 1
print('Part 2 :', total)
