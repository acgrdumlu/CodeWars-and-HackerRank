def sqInRect(lng, wdth):
	if lng == wdth:
		return None

	# Largest square available = smaller of the two sides
	# Remove that square and then recalc remaining squares
	longer = max(lng, wdth)
	shorter = min(lng, wdth)
	squares = []

	while longer > 1:
		# Terminal size, count 1x1 squares
		if shorter == 1:
			for _ in range(longer):
				squares.append(shorter)
			break
		# Count largest square (aka smaller of the two sides)
		else:
			squares.append(shorter)

		# Terminal size, last square remaining already counted
		if longer == shorter:
			break

		# Remove largest square and arrange dimensions for next count
		longer -= shorter
		if longer < shorter:
			tmp = longer
			longer = shorter
			shorter = tmp

	return squares