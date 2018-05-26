from collections import Counter
from itertools import repeat, chain


infile = open("lyrics.txt")
infile.seek(0)
lines = []
for line in infile:
	lines.append(line[:-1])
	print line[:-1]
infile.close()

sorted = list(chain.from_iterable(repeat(i, c) for i,c in Counter(lines).most_common()))

outfile = open("lyrics-sorted.txt", "w+")
for line in sorted:
	outfile.write(line + '\n')
outfile.close()