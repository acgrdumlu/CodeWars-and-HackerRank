def title_case(title, minor_words=''):
	if title is None or title == '':
		return ''

	# Capitalize first word
	words = title.split()
	title = words[0].capitalize()
	words.pop(0)

	# Capitalize rest of sentence based on minor words
	minor_words = minor_words.lower().split()
	rest_of_sentence = ' '.join(word.capitalize() if word.lower() not in minor_words else word.lower() for word in words)

	# Combine sentence
	if rest_of_sentence != '':
		return title + ' ' + rest_of_sentence
	else:
		return title