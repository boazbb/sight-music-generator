import random

notePools = {
	# For piano:
	'C_POSITION': {
		'RIGHT': ["c'", "d'", "e'", "f'", "g'"],
		'LEFT': ["c", "d", "e", "f", "g"]
		},
	'F_POSITION': {
		'RIGHT': ["f'", "g'", "a'", "b'", "c''"],
		'LEFT': ["f", "g", "a", "b", "c'"]
		},
	'OCTAVE': {
		'RIGHT': ["c'", "d'", "e'", "f'", "g'", "a'", "b'", "c''"],
		'LEFT': ["c", "d", "e", "f", "g", "a", "b", "c'"]
		},
	'TWO_OCTAVES': {
		'RIGHT': ["c'", "d'", "e'", "f'", "g'", "a'", "b'", "c''",
			"d''", "e''", "f''", "g''", "a''", "b''", "c'''"],
		'LEFT': ["c,", "d,", "e,", "f,", "g,", "a,", "b,",
			"c", "d", "e", "f", "g", "a", "b", "c'"]
		}
	}

rhythmPools = [
	['2', '2'],
	['2.', '4'],
	['2', '4', '4'],
	['4', '2', '4'],
	['4', '4', '4', '4']
]

def getRhythmPattern(type):
	# Gets a random rhythm pattern, with 'type' as the shortest note.
	if type == "QUARTERS":
		return random.choice(rhythmPools)
	if type == "EIGHTS":
		originalA = random.choice(rhythmPools)
		originalB = random.choice(rhythmPools)
		finalA = [i.replace('4', '8').replace('2', '4') for i in originalA]
		finalB = [i.replace('4', '8').replace('2', '4') for i in originalB]
		return finalA+finalB
	if type == "SIXTEENS":
		final = []
		for i in range(4):
			original = random.choice(rhythmPools)
			final += [j.replace('4', '16').replace('2', '8') for j in original]
		return final

def getNotePool(type):
	# Gets a note pool
	return notePools[type]