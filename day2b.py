#brendon
def find():
	data = [list(x.strip()) for x in open('/tmp/day2.txt', 'r').readlines()]
	for l in data:
		for k in data:
			intersection = [val for index, val in enumerate(l) if val == k[index]]
			if (len(l) -1) == len(intersection):
				return(intersection)
print("".join(find()))