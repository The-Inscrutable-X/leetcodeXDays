from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        stack: list[int] = [(root, 1)]
        maxRank = 1
        curRank = 1
        while stack:
            root, curRank = stack.pop()
            if curRank > maxRank:
                maxRank = curRank
            if root.right:
                stack.append((root.right, curRank + 1))
            if root.left:
                stack.append((root.left, curRank + 1))
        return maxRank

sol = Solution()
# root = None
root = TreeNode(1)
root.right = TreeNode(2)
root.left = TreeNode(0)
root.left.left = TreeNode(-5)
outlist = sol.maxDepth(root)
print(outlist)