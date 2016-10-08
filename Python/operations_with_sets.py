def process_2arrays(arr1, arr2):
	arr1_solo = set(arr1)
	arr2_solo = set(arr2)

	# Using set operations: intersections, symmetric difference, difference
	return [len(arr1_solo & arr2_solo), len(arr1_solo ^ arr2_solo), len(arr1_solo - arr2_solo), len(arr2_solo - arr1_solo)]