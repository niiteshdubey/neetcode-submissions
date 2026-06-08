class Solution:
    def dfs(self, graph, start, visited):
        visited[start] = True
        for nbr in graph[start]:
            if visited[nbr] == False:
                self.dfs(graph, nbr, visited)
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)
        visited = [False] * n
        cnt = 0
        for i in range(n):
            if visited[i] == False:
                self.dfs(graph, i, visited)
                cnt += 1
        return cnt

