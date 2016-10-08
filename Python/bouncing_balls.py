def bouncingBall(h, bounce, window):
	if h <= 0 or bounce <= 0 or bounce >= 1 or window >= h:
		return -1
	view = 1
	h *= bounce
	while h > window:
		view += 2
		h *= bounce

	return view