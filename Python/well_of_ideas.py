def well(x):
	good = 0
	for case in x:
		if case == 'good':
			good += 1
	if good > 2:
		return 'I smell a series!'
	elif good >= 1:
		return 'Publish!'
	else:
		return 'Fail!'