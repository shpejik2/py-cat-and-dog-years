import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "dog_age,cat_age,expected_human_age",
    [
        pytest.param(
            0,
            0,
            [0, 0],
            id="should return zeros if zero"
        ),
        pytest.param(
            14,
            14,
            [0, 0],
            id="should return zeros less then 15"
        ),
        pytest.param(
            15,
            15,
            [1, 1],
            id="should return one more than 15"
        ),
        (
            24,
            24,
            [1, 1]
        ),
        (
            27,
            27,
            [2, 2]
        ),
        (
            28,
            28,
            [3, 2]
        ),
        (
            100,
            100,
            [21, 17]
        )
    ]
)
def test_get_human_age(
        dog_age: int,
        cat_age: int,
        expected_human_age: list
) -> None:
    assert get_human_age(dog_age, cat_age) == expected_human_age
