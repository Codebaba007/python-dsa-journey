
class Solution:
    def diameterOfBinaryTree(self, root):
        res = [0]

        def depth(node):
            if not node:
                return 0

            l = depth(node.left)
            r = depth(node.right)

            res[0] = max(res[0], l + r)

            return max(l, r) + 1

        depth(root)
        return res[0]