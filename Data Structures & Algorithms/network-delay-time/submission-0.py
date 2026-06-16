class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Dijkstra−algorithm
        adj = defaultdict(list)
        for u, v, w in times:
            adj[u].append((v, w)) # source -> (target, time)
        # Heap stores tuples of (cumulative_time, current_node)
        min_heap = [(0, k)]
        distances = {}
        while min_heap:
            current_time, node = heapq.heappop(min_heap)
            
            # If we've already found a shorter path to this node, skip processing
            if node in distances:
                continue
                
            # Record the absolute shortest time to reach this node
            distances[node] = current_time
            
            # Explore all outgoing paths to neighbors
            for neighbor, weight in adj[node]:
                if neighbor not in distances:
                    heapq.heappush(min_heap, (current_time + weight, neighbor))
                    
        if len(distances) == n:
            return max(distances.values())
            
        return -1