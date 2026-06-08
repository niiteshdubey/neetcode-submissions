# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def util(self, root):
        if not root:
            return
        temp = root.left
        root.left = root.right
        root.right = temp
        self.util(root.left)
        self.util(root.right)
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.util(root)
        return root
        