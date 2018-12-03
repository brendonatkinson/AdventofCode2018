#brendon
two, three, twoseen, threeseen = 0,0, False, False
for l in [list(x.strip()) for x in open('/tmp/day2.txt', 'r').readlines()]:
	if 2 in [l.count(x) for x in set(l)]:
		two += 1
	if 3 in [l.count(x) for x in set(l)]:
		three += 1
print(two * three)