def calculate_years(principal, interest, tax, desired):
	count = 0
	sum = principal
	while sum < desired:
		count += 1
		yearly_interest = sum * interest
		yearly_interest -= yearly_interest * tax
		sum += yearly_interest
	return count