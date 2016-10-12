def sqInRect(lng, wdth, recur=0):
	if lng == wdth:
		# If this is original function call, return None for equal sides (per kata requirement);
		# if this is recursion call, we reached the smallest square, so get out of recursion.
		return (None, [lng])[recur]

	lesser = min(lng, wdth)
	return [lesser] + sqInRect(lesser, abs(lng - wdth), recur=1)