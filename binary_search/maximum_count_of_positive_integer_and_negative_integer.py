

from typing import List


class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        def first_at_least(target: int) -> int:
            l, r = 0, len(nums)
            while l < r:
                mid = (l + r) // 2
                if nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid
            return l

        neg = first_at_least(0)
        pos = len(nums) - first_at_least(1)
        return max(neg, pos)