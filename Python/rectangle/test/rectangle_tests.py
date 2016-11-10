from nose.tools import assert_equal
from rectangle.rectangle import sqInRect


def test_equal_lngth_wdth():
	assert_equal(sqInRect(5, 5), None)


def test_5_3():
	assert_equal(sqInRect(5, 3), [3, 2, 1, 1])


def test_3_5():
	assert_equal(sqInRect(3, 5), [3, 2, 1, 1])


def test_20_14():
	assert_equal(sqInRect(20, 14), [14, 6, 6, 2, 2, 2])


def test_14_20():
	assert_equal(sqInRect(14, 20), [14, 6, 6, 2, 2, 2])


def test_240_32():
	assert_equal(sqInRect(240, 32), [32, 32, 32, 32, 32, 32, 32, 16, 16])


def test_6250_250():
	assert_equal(sqInRect(6250, 250), [250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250])


def test_625_230():
	assert_equal(sqInRect(625, 230), [230, 230, 165, 65, 65, 35, 30, 5, 5, 5, 5, 5, 5])


def test_731_230():
	assert_equal(sqInRect(731, 230), [230, 230, 230, 41, 41, 41, 41, 41, 25, 16, 9, 7, 2, 2, 2, 1, 1])


def test_37_14():
	assert_equal(sqInRect(37, 14), [14, 14, 9, 5, 4, 1, 1, 1, 1])