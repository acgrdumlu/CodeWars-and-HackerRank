alphabet = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')


def alphabet_position(text):
	text = text.lower()
	output = ''

	for character in text:
		if character in alphabet:
			output += str(alphabet.index(character) + 1) + ' '

	output = output.rstrip()
	return output