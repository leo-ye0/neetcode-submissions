class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # kruskal
        n = len(points)
        
        # --- UNION-FIND SETUP ---
        parent = list(range(n))
        
        def find(i):
            if parent[i] == i:
                return i
            parent[i] = find(parent[i]) # Path compression
            return parent[i]
            
        def union(i, j):
            root_i = find(i)
            root_j = find(j)
            if root_i != root_j:
                parent[root_i] = root_j
                return True
            return False
            
        # --- KRUSKAL'S ENGINE ---
        # 1. Collect all possible edges
        all_edges = []
        for i in range(n):
            for j in range(i + 1, n):
                x1, y1 = points[i]
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                all_edges.append((dist, i, j))
                
        # 2. Sort edges by distance (cheapest first)
        all_edges.sort()
        
        total_cost = 0
        edges_used = 0
        
        # 3. Process edges greedily
        for dist, u, v in all_edges:
            # If union returns True, it successfully merged two disconnected groups
            if union(u, v):
                total_cost += dist
                edges_used += 1
                if edges_used == n - 1:
                    break
                    
        return total_cost