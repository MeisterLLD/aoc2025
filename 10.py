from collections import deque
def bfs(initmsk, targetmsk, buttonsmsk):
    dist = {initmsk : 0}
    file = deque([initmsk])
    while file:
        x = file.popleft()

        if x == targetmsk:
            return dist[x]

        for b in buttonsmsk:
            v = x^b
            if v not in dist:
                file.append(v)
                dist[v] = dist[x]+1

def dfs(current, target, buttons, idx, nbpress, best, seen):
    key = (idx, tuple(current))
    if key in seen and seen[key] <= nbpress:
        return
    seen[key] = nbpress

    # pruning
    if nbpress >= best[0]:
        return
    if any(current[i] > target[i] for i in range(len(target))):
        return
    if idx == len(buttons):
        if current == target:
            best[0] = nbpress
        return

    remaining = sum(target[i] - current[i] for i in range(len(target)))
    if nbpress + remaining >= best[0]:
        return

    max_press = max((target[i] - current[i]) for i in buttons[idx])
    for k in range(max_press, -1, -1):
        nxt = current[:]
        for i in buttons[idx]:
            nxt[i] += k
        dfs(nxt, target, buttons, idx + 1, nbpress + k, best, seen)


from scipy.optimize import milp, LinearConstraint, Bounds
import numpy as np

def solve_machine(buttons, target):
    target = np.array(target)
    n = len(target)
    m = len(buttons)

    A = np.zeros((n, m), dtype=int)
    for j, cols in enumerate(buttons):
        A[cols, j] = 1

    c = np.ones(m)                         
    integrality = np.ones(m)               
    bounds = Bounds(0, np.inf)             
    constraints = LinearConstraint(A, target, target)   

    res = milp(c, constraints=constraints,
               integrality=integrality,
               bounds=bounds)

    return int(round(res.fun))




import re
data = open('10').read().splitlines()
P1, P2 = 0, 0
for ligne in data:
    premask = re.findall(r"\[([^\]]+)\]", ligne)[0]
    preboutons = [tuple(map(int, t.split(','))) for t in re.findall(r"\(([^)]+)\)", ligne)]
    targetmask = 0b0
    for i, char in enumerate(premask):
        if char == '#':
            targetmask |= 1<<i
    buttonsmsk = [sum(1<<i for i in b) for b in preboutons]

    joltage = tuple(map(int, re.findall(r"\{([^}]+)\}", ligne)[0].split(',')))
    P1 += bfs(0, targetmask, buttonsmsk)

print('Part 1 :', P1)

total = 0
for line in data:
    preboutons = [tuple(map(int, t.split(',')))
                  for t in re.findall(r"\(([^)]+)\)", line)]
    target = list(map(int,
                re.findall(r"\{([^}]+)\}", line)[0].split(',')))

    total += solve_machine(preboutons, target)

print(total)

print('Part 2 :', P2)

