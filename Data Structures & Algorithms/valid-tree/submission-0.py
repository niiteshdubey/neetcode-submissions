class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) >= n:
            return False
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        visited = set()

        def dfs(curr, par):
            if curr in visited:
                return False
            
            visited.add(curr)
            for nbr in adj[curr]:
                if nbr != par and nbr not in visited:
                    if dfs(nbr, curr) == False:
                        return False
            
            return True

        
        return dfs(0, -1) and len(visited) == n