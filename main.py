"""
The main file, all of the actual generating and writing is done here,
while the note and rhythm structures are in note_data.py
"""

import os, sys
from note_data import *
import piano, melodic

TITLE = "Sight Reading Exersice"
COMPOSER = "Sight Music Generator"

BAR_NUM = 32 # number of bars in the score.

class Score:
	def __init__(self):
		# Basic lilypond file structures:
		self.file = open("smgScore.ly", "w+")
		self.file.write('\\version "2.18.2"\n')
		self.file.write('\\header {\n  title = "'+TITLE+'"\n  composer = "'+COMPOSER+'"\n}')

		inst, bars = self.parse_args(sys.argv)
		
		inst.writeBars(bars)
		
		# Parsing the arguemnts
	def parse_args(self, arguments):
		usage = "Wrong Syntax. usage: main.py -piano/-melodic numBars"
		if (sys.argv[1] == "-piano"):
			inst = piano.Piano(self.file)
		elif (sys.argv[1] == "-melodic"):
			inst = melodic.Melodic(self.file)
		else:
			print(usage)
			exit()
		bars = int(sys.argv[2])
		return inst, bars

def main():
	s = Score()
	print("Sheet generated.")


if __name__ == "__main__":
	main()