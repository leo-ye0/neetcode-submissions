class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        if total_sum % 2 != 0:
            return False
        target = total_sum // 2
        # dp[i] stores whether a subset sum of i is possible
        dp = [False] * (target + 1)
        dp[0] = True
        for num in nums:
            # Loop backwards to prevent reusing the current 'num'
            for j in range(target, num - 1, -1):
                if dp[j - num]:
                    dp[j] = True
                    
            # Optimization: If we found a way to hit the target, exit early!
            if dp[target]:
                return True
                
        return dp[target]