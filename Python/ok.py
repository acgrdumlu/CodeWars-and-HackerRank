def okkOokOo(s):
	ascii = ''
	for w in s.split('?'):
		binary = ''
		for c in w:
			if c == 'O' or c == 'o':
				binary += '0'
			elif c == 'k':
				binary += '1'
		ascii += chr(int(binary, 2))

	return ascii