
class Solution:
    def sumOfLeftLeaves(self, root):
        if not root:
            return 0

        res = 0

        if root.left:
            if not root.left.left and not root.left.right:
                res += root.left.val
            else:
                res += self.sumOfLeftLeaves(root.left)

        res += self.sumOfLeftLeaves(root.right)

        return res