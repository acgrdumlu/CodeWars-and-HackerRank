def toJadenCase(string):
	jadenCase = ''
	for word in string.split(' '):
		jadenCase += upperFirstLetter(word) + ' '
	return jadenCase[0:-1]


def upperFirstLetter(word):
	print word
	return word[0].upper() + word[1:]