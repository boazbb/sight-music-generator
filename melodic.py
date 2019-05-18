"""
Writes the notes for melodic instruments (i.e. instruments that 
play a single note at a time).
"""

import random
from note_data import *

REST_CHANCE = 5 # This means one in five notes will be rest

class Melodic:
	def __init__(self, file):
		self.file = file

	# Writes piano bars into the file
	def writeBars(self, barNum):
		self.notePool = getNotePool("TWO_OCTAVES")
		self.rhythmType = 'QUARTERS'
		self.writeTreble(barNum)

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