"""
LeetCode 1. Two Sum

Difficulty: Easy
Topic: Arrays, Hash Map

Time Complexity: O(n)
Space Complexity: O(n)

Day: 1
"""

class Solution:
    def twoSum(self, nums, target):
        seen = {}

        for i, num in enumerate(nums):
            complement = target - num

            if complement in seen:
                return [seen[complement], i]

            seen[num] = i