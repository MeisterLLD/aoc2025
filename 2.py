import re
data = open('2').read()
pattern = r'(\d+)\-(\d+)'
ranges = [ (int(m.group(1)), int(m.group(2))) for m in re.finditer(pattern, data)  ]

set1 = set()

for a,b in ranges:
    for i in range(a, b+1):
        chaine = str(i)
        n = len(chaine)
        if chaine[0:n//2] == chaine[n//2:]:
            set1.add(i)

print(f'Part 1 : {sum(set1)}')

def invalid(chaine):
    n = len(chaine)
    for k in range(1, n//2+1):
        if chaine == chaine[0:k] * (n//k):
            return True
    return False

set2 = set()
for a,b in ranges:
    for i in range(a, b+1):
        chaine = str(i)
        if invalid(chaine):
            set2.add(i)
print(f'Part 2 : {sum(set2)}')