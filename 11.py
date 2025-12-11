from collections import defaultdict
G = defaultdict(list)
data = open('11').read().splitlines()
for ligne in data:
    a, Bs = ligne.split(': ')
    for b in Bs.split(' '):
        G[a].append(b)

def count_paths(graph, start, end, memo=None):
    if memo is None:
        memo = {}
    if start == end:
        return 1
    if start in memo:
        return memo[start]

    # Data assumption : graph has no cycles
    total = sum(  [count_paths(graph, voisin, end, memo)  for voisin in graph[start] ]  )
    memo[start] = total
    return total

print('Part 1 :', count_paths(G, 'you', 'out', None))

# Data assumption : we observed that 'dac -> fft' is impossible
p2 = count_paths(G, 'svr', 'fft') *  count_paths(G, 'fft', 'dac') *  count_paths(G, 'dac', 'out')
print('Part 2 :', p2)
