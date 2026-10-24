
class Solution:
    def findMaxConsecutiveOnes(self, nums):
        cur = 0
        res = 0

        for n in nums:
            if n == 1:
                cur += 1
                res = max(res, cur)
            else:
                cur = 0

        return res