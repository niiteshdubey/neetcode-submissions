class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dsu = FindUnion(n)
        for x, y in edges:
            dsu.union(x, y)
        return dsu.cnt
class FindUnion:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.cnt = n
    def find(self, x):
        if self.parent[x] == x:
            return x
        return self.find(self.parent[x])
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            self.cnt -= 1
            self.parent[rootY] = rootX