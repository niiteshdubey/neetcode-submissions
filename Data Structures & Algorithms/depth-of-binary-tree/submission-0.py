# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(root, dep):
            if not root:
                return dep
            dl = dfs(root.left, 1 + dep)
            dr = dfs(root.right, 1 + dep)
            return max(dl, dr)
        return dfs(root, 0)
