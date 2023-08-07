from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val)


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        right = self.maxDepth(root.right)
        left = self.maxDepth(root.left)
        return max(right, left) + 1


root = TreeNode(val=3)
root.left = TreeNode(val=9)
right = TreeNode(val=20)
right.left = TreeNode(val=15)
right.right = TreeNode(val=7)
root.right = right

s = Solution()
print(s.maxDepth(root))
