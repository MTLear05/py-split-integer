from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    result = split_integer(10, 2)
    assert sum(result) == 10


def test_sum_of_the_parts_should_be_equal_to_value_when_not_divisible() -> None:
    # catches implementation that just does [value // parts] * parts
    result = split_integer(10, 4)
    assert sum(result) == 10


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    # when divisible, all parts must be equal, not just "sum correct"
    result = split_integer(10, 2)

    assert isinstance(result, list)
    assert result == [5, 5]  # exact expected output
    assert all(part == 5 for part in result)


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    result = split_integer(10, 1)
    assert result == [10]


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    # when there is a remainder, numbers must be sorted AND not all equal
    result = split_integer(10, 3)

    assert result == sorted(result)
    assert len(set(result)) > 1  # [3, 3, 3] is NOT allowed here


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    result = split_integer(1, 3)
    assert result == [0, 0, 1]