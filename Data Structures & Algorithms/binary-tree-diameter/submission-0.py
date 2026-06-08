# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def depth(self, root) -> int:
        if not root:
            return 0
        return 1 + max(self.depth(root.left), self.depth(root.right))

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        self.max_depth = 0

        def util(temp):
            if not temp: return
            self.max_depth = max(self.max_depth, self.depth(temp.left) + self.depth(temp.right))
            util(temp.left)
            util(temp.right)
        util(root)
        return self.max_depth
