class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        #dp[i]=fewest coins to make amount i
        dp=[float('inf')]*(amount+1)
        dp[0]=0

        # for i in range(amount+1):
        #     for j in coins:
        #         if j<=i:
        #             dp[i]=min(dp[i], dp[i-j]+1)
        # return dp[amount] if dp[amount] != float('inf') else -1
        for coin in coins:
            for i in range(coin,amount+1):
                dp[i]=min(dp[i], dp[i-coin]+1)
        return dp[amount] if dp[amount] != float('inf') else -1