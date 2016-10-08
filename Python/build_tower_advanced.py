def tower_builder(n_floors, block_size):
	w, h = block_size
	tower = []

	# Original width on first floor + added dual sided width on subsequent floors
	total_w = w + (n_floors - 1) * 2 * w

	# Build tower from bottom up
	x = 0
	while x < n_floors:
		floor = (' ' * w * x) + ('*' * (total_w - (x * 2 * w))) + (' ' * w * x)
		# Add height of a certain floor
		y = 0
		while y < h:
			tower = [floor] + tower
			y += 1

		x += 1

	return tower