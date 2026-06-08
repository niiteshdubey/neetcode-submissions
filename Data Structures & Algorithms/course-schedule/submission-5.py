class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for u, v in prerequisites:
            graph[u].append(v)
        visited = set()

        # DFS to detect cycle
        def dfs(curr):
            if curr in visited:
                return True
            if graph[curr] == []:   # If all courses are finished
                return False
            visited.add(curr)   # Mark while moving ahead
            for nbr in graph[curr]:
                if dfs(nbr):
                    return True
            visited.remove(curr)    # Unmark while coming back
            graph[curr] = []    # All courses at this node are finished. Empty it's list
        
        for i in range(numCourses):
            if dfs(i):
                return False
        return True