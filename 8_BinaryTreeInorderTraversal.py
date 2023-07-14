from __future__ import annotations
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal1(self, root: Optional[TreeNode]) -> List[int]:
        outList = []
        self.recurse(root, outList)
        return outList

    def recurse(self, root, outList) -> None:
        if root.left != None:
            self.recurse(root.left, outList)
        outList.append(root.val)
        if root.right != None:
            self.recurse(root.right, outList)

    def inorderTraversal(self, root: Optional[TreeNode]) -> ACoolList[int]:
        
        pass

sol = Solution()
root = TreeNode(1)
root.right = TreeNode(2)
root.left = TreeNode(0)
outlist = sol.inorderTraversal(root)
print(outlist)