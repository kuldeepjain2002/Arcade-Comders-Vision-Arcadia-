import random
import time
from RPLCD import CharLCD
from picamera import PiCamera
from test import predict 

lcd = CharLCD(cols=16, rows=2, pin_rs=37, pin_e=35, pins_data=[33, 31, 29, 23])

def computerMove():
	return random.choice(["stone", "paper", "scissors"])

def userMove():
	camera = PiCamera()
	camera.resolution = (2560, 1936)
	camera.start_preview()
	sleep(5)
	camera.capture('test.jpg')
	camera.stop_preview()
	return predict('test.jpg')

def computeResult(userMove, computerMove):
	if userMove == computerMove:
		return 0
	win = [("rock", "scissors"), ("scissors", "paper"), ("paper", "rock")]
	if (userMove, computerMove) in win:
		return 1
	else:
		return -1

def print_string(string):
	lcd.write_string(string)
	time.sleep(1)
	lcd.clear()

def main():

	score = 0
	while True:

		if score >= 21:
			break

		uM = userMove()
		cM =computerMove()

		if uM == "none":
			break

		else:
			result = computeResult(uM, cM)
			score += result
			if result == 1:
				result_str = "win"
			if result == 0:
				result_str = "draw"
			if result == -1:
				result_str = "lost"

			print_string(cM)
			print_string_string(result_str)
			print_string(f"score: {score}")
			
			

if __name__ == "__main__":
	main()
