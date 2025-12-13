data = open('12').read().splitlines()[30:]
P1 = 0
for ligne in data:
    str1, str2 = ligne.split(': ')
    L, H = map(int,  str1.split('x')   )
    available = L*H
    if available >= 9*sum((list(map(int, str2.split(' '))))):
        P1 += 1
print(P1)
