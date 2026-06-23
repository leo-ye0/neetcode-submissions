class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        hold = -prices[0]
        sold = 0
        rest = 0
        
        for i in range(1, len(prices)):
            # 1. Store yesterday's values before they get overwritten
            prev_hold = hold
            prev_sold = sold
            prev_rest = rest
            
            # 2. Calculate today's state values based on yesterday's states
            hold = max(prev_hold, prev_rest - prices[i])
            sold = prev_hold + prices[i]
            rest = max(prev_rest, prev_sold)
            
        # The ultimate maximum profit must end with no stock in hand (sold or resting)
        return max(sold, rest)