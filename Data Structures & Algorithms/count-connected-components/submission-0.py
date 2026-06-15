class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        visited = set()
        count = 0
        
        def dfs(node):
            for neighbor in adj[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    dfs(neighbor)
                    
        for i in range(n):
            if i not in visited:
                count += 1
                visited.add(i)
                dfs(i) # Mark the entire component as visited
                
        return count