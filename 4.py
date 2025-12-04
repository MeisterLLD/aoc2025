mat = [ ]
with open('4','r') as f:
    for ligne in f.read().splitlines():
        mat.append([x for x in ligne])
n, m = len(mat), len(mat[0])

def voisins(i,j):
    voisinspotentiels = [ (i,j-1), (i,j+1), (i-1,j-1), (i-1,j), (i-1,j+1), (i+1,j-1), (i+1,j), (i+1,j+1)   ]
    return[ v for v in voisinspotentiels if v[0] >= 0 and v[0] < n and v[1] >= 0 and v[1] < m and mat[v[0]][v[1]] == '@']

res = 0
for i in range(n):
    for j in range(m):
        if mat[i][j] == '@' and len(voisins(i,j)) < 4:
            res += 1

print('Part 1 :', res)

totremoved = 0
justremoved = 1
while justremoved > 0:
    justremoved = 0
    for i in range(n):
        for j in range(m):
            if mat[i][j] == '@' and len(voisins(i,j)) < 4:
                mat[i][j] = '.'
                totremoved += 1
                justremoved += 1

print('Part 2 :', totremoved)