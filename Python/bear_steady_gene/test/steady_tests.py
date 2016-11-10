# -*- coding: utf-8 -*-
"""NoseTests for Bear Steady Gene"""
from nose.tools import assert_equal
from gene.steady import stabilize


def test_steady1():
    """Tests against the example provided by HackerRank"""
    orig_gene = 'GAAATAAA'
    assert_equal(stabilize(8, orig_gene), 5)
