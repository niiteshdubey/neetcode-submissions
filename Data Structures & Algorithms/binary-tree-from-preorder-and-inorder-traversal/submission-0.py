# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inIdMap = {num: idx for idx, num in enumerate(inorder)}

        start = 0
        def recur(lo, hi):
            if lo > hi:
                return None
            
            nonlocal start
            val = preorder[start]
            start += 1
            root = TreeNode(val)
            mid = inIdMap[val]
            root.left = recur(lo, mid - 1)
            root.right = recur(mid + 1, hi)
            return root
        return recur(0, len(inorder) - 1)
            

