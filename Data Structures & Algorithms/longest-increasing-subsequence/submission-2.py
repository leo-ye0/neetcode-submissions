import bisect
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        sub = []
        for num in nums:
            # Find the index of the first element >= num using binary search
            idx = bisect.bisect_left(sub, num)
            
            # If num is greater than all elements in sub, append it
            if idx == len(sub):
                sub.append(num)
            # Otherwise, replace the existing element at idx with num
            else:
                sub[idx] = num
                
        return len(sub)