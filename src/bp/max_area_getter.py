from .domain import Parameters
from typing import Final
from typing import Tuple
from typing import List

DECREMENT: Final = 1
INCREMENT: Final = 1
DEFAULT_MAX_AREA: Final = 0

class MaxAreaGetter:
    def __init__(self):
        pass

    def run(self, parameters: Parameters) -> int:
        heights = parameters.heights
        max_area_found = DEFAULT_MAX_AREA
        left_index = 0
        right_index = len(heights) - DECREMENT
        while left_index < right_index:
            width = right_index - left_index
            minimum_height = min(heights[left_index], heights[right_index])
            area = self._calculate_area(width, minimum_height)
            if area > max_area_found:
                max_area_found = area
            left_index, right_index = self._calculate_new_indexes(heights, left_index, right_index)
        return max_area_found

    def _calculate_new_indexes(self, heights: List[int], left_index: int, right_index: int) -> Tuple[int, int]:
        if heights[left_index] <= heights[right_index]:
            left_index += INCREMENT
        else:
            right_index -= DECREMENT
        return left_index, right_index

    def _calculate_area(self, width: int, height: int) -> int:
        area = height*width
        return area