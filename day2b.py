#brendon
def find():
	for l in [list(x.strip()) for x in open('/tmp/day2.txt', 'r').readlines()]:
		for k in [list(x.strip()) for x in open('/tmp/day2.txt', 'r').readlines()]:
			if (len(l) -1) == len([val for index, val in enumerate(l) if val == k[index]]):
				return([val for index, val in enumerate(l) if val == k[index]])
print("".join(find()))
