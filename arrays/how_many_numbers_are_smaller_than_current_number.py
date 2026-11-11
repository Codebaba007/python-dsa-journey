
class Solution:
    def smallerNumbersThanCurrent(self, nums):
        s = sorted(nums)
        mp = {}

        for i, n in enumerate(s):
            if n not in mp:
                mp[n] = i

        res = []

        for n in nums:
            res.append(mp[n])

        return res