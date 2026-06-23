class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # sum(P) = (target + total_sum)/2
        total_sum = sum(nums)
        # Edge cases: Target is out of bounds or results in a fraction
        if abs(target) > total_sum or (target + total_sum) % 2 != 0:
            return 0
            
        subset_target = (target + total_sum) // 2
        
        # dp[j] stores the number of ways to form a subset sum of j
        dp = [0] * (subset_target + 1)
        dp[0] = 1  # Base case: There is exactly 1 way to make a sum of 0 (empty subset)
        
        for num in nums:
            # Loop backwards to prevent reusing the same number in the same round
            for j in range(subset_target, num - 1, -1):
                dp[j] += dp[j - num]
                
        return dp[subset_target]