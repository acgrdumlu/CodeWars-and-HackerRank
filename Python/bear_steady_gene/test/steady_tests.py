from nose.tools import assert_equal
from gene.steady import stabilize


def test_steady1():
    orig_gene = 'GAAATAAA'
    assert_equal(stabilize(orig_gene), 5)
