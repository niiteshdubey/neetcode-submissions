# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = float("-inf")
        def recur(node):
            if not node:
                return -10000
            nonlocal max_sum
            left = recur(node.left)
            right = recur(node.right)
            max_sum = max(max_sum, left, right, left + node.val, right + node.val, left + node.val + right, node.val)
            return max(left + node.val, right + node.val, node.val)
        recur(root)
        return int(max_sum)