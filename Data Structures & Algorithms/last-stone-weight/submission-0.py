class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-stone for stone in stones]
        heapq.heapify(max_heap)
        while len(max_heap) > 1:
            stone1 = heapq.heappop(max_heap)
            stone2 = heapq.heappop(max_heap)

            if stone1 != stone2:
                # Math Trick: stone1 is more negative than stone2. 
                # e.g., -8 - (-7) = -1, which is the correct negative weight!
                remainder = stone1 - stone2
                heapq.heappush(max_heap, remainder)

        return -max_heap[0] if max_heap else 0