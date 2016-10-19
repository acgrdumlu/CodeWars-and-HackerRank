class Tree(object):
    def __init__(self, branches):
        # Add initial leaf node
        self.leaves = [Leaf()]
        # Build rest of tree based on instructions
        for branch in branches:
            new_leaf = Leaf()
            new_leaf.add_parent(branch[1], self.leaves)
            self.leaves.append(new_leaf)

    def decompose(self):
        # Count edges that would have even # of nodes on both sides
        count = 0
        for node in self.leaves:
            if node.parent is not None:
                if node.children_count % 2 == 1:
                    count += 1
        return count


class Leaf(object):
    def __init__(self):
        self.parent = None
        self.children_count = 0

    def add_parent(self, p, leaves):
        self.parent = p
        while p is not None:
            leaves[p - 1].children_count += 1
            p = leaves[p - 1].parent


# Skip this section if nosetesting. This section is just for submission to HackerRank
if __name__ == "__main__":
    # Input format
    # First line contains two integers N and M. N is the number of vertices, and M is the number
    # of edges. The next M lines contain two integers U and V which specifies an edge of the tree.

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

    # Decompose the tree
    tree = Tree(tree_edges)
    print tree.decompose()
