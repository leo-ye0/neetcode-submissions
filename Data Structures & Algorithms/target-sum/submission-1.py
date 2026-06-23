class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total_sum = sum(nums)
        
        if abs(target) > total_sum:
            return 0
            
        n = len(nums)
        # Total possible sum range is from -total_sum to +total_sum
        # Size of the column axis is 2 * total_sum + 1
        num_columns = 2 * total_sum + 1
        offset = total_sum
        
        # dp[i][j] = number of ways to reach sum (j - offset) using the first i numbers
        dp = [[0] * num_columns for _ in range(n + 1)]
        
        # Base case: 1 way to reach a sum of 0 with 0 elements
        dp[0][0 + offset] = 1
        
        for i in range(1, n + 1):
            num = nums[i - 1]
            for j in range(num_columns):
                if dp[i - 1][j] > 0:
                    # Choice 1: Add the current number (+)
                    if j + num < num_columns:
                        dp[i][j + num] += dp[i - 1][j]
                    
                    # Choice 2: Subtract the current number (-)
                    if j - num >= 0:
                        dp[i][j - num] += dp[i - 1][j]
                        
        return dp[n][target + offset]