class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        indegree = [0] * numCourses

        for a, b in prerequisites:
            graph[b].append(a) # a <-- b, b should be finished before a
            indegree[a] += 1 

        que = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                que.append(i)

        taken = 0
        while que:
            course = que.popleft()
            taken += 1
            for nei in graph[course]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    que.append(nei)
        
        return taken == numCourses