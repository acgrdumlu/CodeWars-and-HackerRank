import re
import binascii


def okkOokOo(s):
	s = s.replace(" ", "")
	s = s.replace(",", "")
	s = re.split('[?!]\s*', s)
	binary = ''

	for w in s:
		if 0 < len(w) < 8:
			binary += '0'
		for c in w:
			if c == 'O' or c == 'o':
				binary += '0'
			elif c == 'k':
				binary += '1'

	binary = int(binary, 2)
	return binascii.unhexlify('%x' % binary)