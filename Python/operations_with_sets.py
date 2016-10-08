def process_2arrays(arr1, arr2):
	arr1_solo = set(arr1)
	arr2_solo = set(arr2)

	def exists_in_both():
		count = 0
		for a in arr1:
			if a in arr2_solo:
				count += 1
				arr1_solo.remove(a)
				arr2_solo.remove(a)
		return count

	bothCount = exists_in_both()

	def exists_in_one():
		return len(arr1) + len(arr2) - bothCount * 2

	return [bothCount, exists_in_one(), len(arr1_solo), len(arr2_solo)]