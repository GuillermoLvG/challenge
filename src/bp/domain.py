from dataclasses import dataclass
from typing import Final
from typing import List

from .errors import HeightsLengthConstraintFailed
from .errors import HeightValueConstraintFailed

MAX_HEIGHTS: Final = 105
MIN_HEIGHTS: Final = 2
MIN_HEIGHT_VALUE: Final = 0
MAX_HEIGHT_VALUE: Final = 104
ERROR_MESSAGE_MAX_LIMIT: Final = f"More than {MAX_HEIGHTS} heights were given: {{}}"
ERROR_MESSAGE_MIN_LIMIT: Final = f"Less than {MIN_HEIGHTS} heights were given: {{}}"
ERROR_MESSAGE_MAX_HEIGHT_VALUE: Final = (
    f"{{}} is larger than maximum height allowed {MAX_HEIGHT_VALUE}"
)
ERROR_MESSAGE_MIN_HEIGHT_VALUE: Final = (
    f"{{}} is smaller than minimum height allowed {MIN_HEIGHT_VALUE}"
)


class Parameters:
    def __init__(self, heights: List[int]):
        self.heights = heights
        self._validate_constraints()

    def _validate_constraints(self):
        heights_length = len(self.heights)
        if heights_length < MIN_HEIGHTS:
            raise HeightsLengthConstraintFailed(
                ERROR_MESSAGE_MIN_LIMIT.format(heights_length)
            )
        if heights_length > MAX_HEIGHTS:
            raise HeightsLengthConstraintFailed(
                ERROR_MESSAGE_MAX_LIMIT.format(heights_length)
            )
        for height in self.heights:
            if height < MIN_HEIGHT_VALUE:
                raise HeightValueConstraintFailed(
                    ERROR_MESSAGE_MIN_HEIGHT_VALUE.format(height)
                )
            if height > MAX_HEIGHT_VALUE:
                raise HeightValueConstraintFailed(
                    ERROR_MESSAGE_MAX_HEIGHT_VALUE.format(height)
                )
