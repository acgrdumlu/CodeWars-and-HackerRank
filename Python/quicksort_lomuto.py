n = raw_input("Enter length of array: ")
ar = [int(x) for x in raw_input("Enter array of numbers separated by spaces: ").split()]


def quicksort(ar, lo, hi):
	if lo < hi:
		p = partition(ar, lo, hi)
		quicksort(ar, lo, p - 1)
		quicksort(ar, p + 1, hi)
	return ' '.join(str(j) for j in ar)


def partition(ar, lo, hi):
	pivot = ar[hi]
	i = lo
	for x in xrange(lo, hi):
		if ar[x] <= pivot:
			ar[i], ar[x] = ar[x], ar[i]
			i += 1
	ar[i], ar[hi] = ar[hi], ar[i]
	print ' '.join(str(j) for j in ar)
	return i


quicksort(ar, 0, len(ar) - 1)