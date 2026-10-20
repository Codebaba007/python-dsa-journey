
from collections import deque


class Solution:
    def countStudents(self, students, sandwiches):
        q = deque(students)
        i = 0
        skip = 0

        while q and skip < len(q):
            if q[0] == sandwiches[i]:
                q.popleft()
                i += 1
                skip = 0
            else:
                q.append(q.popleft())
                skip += 1

        return len(q)