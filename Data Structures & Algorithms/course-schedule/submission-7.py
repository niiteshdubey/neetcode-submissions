class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        path = set()
        graph = defaultdict(list)
        for u, v in prerequisites:
            graph[u].append(v)
        
        def dfs(s):
            if s in path:
                return False
            if graph[s] == []:
                return True
            
            path.add(s)
            for nei in graph[s]:
                if not dfs(nei):
                    return False
            path.remove(s)
            graph[s] = []
            return True
        for s in range(numCourses):
            if not dfs(s):
                return False
        return True