

class Solution:
    def backspaceCompare(self, s, t):
        def get_char(s, i):
            skip = 0

            while i >= 0:
                if s[i] == '#':
                    skip += 1
                elif skip > 0:
                    skip -= 1
                else:
                    return i

                i -= 1

            return i

        i = len(s) - 1
        j = len(t) - 1

        while i >= 0 or j >= 0:
            i = get_char(s, i)
            j = get_char(t, j)

            if i < 0 or j < 0:
                return i == j

            if s[i] != t[j]:
                return False

            i -= 1
            j -= 1

        return True