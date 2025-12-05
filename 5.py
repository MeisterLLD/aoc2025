import re
data = open('5').read()
d_ranges, d_ings = data.split('\n\n')
r_ranges = r'(\d+)-(\d+)'
r_ings = r'(\d+)'
ranges = [(int(m.group(1)), int(m.group(2))) for m in re.finditer(r_ranges,d_ranges)]
ings = [int(x) for x in re.findall(r_ings, d_ings)]

tot = 0
for ing in ings:
    for a,b in ranges:
        if a <= ing <= b:
            tot += 1
            break
print('Part 1 :', tot)

ranges.sort()
fusion = [ranges[0]]
for (a_new, b_new) in ranges[1:]:
    a_last, b_last = fusion[-1]
    if a_new > b_last:
        fusion.append( (a_new, b_new) )
    else:
        fusion[-1] = (a_last, max(b_last,b_new) )

print('Part 2 :', sum( [b-a+1 for a,b in fusion] ) )
