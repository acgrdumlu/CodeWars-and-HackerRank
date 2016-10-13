def lcs(x, y):
	# First Property: https://en.wikipedia.org/wiki/Longest_common_subsequence_problem#First_property
	if x[-1] == y[-1]:
		lcs_string = x[-1]
		return lcs(x[:-1], y[:-1]) + lcs_string if min(len(x), len(y)) > 1 else lcs_string

	# Second Property: https://en.wikipedia.org/wiki/Longest_common_subsequence_problem#Second_property
	else:
		if (min(len(x), len(y))) == 1:
			sequence_one = sequence_two = (y if y in x else '') if (len(x) > len(y)) else (x if x in y else '')
		else:
			sequence_one = lcs(x[:], y[:-1])
			sequence_two = lcs(x[:-1], y[:])

		lcs_string = sequence_one if len(sequence_one) > len(sequence_two) else sequence_two
		return lcs_string