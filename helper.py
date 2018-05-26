from collections import defaultdict
import operator


map = {};
LETTERS = "esiarntolcdupmghbyfvkwzxqj"


def matchStrs(known, unknown):
	for k, u in zip(known, unknown):
		if k != '_':
			if k != u:
				return False;
	return True;

def nextNotGuessed(already_guessed):
	for c in LETTERS:
		if c not in already_guessed and c.isalpha():
			return c

def mostFreqLetter(expr, already_guessed):
	length = len(expr)
	freqs = {}
	if length in map:
		words = map[length]
		for word in words:
			if matchStrs(expr, word):
				#print expr + " " + word
				#not iterate through the found match and increment frequencies for each letter
				for c in word:
					if c not in freqs:
						freqs[c] = 0;
					else:
						freqs[c] = freqs[c] + 1
	index = 0
	#to prevent error when find no matches
	if len(freqs) == 0:
		return nextNotGuessed(already_guessed)
	sorted_freqs = sorted(freqs.items(), key=operator.itemgetter(1), reverse = True)
	print "expression is " + expr
	# print sorted_freqs
	# print index
	while sorted_freqs[index][0] in already_guessed or not sorted_freqs[index][0].isalpha():
		index = index + 1;
		if index == len(sorted_freqs):
			return nextNotGuessed(already_guessed)
	return sorted_freqs[index][0]

# my_guess = nextGuess("__e_e", ['e'])
# print my_guess


def longestWord(str):
	words = str.split(' ')
	unfinished_words = [ x for x in words if "_" in x ]
	#print unfinished_words
	if len(unfinished_words) == 0:
		return "zzzzjfdskasklfjda;lksjdf" #return something that it wont be able to match
	return max(unfinished_words, key=len)

def nextGuess(str, already_guessed):
	# print "str we got was " + str
	# print "alreadyguessed we got was "
	# print already_guessed
	infile = open("lyrics-sorted.txt")
	infile.seek(0)
	for line in infile:
		length = len(line) - 1
		if not length in map:
			map[length] = []
		if line[:-1] not in map[length]:
			map[length].append(line[:-1])
	infile.close()
	return mostFreqLetter(longestWord(str), already_guessed)

#nextGuess("__ i_ __e_ _a_e_as a__ s_i_ _i_e i", ['e', 's', 'i', 'a']);