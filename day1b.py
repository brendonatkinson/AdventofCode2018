# brendon
def find_answer():
	cumulative, previous = 0, set([0])
	while True:
		for i in [int(x) for x in open('/tmp/advent_day1b.txt', 'r').readlines()]:
			cumulative += i
			if cumulative in previous:
				return(cumulative)
			previous.add(cumulative)
print(find_answer())