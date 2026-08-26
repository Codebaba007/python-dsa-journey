class Solution:
    def longestPalindrome(self, s):
        count = {}

        for ch in s:
            if ch in count:
                count[ch] += 1
            else:
                count[ch] = 1

        length = 0
        has_odd = False

        for freq in count.values():
            length += (freq // 2) * 2

            if freq % 2 == 1:
                has_odd = True

        if has_odd:
            length += 1

        return length
