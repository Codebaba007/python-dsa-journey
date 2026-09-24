
class Solution:
    def dailyTemperatures(self, temp):
        res = [0] * len(temp)
        st = []

        for i in range(len(temp)):
            while st and temp[i] > temp[st[-1]]:
                p = st.pop()
                res[p] = i - p

            st.append(i)

        return res