def duplicate_encode(word):
	characters = list(word.lower())
	counter = {}
	output = ""
	for character in characters:
		if character in counter:
			counter[character] += 1
		else:
			counter[character] = 1
	for character in characters:
		if counter[character] > 1:
			output += ')'
		else:
			output += '('
	return output