from typing import Final
from typing import List
from typing import Union

import pytest
from bp.domain import MAX_HEIGHT_VALUE
from bp.domain import MAX_HEIGHTS
from bp.domain import MIN_HEIGHT_VALUE
from bp.domain import MIN_HEIGHTS
from bp.domain import Parameters
from bp.errors import HeightsLengthConstraintFailed
from bp.errors import HeightValueConstraintFailed
from bp.max_area_getter import MaxAreaGetter

EXTRA_VALUES_IN_HEIGHTS: Final = 1
REMOVED_VALUES_FROM_HEIGHTS: Final = 1
DECREMENT: Final = 1
INCREMENT: Final = 1

CASE_1: Final = (
    [1] * (MAX_HEIGHTS + EXTRA_VALUES_IN_HEIGHTS),
    HeightsLengthConstraintFailed(),
)
CASE_2: Final = (
    [1] * (MIN_HEIGHTS - REMOVED_VALUES_FROM_HEIGHTS),
    HeightsLengthConstraintFailed(),
)
CASE_3: Final = ([1, MIN_HEIGHT_VALUE - DECREMENT], HeightValueConstraintFailed())
CASE_4: Final = ([1, MAX_HEIGHT_VALUE + INCREMENT], HeightValueConstraintFailed())


class TestParametersConstraints:
    def given(
        self,
        heights: List[int],
        expected_exception: Union[
            HeightsLengthConstraintFailed, HeightValueConstraintFailed
        ],
    ):
        self.heights = heights
        self.expected_exception = expected_exception

    def when(self):
        try:
            self.parameters = Parameters(self.heights)
        except Exception as e:
            self.exception_sent = e

    def then(self):
        assert type(self.exception_sent) == type(self.expected_exception)


@pytest.mark.parametrize(
    """
    heights, expected_exception
    """,
    [CASE_1, CASE_2, CASE_3, CASE_4],
)
@pytest.mark.should_raise_error_due_to_constrains
def test_should_raise_error_due_to_constrains(heights: List[int], expected_exception):
    test = TestParametersConstraints()
    test.given(heights, expected_exception)
    test.when()
    test.then()
