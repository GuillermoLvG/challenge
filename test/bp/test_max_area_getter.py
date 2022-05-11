import pytest
from bp.max_area_getter import MaxAreaGetter
from bp.domain import Parameters
from typing import Final
from typing import List

CASE_1: Final = ([1,1], 1)
CASE_2: Final = ([1,8,6,2,5,4,8,3,7], 49)

# from bp.domain import MAX_HEIGHTS, MIN_HEIGHTS, MIN_HEIGHT_VALUE, MAX_HEIGHT_VALUE
# EXTRA_VALUES_IN_HEIGHTS: Final = 1
# REMOVED_VALUES_FROM_HEIGHTS: Final = 1
# DECREMENT: Final = 1
# INCREMENT: Final = 1
# CASE_1: Final = [1]
# CASE_3: Final = [1] * MAX_HEIGHTS + EXTRA_VALUES_IN_HEIGHTS
# CASE_4: Final = [1] * MIN_HEIGHTS - REMOVED_VALUES_FROM_HEIGHTS
# CASE_5: Final = [1, MIN_HEIGHT_VALUE - DECREMENT]
# CASE_6: Final = [1, MAX_HEIGHT_VALUE + INCREMENT]

class TestShouldGetMaximumArea:
    def given(
        self,
        heights: List[int],
        expected_maximum_area: int
    ):
        self.heights = heights
        self.expected_maximum_area = expected_maximum_area
        self.max_area_getter = MaxAreaGetter()

    def when(self):
        self.parameters = Parameters(self.heights)
        self.response = self.max_area_getter.run(self.parameters)

    def then(self):
        assert self.response == self.expected_maximum_area

@pytest.mark.parametrize(
    """
    heights, expected_maximum_area
    """,
    [
        CASE_1,
        CASE_2
    ],
)
@pytest.mark.should_get_max_area
def test_should_get_max_area(
    heights: List[int], expected_maximum_area: int
):
    test = TestShouldGetMaximumArea()
    test.given(heights, expected_maximum_area)
    test.when()
    test.then()
