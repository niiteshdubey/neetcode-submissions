# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        bal = True

        def depth(node):
            nonlocal bal
            
            if not node:
                return 0

            ld = depth(node.left)
            rd = depth(node.right)

            if not bal: return 0

            if abs(ld - rd) > 1:
                bal = False
            
            return 1 + max(ld, rd)
        depth(root)
        return bal