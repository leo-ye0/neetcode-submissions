class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []
        
        for x, y in points:
            dist = x**2 + y**2
            
            # 2. Push onto our max heap (invert the distance with -)
            # Store as a tuple: (-distance, [x, y])
            heapq.heappush(max_heap, (-dist, [x, y]))
            
            if len(max_heap) > k:
                heapq.heappop(max_heap)
                
        # 4. Extract just the physical point coordinates from our remaining top-k tuples
        return [point for dist, point in max_heap]