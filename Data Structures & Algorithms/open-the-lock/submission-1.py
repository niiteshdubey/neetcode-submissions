class Solution:
    def children(self, lock):
        res = []
        for i in range(4):
            digit = str((int(lock[i]) + 1) % 10)
            res.append(lock[:i] + digit + lock[i+1:])
            digit = str((int(lock[i]) - 1 + 10) % 10) # handle negative cases in mod
            res.append(lock[:i] + digit + lock[i+1:])
        return res
    def openLock(self, deadends: List[str], target: str) -> int:
        start = "0000"
        visited = set(deadends)
        if start in visited:
            return -1
        
        q = deque([(start, 0)])
        visited.add(start)
        
        while q:
            lock, steps = q.popleft()
            if lock == target:
                return steps
            for child in self.children(lock):
                if child not in visited:
                    q.append((child, steps + 1))
                    visited.add(child)
        
        return -1