from nose.tools import assert_equal
from even_tree.even_tree import Tree


def test_tree1():
    tree_edges = [[2, 1], [3, 1], [4, 3], [5, 2], [6, 1], [7, 2], [8, 6], [9, 8], [10, 8]]
    tree = Tree(tree_edges)
    assert_equal(tree.decompose(), 2)

def test_tree2():
    tree_edges = [[2, 1], [3, 2], [4, 3], [5, 2], [6, 4], [7, 4], [8, 1], [9, 5], [10, 4], [11, 4], [12, 8], [13, 2], [14, 2], [15, 8], [16, 10], [17, 1], [18, 17], [19, 18], [20, 4], [21, 15], [22, 20], [23, 2], [24, 12], [25, 21], [26, 17], [27, 5], [28, 27], [29, 4], [30, 25]]
    tree = Tree(tree_edges)
    assert_equal(tree.decompose(), 11)
