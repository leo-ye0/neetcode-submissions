class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()  # Stores indices of elements
        result = []
        
        for i in range(len(nums)):
            # 1. Remove indices that are out of the current window's range
            if dq and dq[0] < i - k + 1:
                dq.popleft()
                
            # 2. Remove indices of smaller elements from the back
            # They can no longer be the maximum for current or future windows
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()
                
            # 3. Add the current element's index to the deque
            dq.append(i)
            
            # 4. Once the first window is fully formed, record the max
            if i >= k - 1:
                result.append(nums[dq[0]])
                
        return result