# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        inorder = []
        def recur(node, cnt):
            nonlocal inorder
            nonlocal k
            if not node:
                return
            if cnt < k:
                recur(node.left, cnt)
            inorder.append(node.val)
            cnt += 1
            if cnt < k:
                recur(node.right, cnt)
        recur(root, 0)
        return inorder[k - 1]
            