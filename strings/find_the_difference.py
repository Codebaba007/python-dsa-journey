
class Solution:
    def findTheDifference(self, s, t):
        count = {}

        for c in s:
            count[c] = count.get(c, 0) + 1

        for c in t:
            if count.get(c, 0) == 0:
                return c

            count[c] -= 1