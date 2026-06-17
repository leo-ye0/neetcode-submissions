class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(list)
        for u, v, price in flights:
            adj[u].append((v, price))
            
        # Min-Heap stores: (total_cost, current_airport, stops_remaining)
        min_heap = [(0, src, k + 1)]
        
        # Track the maximum remaining stops seen for each airport to prune bad paths
        stops_recorded = {}
        
        while min_heap:
            cost, u, stops_left = heapq.heappop(min_heap)
            
            if u == dst:
                return cost
                
            if stops_left > 0:
                # If we've been to airport 'u' before with MORE or EQUAL stops remaining,
                # this current path is worse or redundant. Skip it.
                if u in stops_recorded and stops_recorded[u] >= stops_left:
                    continue
                stops_recorded[u] = stops_left
                
                for v, price in adj[u]:
                    heapq.heappush(min_heap, (cost + price, v, stops_left - 1))
                    
        return -1