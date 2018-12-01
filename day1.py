# brendon
print(str(sum([int(x.replace('+',"")) for x in open('/tmp/advent_day1.txt', 'r').readlines()])))