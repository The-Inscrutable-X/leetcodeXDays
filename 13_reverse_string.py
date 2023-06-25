import typing
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def reverse_string(self, s: list[str]) -> bool:
        st = 0
        t = len(s) - 1
        while st < t:
            temp = s[st]
            s[st] = s[t]
            s[t] = temp
            st += 1
            t -= 1
        
            

sol = Solution()
# root = None
listo = ["t", "a", "n", "i"]
sol.reverse_string(listo)
# root.left.left.left = TreeNode(-5)

print(listo)