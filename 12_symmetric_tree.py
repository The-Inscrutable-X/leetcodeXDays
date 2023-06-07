import typing
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        from collections import deque
        myQueue: list[tuple] = deque()
        Layer: list = []
        if root != None:
            myQueue.append((root, 0))
        else:
            return True
        while myQueue:
            cur, layer = myQueue.popleft()
            Layer.append((cur.val, layer))
            if cur.val == -101:
                continue
            if cur.left != None:
                myQueue.append((cur.left, layer + 1))
            else:
                myQueue.append((TreeNode(-101), layer + 1))

            if cur.right != None:
                myQueue.append((cur.right, layer + 1))
            else:
                myQueue.append((TreeNode(-101), layer + 1))
        print(Layer)
        layerCounter = 0
        curLayer = []
        for i,x in enumerate(Layer):
            print(curLayer, layerCounter)
            if x[1] == layerCounter:
                curLayer.append(x)
            else:
                for j in range(len(curLayer)//2):
                    if curLayer[j] == curLayer[-j-1]:
                        pass
                    else:
                        return False
                layerCounter = x[1]
                curLayer = [x]
        for j in range(len(curLayer)//2):
                    if curLayer[j] == curLayer[-j-1]:
                        pass
                    else:
                        return False
        return True
            

sol = Solution()
# root = None
root = TreeNode(1)
root.right = TreeNode(2)
root.right.right = TreeNode(-5)
root.left = TreeNode(2)
root.left.left = TreeNode(-5)
# root.left.left.left = TreeNode(-5)
outlist = sol.isSymmetric(root)
print(outlist)