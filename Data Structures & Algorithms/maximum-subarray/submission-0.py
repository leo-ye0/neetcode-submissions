class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = current_sum = nums[0]
        for i in range(1, len(nums)):
            # Decision: Should we start fresh or keep adding?
            current_sum = max(nums[i], current_sum + nums[i])
            
            # Update the global maximum if the current subarray is better
            max_sum = max(max_sum, current_sum)
            
        return max_sum