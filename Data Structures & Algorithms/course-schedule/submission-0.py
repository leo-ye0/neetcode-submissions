class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        in_degree = [0] * numCourses
        for course, pre in prerequisites:
            adj[pre].append(course)
            in_degree[course] += 1
        # Start with courses that have no prerequisites
        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
        count = 0
        while queue:
            current_pre = queue.popleft()
            count += 1
            for neighbor in adj[current_pre]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        return count == numCourses