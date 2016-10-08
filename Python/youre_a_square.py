import math


def is_square(n):
	if n >= 0:
		return math.sqrt(n).is_integer()
	else:
		return False