# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        self.best = 0

        def height(root) -> int:
            if not root: return 0
            
            heightLeft = height(root.left)
            
            heightRight = height(root.right)

            self.best = max(self.best, heightLeft + heightRight)   # job 1: update the best diameter
            return 1 + max(heightLeft, heightRight)                # job 2: report my height to my parent
        

        height(root)

        return self.best
        

    

