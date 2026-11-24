
from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        ans = 0
        curr = head

        while curr:
            ans = ans * 2 + curr.val
            curr = curr.next

        return ans