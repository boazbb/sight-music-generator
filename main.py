"""
The main file, all of the actual generating and writing is done here,
while the note and rhythm structures are in note_data.py
"""

import os
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

		# Writing piano staff
		instru = melodic.Melodic(self.file)
		
		instru.writeBars(32)
		


def main():
	s = Score()
	print("Sheet generated.")


if __name__ == "__main__":
	main()