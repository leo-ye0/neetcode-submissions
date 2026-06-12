class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # Condition 1: A valid tree must have exactly n - 1 edges
        if len(edges) != n - 1:
            return False

        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        # Condition 2: Check if the graph is fully connected
        visited = set()
        queue = deque([0]) # Start traversing from node 0
        visited.add(0)
        
        while queue:
            node = queue.popleft()
            for neighbor in adj[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
                    
        # If we visited every single node, it's a tree!
        return len(visited) == n