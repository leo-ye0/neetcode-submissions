class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        # 1. Sort intervals by their start time
        intervals.sort(key=lambda x: x[0])
        
        # 2. Pair each query with its original index, then sort them by query value
        # This is the "Offline Queries" pattern
        sorted_queries = sorted((q, i) for i, q in enumerate(queries))
        
        ans = [-1] * len(queries)
        min_heap = []  # Elements stored as: (interval_size, right_boundary)
        i = 0  # Pointer to keep track of our position in intervals
        n = len(intervals)
        
        # 3. Sweep through the sorted queries chronologically
        for q, original_idx in sorted_queries:
            
            # Step A: Push all intervals that start at or before our query 'q'
            while i < n and intervals[i][0] <= q:
                left, right = intervals[i][0], intervals[i][1]
                size = right - left + 1
                heapq.heappush(min_heap, (size, right))
                i += 1
                
            # Step B: Prune the heap. Evict any intervals that end BEFORE our query 'q'
            while min_heap and min_heap[0][1] < q:
                heapq.heappop(min_heap)
                
            # Step C: If there are valid intervals left, the top of the Min-Heap
            # is mathematically guaranteed to be the smallest one covering 'q'
            if min_heap:
                ans[original_idx] = min_heap[0][0]
                
        return ans
