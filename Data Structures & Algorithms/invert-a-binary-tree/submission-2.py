# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        
        stack = []
        stack.append(root)

        while stack:
            temp = stack.pop()
            temp.left, temp.right = temp.right, temp.left

            if temp.left:
                stack.append(temp.left)
            if temp.right: stack.append(temp.right)

        return root