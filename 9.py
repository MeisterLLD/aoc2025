import re
data = open('9').read()
reg = r'(\d+),(\d+)'
coords = [(int(x[0]), int(x[1])) for x in re.findall(reg, data)]
n = len(coords)

## Part 1
ans1 = 0
for i in range(n):
    for j in range(i+1, n):
        x1, y1 = coords[i]
        x2, y2 = coords[j]
        aire = (abs(x2-x1)+1)*(abs(y2-y1)+1)
        if  aire > ans1:
            ans1 = aire

print('Part 1 :', ans1)

## Part 2
H, V = [], []
for i in range(len(coords)):
    p, q = coords[i], coords[(i + 1) % len(coords)] # data cycles
    if p[0] == q[0]:
        V.append((p, q))
    else:
        H.append((p,q))

def isrectangleinsidepolygon(p, q):
    ''' This is correct only because we are sure that p and q lie
    on the boundary of the polygon ! '''
    min_x, max_x = sorted([p[0], q[0]])
    min_y, max_y = sorted([p[1], q[1]])

    for (x1, y), (x2, _) in H:
        if min_y < y < max_y and max(min_x, min(x1, x2)) < min(max_x, max(x1, x2)):
            return False

    for (x, y1), (_, y2) in V:
        if min_x < x < max_x and max(min_y, min(y1, y2)) < min(max_y, max(y1, y2)):
            return False

    return True

ans2 = 0
for i in range(n):
    for j in range(i+1, n):
        if isrectangleinsidepolygon(coords[i], coords[j]):
            x1, y1 = coords[i]
            x2, y2 = coords[j]
            aire = (abs(x2-x1)+1)*(abs(y2-y1)+1)
            if  aire > ans2:
                ans2 = aire

print('Part 2 :', ans2)