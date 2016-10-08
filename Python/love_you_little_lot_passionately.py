petals = ['I love you', 'a little', 'a lot', 'passionately', 'madly', 'not at all']


def how_much_i_love_you(nb_petals):
	return petals[nb_petals % len(petals) - 1]