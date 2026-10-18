
from collections import deque


class Solution:
    def averageOfLevels(self, root):
        res = []
        q = deque([root])

        while q:
            size = len(q)
            total = 0

            for _ in range(size):
                node = q.popleft()
                total += node.val

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)

            res.append(total / size)

        return res