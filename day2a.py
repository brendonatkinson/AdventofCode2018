#brendon
two, three = 0,0
for l in [list(x.strip()) for x in open('/tmp/day2.txt', 'r').readlines()]:
	if 2 in [l.count(x) for x in set(l)]:
		two += 1
	if 3 in [l.count(x) for x in set(l)]:
		three += 1
print(two * three)
