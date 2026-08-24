from collections import Counter

class Solution:
    def intersect(self, num1, num2):
        count = Counter(num1)
        result = []

        for num in num2:
            if count[num] > 0:
                result.append(num)
                count[num] -= 1

        return result        