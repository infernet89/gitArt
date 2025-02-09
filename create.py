#!/usr/bin/env python
import subprocess
import datetime
import os

# We work with a 51x7 grid not counting first and last column. We can type 10 characters.

# conversion of each letter in a 5x7 Pixel Art character. Space is AFTER the letter. 0-6 is the first column, 28-34 the last
chars = {
    'A': [1, 2, 3, 4, 5, 6, 7, 10, 14, 17, 22, 23, 24, 25, 26, 27],
    'B': [0, 1, 2, 3, 4, 5, 6, 7, 10, 13, 14, 17, 20, 22, 23, 25, 26],
    'C': [1, 2, 3, 4, 5, 7, 13, 14, 20, 21, 27],
    'D': [0, 1, 2, 3, 4, 5, 6, 7, 13, 14, 20, 22, 23, 24, 25, 26],
    'E': [0, 1, 2, 3, 4, 5, 6, 7, 10, 13, 14, 17, 20, 21, 24, 27],
    'F': [0, 1, 2, 3, 4, 5, 6, 7, 10, 14, 17, 21, 24],
    'G': [1, 2, 3, 4, 5, 7, 13, 14, 17, 20, 21, 24, 25, 26, 27],
    'H': [0, 1, 2, 3, 4, 5, 6, 10, 17, 21, 22, 23, 24, 25, 26, 27],
    'I': [0, 6, 7, 8, 9, 10, 11, 12, 13, 14, 20],
    'J': [5, 7, 13, 14, 20, 21, 22, 23, 24, 25, 26],
    'K': [0, 1, 2, 3, 4, 5, 6, 10, 16, 18, 21, 22, 26, 27],
    'L': [0, 1, 2, 3, 4, 5, 6, 13, 20, 27],
    'M': [0, 1, 2, 3, 4, 5, 6, 8, 16, 22, 28, 29, 30, 31, 32, 33, 34],
    'N': [0, 1, 2, 3, 4, 5, 6, 8, 9, 17, 18, 19, 21, 22, 23, 24, 25, 26, 27],
    'O': [1, 2, 3, 4, 5, 7, 13, 14, 20, 22, 23, 24, 25, 26],
    'P': [0, 1, 2, 3, 4, 5, 6, 7, 10, 14, 17, 22, 23],
    'Q': [1, 2, 3, 4, 5, 7, 13, 14, 19, 20, 22, 23, 24, 25, 26, 27],
    'R': [0, 1, 2, 3, 4, 5, 6, 7, 10, 14, 17, 22, 23, 25, 26, 27],
    'S': [1, 2, 6, 7, 10, 13, 14, 17, 20, 21, 25, 26],
    'T': [0, 7, 14, 15, 16, 17, 18, 19, 20, 21,28],
    'U': [0, 1, 2, 3, 4, 5, 6, 13, 20, 21, 22, 23, 24, 25, 26, 27],
    'V': [0, 1, 2, 3, 4, 5, 13, 20, 21, 22, 23, 24, 25, 26],
    'W': [0, 1, 2, 3, 4, 5, 6, 12, 18, 26, 28, 29, 30, 31, 32, 33, 34],
    'X': [0, 1, 2, 4, 5, 6, 10, 17, 21, 22, 23, 25, 26, 27],
    'Y': [0, 1, 2, 10, 17, 18, 19, 20, 21, 22, 23],
    'Z': [0, 4, 5, 6, 7, 10, 11, 13, 14, 16, 17, 20, 21, 22, 23, 27],
    '8': [7,14,21,1,2,10,17,24,32,33,27,20,13,5,4,29,30],
    '9': [8,9,14,21,29,30,24,17,31,32,33,27,20,13],
}

# visually print a word, for debug purposes
def printWord(word):
	global chars
	textRows=[''] * 7
	for l in word:
		for i in range(0,35):
			if i in chars[l]:
				textRows[i%7]+='#'
			else:
				textRows[i%7]+=' '
	for i in range(0,7):
		print(textRows[i])
	return

# create a commit, converting each pixel of the word in a date
def createCommit(word):
	global chars
	global year
	res=[]
	# transform pixel art in a list of number that represent our 51*7 grid where 0-6 is the first and 350-356 is the last
	offset=0
	for l in word:
		for i in range(0,35):
			if i in chars[l]:
				res.append(i+offset)
		offset+=35
	#then we offset it in order to start with the first monday of the year
	offset = (6 - (datetime.date(year, 1, 1).weekday())) % 7
	res = [x + offset for x in res]
	for day in res:
		command='git commit --date=\''
		command+=(datetime.date(year, 1, 1) + datetime.timedelta(days=day)).strftime('%Y-%m-%d')
		command+='\' -am \'gitArt day '+str(day)+'\' --allow-empty'
		print(command)
		os.system("command")
	return

printWord("INFERNET89")
year=2024
createCommit("INFERNET89")

print("Done!")