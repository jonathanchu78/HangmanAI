import requests
import time
from hangman import startGame, guess

LETTERS = "esiarntolcdupmghbyfvkwzxqj"

def mine(lyric):
	words = lyric.split(' ')
	outfile1 = open("lyrics.txt", "a")
	outfile2 = open("full-lines.txt", "a")
	outfile2.write(lyric + '\n')
	for w in words:
		outfile1.write(w + '\n')
	outfile1.close()
	outfile2.close()


def oneGame():
	print "ONEGAME"
	startGame()
	index = 25
	while True:
		response = guess(LETTERS[index])
		if response["status"] == "DEAD" or response["status"] == "FREE":
			mine(response["lyrics"])
			return
		index = index - 1

def collect():
	while True:
		oneGame()

collect()