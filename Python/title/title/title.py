def title_case(title, minor_words=''):
	if title is None or title == '':
		return ''

	words = title.split()
	title = words[0].capitalize()
	words.pop(0)

	minor_words = minor_words.lower().split()
	for word in words:
		if word.lower() not in minor_words:
			title += ' ' + word.capitalize()
		else:
			title += ' ' + word.lower()

	return title