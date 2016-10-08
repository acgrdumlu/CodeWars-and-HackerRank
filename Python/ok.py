SCORE = {'O': '0', 'o': '0', 'k': '1'}


def okkOokOo(s):
	ascii = ''
	for w in s.split('?'):
		binary = ''
		for c in w:
			binary += SCORE.get(c, '')
		ascii += chr(int(binary, 2))

	return ascii