class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])
        return max(self.rob_linear(nums[:-1]), self.rob_linear(nums[1:]))
    def rob_linear(self, nums: list[int]) -> int:
        # This is the space-optimized O(1) linear House Robber engine
        prev2, prev1 = nums[0], max(nums[0], nums[1])

        for i in range(2, len(nums)):
            curr = max(prev1, prev2 + nums[i])
            prev2, prev1 = prev1, curr 
        
        return prev1