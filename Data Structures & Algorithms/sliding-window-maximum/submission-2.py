class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Heap stores (-value, index)
        max_heap = []
        res = []
        
        for i in range(len(nums)):
            heapq.heappush(max_heap, (-nums[i], i))
            if i >= k - 1:
                # While the top of the heap is outside the current window
                while max_heap[0][1] <= i - k:
                    heapq.heappop(max_heap)
                
                # The top is now the max for the current window
                res.append(-max_heap[0][0])
                
        return res