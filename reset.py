import requests
import time

url = "http://upe.42069.fun"
access = "/HlGKM"
reset_path = access + "/reset"

def reset():
	data = {"email":"jonathanchu78@gmail.com"}
	response = requests.post(url = url + reset_path, data = data)
	time.sleep(0.5)
	print response.json()

reset()