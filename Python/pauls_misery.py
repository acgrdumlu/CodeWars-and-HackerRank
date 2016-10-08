misery = {
	'kata': 5,
	'Petes kata': 10,
	'life': 0,
	'eating': 1
}


def paul(x):
	score = sum(misery[task] for task in x)
	if score < 40:
		return 'Super happy!'
	elif 40 <= score < 70:
		return 'Happy!'
	elif 70 <= score < 100:
		return 'Sad!'
	elif score >= 100:
		return 'Miserable!'