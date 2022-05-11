import pytest
from typing import Final

CASE_1: Final = ([1,1], 1)
CASE_2: Final = ([1,8,6,2,5,4,8,3,7], 49)
HEIGHTS: Final = "heights"
AREA: Final = "area"

@pytest.mark.parametrize(
    "heights, expected_area",
    [CASE_1, CASE_2]
)
def test_endpoint(flask_test_client, heights, expected_area):
    input = {
        HEIGHTS: heights
    }
    response = flask_test_client.post('/tekton/max_area_getter/1.0.0', json=input)
    results = response.get_json()
    assert results[AREA] == expected_area
