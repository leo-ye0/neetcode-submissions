class MedianFinder:

    def __init__(self):
        # max_heap stores the smaller half
        self.small = [] 
        # min_heap stores the larger half
        self.large = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -num)
        heapq.heappush(self.large, -heapq.heappop(self.small))
        if len(self.large) > len(self.small):
            heapq.heappush(self.small, -heapq.heappop(self.large))

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return float(-self.small[0])
        # If even, return the average of both tops
        return (-self.small[0] + self.large[0]) / 2.0
        