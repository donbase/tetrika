import pytest
from contextlib import nullcontext as does_not_raise
from task1.solution1 import sum_two, foo_1, foo_2


@pytest.mark.parametrize(
    "a, b, res, expectation",
    [
        (1, 2, 3, does_not_raise()),
        ("1", 2, 3, pytest.raises(TypeError)),
        (1, "2", 3, pytest.raises(TypeError)),
        ("1", "2", 3, pytest.raises(TypeError)),
        (False, 0, -1, pytest.raises(TypeError)),
        (4, True, 5, pytest.raises(TypeError)),
        (True, True, 2, pytest.raises(TypeError)),
        (1.0, 1.0, 2, pytest.raises(TypeError)),
        (1, 1.0, 2, pytest.raises(TypeError)),
        (1.0, 1, 2, pytest.raises(TypeError)),
    ],
)
def test_sum_two(a, b, res, expectation):
    with expectation:
        assert sum_two(a, b) == res


@pytest.mark.parametrize(
    "a, b, c, d, res, expectation",
    [
        (1, 2, 3, 4, 0, pytest.raises(TypeError)),
        ("1", True, 3.0, 0, 0, pytest.raises(TypeError)),
        (1.0, 1.0, 3.0, 0.0, 0, pytest.raises(TypeError)),
        ("2", "2", "2", "5", 0, pytest.raises(TypeError)),
        ("2", 2, True, 4.1, 0, does_not_raise()),
    ],
)
def test_foo_1(a, b, c, d, res, expectation):
    with expectation:
        assert foo_1(a, b, c, d) == res


@pytest.mark.parametrize("res, expectation", [(0, does_not_raise())])
def test_foo_2(res, expectation):
    with expectation:
        assert foo_2() == res
