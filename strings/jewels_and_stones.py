
class Solution:
    def numJewelsInStones(self, jewels, stones):
        j = set(jewels)
        res = 0

        for s in stones:
            if s in j:
                res += 1

        return res