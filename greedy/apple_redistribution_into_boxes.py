

from typing import List


class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        total = sum(apple)
        capacity.sort(reverse=True)
        boxes = 0

        for c in capacity:
            total -= c
            boxes += 1
            if total <= 0:
                return boxes

        return boxes