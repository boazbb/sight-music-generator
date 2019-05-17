"""
The main file, all of the actual generating and writing is done here,
while the note and rhythm structures are in note_data.py
"""

import os, random
from note_data import *

TITLE = "Sight Reading Exersice"
COMPOSER = "SightMusicGenerator"

BAR_NUM = 32 # number of bars in the score.
REST_CHANCE = 5 # This means one in five notes will be rest

class Score:
	def __init__(self):
		# Basic lilypond file structures:
		self.file = open("seerScore.ly", "w+")
		self.file.write('\\version "2.18.2"\n')
		self.file.write('\\header {\n  title = "'+TITLE+'"\n  composer = "'+COMPOSER+'"\n}')

		# Writing piano staff
		self.file.write('\\new PianoStaff <<\n')
		
		self.writeBars(32)

		self.file.write('>>')

	# Writes piano bars into the file
	def writeBars(self, barNum):
		self.notePool = getNotePool("TWO_OCTAVES")
		self.rhythmType = 'QUARTERS'
		self.writeTreble(barNum)
		self.writeBass(barNum)

	# Writes the left hand bars
	def writeBass(self, barNum):
		self.file.write('\t\\new Staff { \\clef "bass" ')
		for i in range(BAR_NUM):
			self.writeBar('LEFT')
		self.file.write('}\n')

	# Writes the right hand bars
	def writeTreble(self, barNum):
		self.file.write('\t\\new Staff { \\time 4/4 ')
		for i in range(barNum):
			self.writeBar('RIGHT')
		self.file.write('}\n')

	# Writes the actual music content of a bar
	def writeBar(self, hand):
		rhythm = getRhythmPattern(self.rhythmType)
		for i in rhythm:
			if random.randint(0, (REST_CHANCE-1)) == 0:
				note = 'r'
			else:
				note = random.choice(self.notePool[hand])
			self.file.write(note+i)


def main():
	s = Score()
	print("Sheet generated.")


if __name__ == "__main__":
	main()