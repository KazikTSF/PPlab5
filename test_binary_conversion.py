import pytest

import utils


@pytest.mark.parametrize(
    "number, expected",
    [
        (0, "0"),
        (1, "1"),
        (2, "10"),
        (5, "101"),
        (10, "1010"),
        (100, "1100100"),
    ],
)
def test_int_to_binary_correctness(number, expected):
    assert utils.int_to_binary(number) == expected


@pytest.mark.parametrize("number", [-1, -10, 101, 200])
def test_int_to_binary_out_of_range(number):
    with pytest.raises(ValueError):
        utils.int_to_binary(number)


@pytest.mark.parametrize("number", [0.5, 1.2, 50.5])
def test_int_to_binary_not_natural(number):
    with pytest.raises(TypeError):
        utils.int_to_binary(number)

