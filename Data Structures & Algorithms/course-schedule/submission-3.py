class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        indegree = [0] * numCourses
        q = deque()

        for u, v in prerequisites:
            graph[u].append(v)
            indegree[v] += 1

        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        
        finished = 0
        while q:
            curr = q.popleft()
            finished += 1
            for n in graph[curr]:
                indegree[n] -= 1
                if indegree[n] == 0:
                    q.append(n)
        
        if finished == numCourses:
            return True
        return False