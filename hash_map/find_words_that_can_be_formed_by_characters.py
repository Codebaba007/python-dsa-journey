
class Solution:
    def countCharacters(self, words, chars):
        available = {}

        for c in chars:
            available[c] = available.get(c, 0) + 1

        res = 0

        for word in words:
            required = {}

            for c in word:
                required[c] = required.get(c, 0) + 1

            good = True

            for c in required:
                if required[c] > available.get(c, 0):
                    good = False
                    break

            if good:
                res += len(word)

        return res