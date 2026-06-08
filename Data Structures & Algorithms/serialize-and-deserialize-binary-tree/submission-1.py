# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return "N"
        res = []
        que = deque([root])
        while que:
            node = que.popleft()
            if not node:
                res.append("N")
            else:
                res.append(str(node.val))
                que.append(node.left)
                que.append(node.right)
        return ",".join(res)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals = data.split(",")
        if vals[0] == "N":
            return None
        root = TreeNode(vals[0])
        que = deque([root])
        start = 1
        while que:
            node = que.popleft()
            if vals[start] != "N":
                node.left = TreeNode(vals[start])
                que.append(node.left)
            start += 1
            if vals[start] != "N":
                node.right = TreeNode(vals[start])
                que.append(node.right)
            start += 1
        return root
            
            





