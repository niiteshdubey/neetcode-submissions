"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        otn = {}
        que = deque([node])
        otn[node] = Node(node.val)

        while que:
            curr = que.popleft()
            for nei in curr.neighbors:
                if nei not in otn:
                    otn[nei] = Node(nei.val)
                    que.append(nei)
                otn[curr].neighbors.append(otn[nei])
        return otn[node] 
        