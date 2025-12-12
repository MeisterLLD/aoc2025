sizes = [6, 7, 5, 7, 7, 7]
data = open('12').read().splitlines()[30:]
P1 = 0
for ligne in data:
    str1, str2 = ligne.split(': ')
    L, H = map(int,  str1.split('x')   )
    available = L*H
    needed = sum(x*sizes[i] for i,x in enumerate(list(map(int, str2.split(' ')))))
    if needed <= available:
        P1 += 1
print(P1)
