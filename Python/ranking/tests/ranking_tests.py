from nose.tools import assert_equal
from ranking.ranking import User


# Note: These test do not come near 100% coverage of scenarios
# The CodeWars submission tests cover more scenarios than this unit test
def test_create_user():
    user = User()
    assert_equal(user.rank, 0)


def test_apply_initial_rank():
    user = User()
    user.inc_progress(-8)
    assert_equal(user.rank, -8)
    assert_equal(user.progress, 3)


def test_apply_rank_neg7():
    user = User()
    user.inc_progress(-7)
    assert_equal(user.rank, -8)
    assert_equal(user.progress, 10)


def test_apply_rank_neg6():
    user = User()
    user.inc_progress(-6)
    assert_equal(user.rank, -8)
    assert_equal(user.progress, 40)


def test_apply_rank_neg5():
    user = User()
    user.inc_progress(-5)
    assert_equal(user.rank, -8)
    assert_equal(user.progress, 90)


def test_apply_rank_neg4():
    user = User()
    user.inc_progress(-4)
    assert_equal(user.rank, -7)
    assert_equal(user.progress, 60)


def test_apply_rank_neg3():
    user = User()
    user.inc_progress(-3)
    assert_equal(user.rank, -6)
    assert_equal(user.progress, 50)


def test_apply_rank_neg2():
    user = User()
    user.inc_progress(-2)
    assert_equal(user.rank, -5)
    assert_equal(user.progress, 60)


def test_apply_rank_neg1():
    user = User()
    user.inc_progress(-1)
    assert_equal(user.rank, -4)
    assert_equal(user.progress, 90)


def test_apply_rank_neg1_on_1():
    user = User(1, 20)
    user.inc_progress(-1)
    assert_equal(user.rank, 1)
    assert_equal(user.progress, 21)


def test_apply_rank_1():
    user = User()
    user.inc_progress(1)
    assert_equal(user.rank, -2)
    assert_equal(user.progress, 40)


def test_apply_rank_2():
    user = User()
    user.inc_progress(2)
    assert_equal(user.rank, 1)
    assert_equal(user.progress, 10)


def test_apply_rank_3():
    user = User()
    user.inc_progress(3)
    assert_equal(user.rank, 3)
    assert_equal(user.progress, 0)


def test_apply_rank_4():
    user = User()
    user.inc_progress(4)
    assert_equal(user.rank, 5)
    assert_equal(user.progress, 10)


def test_apply_rank_5():
    user = User()
    user.inc_progress(5)
    assert_equal(user.rank, 7)
    assert_equal(user.progress, 40)


def test_apply_rank_6():
    user = User()
    user.inc_progress(6)
    assert_equal(user.rank, 8)
    assert_equal(user.progress, 0)


def test_apply_rank_7():
    user = User()
    user.inc_progress(7)
    assert_equal(user.rank, 8)
    assert_equal(user.progress, 0)


def test_apply_rank_8():
    user = User()
    user.inc_progress(8)
    assert_equal(user.rank, 8)
    assert_equal(user.progress, 0)