def loop_size(node):
	size = 1
	# Have a walker traverse each node one-by-one. Have a runner traverse at 2x the speed.
	walker = node
	runner = node.next

	# When the runner laps the walker, we know we are in the loop.
	while(walker != runner):
		runner = runner.next.next
		walker = walker.next

	# Once we know we are in the loop, count one pass through the loop
	while(walker.next != runner):
		size += 1
		walker = walker.next
	return size