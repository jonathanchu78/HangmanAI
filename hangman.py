import requests
import time
from helper import nextGuess

url = "http://upe.42069.fun"
access = "/HlGKM"
reset_path = access + "/reset"
 
#start game
def startGame():
	start = requests.get(url = url + access)
	data = start.json()
	print data

def guess(letter):
	print letter
	data = {"guess":letter}
	response = requests.post(url = url + access, data = data)
	time.sleep(0.5)
	print response.json()
	return response.json()

# data = {"guess":"e"}
# guess1 = requests.post(url = url + access, data = data)
# print guess1.json()

def reset():
	data = {"email":"jonathanchu78@gmail.com"}
	response = requests.post(url = url + reset_path, data = data)
	time.sleep(0.5)
	print response.json()

def mine(lyric):
	words = lyric.split(' ')
	outfile1 = open("lyrics.txt", "a")
	outfile2 = open("full-lines.txt", "a")
	outfile2.write(lyric + '\n')
	for w in words:
		outfile1.write(w + '\n')
	outfile1.close()
	outfile2.close()

def play():
	startGame()
	guess('e') 
	guess('i')
	response = guess('s')
	print response

	finished = False
	already_guessed = ['e', 'i', 's']
	#guess_num = 0
	while not finished:
		if response["status"] == "DEAD" or response["status"] == "FREE":
			#mine(response["lyrics"])
			return
		# guess_num = guess_num + 1
		state = response["state"]
		# print "state is " + state
		my_guess = nextGuess(state, already_guessed)
		response = guess(my_guess)
		already_guessed.append(my_guess)

def fullGame():
	counter = 0
	while counter < 101:
		play()

fullGame()