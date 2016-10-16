predictions = []
num_tests = int(raw_input())
for test in range(0, num_tests):
	days = raw_input()
	predictions.append([int(x) for x in raw_input().split()])


def calculate(prediction):
	max_price = max(prediction)
	max_price_idx = prediction.index(max_price)
	profit = 0

	for idx in xrange(0, max_price_idx):
		profit += max_price - prediction[idx]

	if len(prediction) > max_price_idx + 1:
		profit += calculate(prediction[max_price_idx + 1:])
	return profit

for prediction in predictions:
	print calculate(prediction)