from nose.tools import assert_equal
from title.title import title_case


def test_empty():
	assert_equal(title_case(''), '')


def test_first_word_in_exclusions():
	assert_equal(title_case('a clash of KINGS', 'a an the of'), 'A Clash of Kings')


def test_all_upper():
	assert_equal(title_case('THE WIND IN THE WILLOWS', 'The In'), 'The Wind in the Willows')


def test_all_lower():
	assert_equal(title_case('the quick brown fox'), 'The Quick Brown Fox')


def test_single_word():
	assert_equal(title_case('ab', 'ab'), 'Ab')