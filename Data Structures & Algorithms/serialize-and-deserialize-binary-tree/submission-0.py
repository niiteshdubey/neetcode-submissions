# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []
        def recur(node):
            nonlocal res
            if not node:
                res.append("N")
                return
            res.append(str(node.val))
            recur(node.left)
            recur(node.right)
        recur(root)
        return ",".join(res)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        res = data.split(",")
        start = 0
        def recur():
            nonlocal start
            if res[start] == "N":
                start += 1
                return None
            node = TreeNode(res[start])
            start += 1
            node.left = recur()
            node.right = recur()
            return node
        return recur()





















