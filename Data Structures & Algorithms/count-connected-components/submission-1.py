class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = list(range(n))
        count = n
        
        def find(i):
            if parent[i] == i:
                return i
            parent[i] = find(parent[i]) # Path compression
            return parent[i]
            
        def union(i, j):
            nonlocal count
            root_i, root_j = find(i), find(j)
            if root_i != root_j:
                parent[root_i] = root_j
                count -= 1 # Successfully merged two components
                
        for u, v in edges:
            union(u, v)
            
        return count