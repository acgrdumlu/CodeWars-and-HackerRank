from nose.tools import assert_equal
from lcs.lcs import lcs


def test_single_letter_diff():
	assert_equal(lcs("a", "b"), "")


def test_single_letter_same():
	assert_equal(lcs("a", "a"), "a")


def test_single_word_ordered2():
	assert_equal(lcs("abcdef", "abc"), "abc")


def test_single_word_unordered1():
	assert_equal(lcs("abc", "ac"), "ac")


def test_single_word_unordered2():
	assert_equal(lcs("abcdef", "acf"), "acf")


def test_numbers():
	assert_equal(lcs("132535365", "123456789"), "12356")


def test_words1():
	assert_equal(lcs("anothertest", "notatest"), "nottest")


def test_words2():
	assert_equal(lcs("finaltest", "zzzfinallyzzz"), "final")