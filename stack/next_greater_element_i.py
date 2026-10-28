

class Solution:
    def nextGreaterElement(self, nums1, nums2):
        st = []
        mp = {}

        for n in nums2:
            while st and n > st[-1]:
                mp[st.pop()] = n

            st.append(n)

        return [mp.get(n, -1) for n in nums1]