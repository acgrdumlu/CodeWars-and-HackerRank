class Node(object):
	def __init__(self, tree):
		self.parent = None
		self.children_count = 0

	def add_parent(self, p):
		self.parent = p
		while p is not None:
			tree[p - 1].children_count += 1
			p = tree[p - 1].parent


def decompose(tree_edges):
	# Build tree based on instructions
	tree.append(Node(tree))
	for edge in tree_edges:
		new_node = Node(tree)
		new_node.add_parent(edge[1])
		tree.append(new_node)

	# Count edges that would have even # of nodes on both sides
	count = 0
	for idx, node in enumerate(tree):
		if node.parent is not None:
			if node.children_count % 2 == 1:
				count += 1

	print count

# Get tree definition from user
tree_dimensions = [int(x) for x in raw_input().split()]

if len(tree_dimensions) < 2:
	raise ValueError('Need definition for both vertices and edges of our base tree')
else:
	vertices = tree_dimensions[0]
	edges = tree_dimensions[1]

tree_edges = []
for x in xrange(1, edges + 1):
	tree_edges.append([int(y) for y in raw_input().split()])

# Test cases:
# # Should equal 2
# tree_edges = [[2, 1], [3, 1], [4, 3], [5, 2], [6, 1], [7, 2], [8, 6], [9, 8], [10, 8]]
# # Should equal 11
# tree_edges = [[2, 1], [3, 2], [4, 3], [5, 2], [6, 4], [7, 4], [8, 1], [9, 5], [10, 4], [11, 4], [12, 8], [13, 2], [14, 2], [15, 8], [16, 10], [17, 1], [18, 17], [19, 18], [20, 4], [21, 15], [22, 20], [23, 2], [24, 12], [25, 21], [26, 17], [27, 5], [28, 27], [29, 4], [30, 25]]

# Decompose the tree
tree = []
decompose(tree_edges)