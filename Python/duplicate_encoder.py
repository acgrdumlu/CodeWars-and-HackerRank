from collections import Counter


def duplicate_encode(word):
	word = word.lower()
	counter = Counter(word)
	output = ''

	for character in word:
		if counter[character] > 1:
			output += ')'
		else:
			output += '('
	return output