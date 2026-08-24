class Solution:
    def canConstruct(self, ransomNote, magazine):
        if len(ransomNote) > len(magazine):
            return False

        count = {}

        for ch in magazine:
            count[ch] = count.get(ch, 0) + 1

        for ch in ransomNote:
            if count.get(ch, 0) == 0:
                return False

            count[ch] -= 1

        return True