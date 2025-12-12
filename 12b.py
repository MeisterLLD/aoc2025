from itertools import product
polyminos_txt = [
    ['..#',
     '.##',
     '###'],

    ['..#',
     '###',
     '###'],

    ['..#',
     '.##',
     '##.'],

    ['##.',
     '.##',
     '###'],

    ['#.#',
     '###',
     '#.#'],

    ['###',
     '#.#',
     '#.#']
]

sizes = [6, 7, 5, 7, 7, 7]


def poly2coord(polymino):
    w, h = len(polymino[0]), len(polymino)
    p = []
    for x, y in product(range(w), range(h)):
        if polymino[y][x] == '#':
            p.append((x, y))
    return p


def valid(c, L, H):
    x, y = c
    return x < L and y < H


def rotate(polymino):
    w, h = len(polymino[0]), len(polymino)
    p = []
    for x in range(w):
        s = ''
        for y in range(h):
            s = polymino[y][x] + s
        p.append(s)
    return p


def translate(polymino, x, y):
    return [(x0+x, y0+y) for (x0, y0) in polymino]


def polymino_to_mask(L, p):
    m = 0
    for x, y in p:
        m |= 1 << (x + y * L)
    return m


def sym(p):
    return [l for l in reversed(p)]


def generate_all_tiles():
    polyminos = []
    for p0 in polyminos_txt:
        p1 = rotate(p0)
        p2 = rotate(p1)
        p3 = rotate(p2)
        p0s, p1s, p2s, p3s = map(sym, (p0, p1, p2, p3))
        instanciations = set()
        for pb in [p0,p1,p2,p3,p0s,p1s,p2s,p3s]:
            p = poly2coord(pb)
            instanciations.add(tuple(p))


        polyminos.append(instanciations)

    return polyminos


def search(board, L, H, current, objective):

    if current == objective:
        return True

    i = 0
    while current[i] == objective[i]:
        i+=1

    for p in polyminos[i]:
        max_x = L - max(x for x,_ in p)
        max_y = H - max(y for _,y in p)
        for x in range(max_x+1):
            for y in range(max_y+1):
                pt = translate(p, x, y)
                if all(map(   lambda c :valid(c, L, H), pt)):
                    ptmask = polymino_to_mask(L, pt)
                    if ptmask & board == 0:
                        current[i] += 1
                        if search(ptmask | board, L, H, current, objective):
                            return True
                        current[i] -= 1

    return False


data = open('12').read().splitlines()[30:]
P1 = 0
polyminos = generate_all_tiles( )

for ligne in data:
    str1, str2 = ligne.split(': ')
    L, H = map(int,  str1.split('x')   )
    objective = list(map(int, str2.split(' ')))
    available = L*H
    needed = sum(x*sizes[i] for i,x in enumerate(objective))

    if needed > available:
        continue

    current = [0]*len(objective)
    if search(0, L, H, current, objective):
        P1 += 1
    print(P1)


