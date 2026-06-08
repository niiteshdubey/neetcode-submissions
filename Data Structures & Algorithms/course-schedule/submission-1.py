class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i: [] for i in range(numCourses)}
        for course, prereq in prerequisites:
            preMap[course].append(prereq)
        
        visited = set()
        def detectCycle(node):
            if node in visited:
                return True
            visited.add(node)   # Mark when going forward
            for nbr in preMap[node]:
                if detectCycle(nbr):
                    return True
            visited.remove(node)    # Unmark while coming back
            return False
        
        for i in range(numCourses):
            if detectCycle(i):
                return False
        return True
        
            