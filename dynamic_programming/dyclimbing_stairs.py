

class Solution:
    def climbStairs(self, n):
        if n <= 2:
            return n

        two_steps_before = 1
        one_step_before = 2

        for _ in range(3, n + 1):
            current = one_step_before + two_steps_before

            two_steps_before = one_step_before
            one_step_before = current

        return one_step_before