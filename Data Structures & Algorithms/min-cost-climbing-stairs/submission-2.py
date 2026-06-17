class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        prev_step = 0        
        two_steps_back = 0   

        for i in range(2, len(cost) + 1):
            current_step_cost = min(prev_step + cost[i - 1], two_steps_back + cost[i - 2])
            two_steps_back = prev_step
            prev_step = current_step_cost

        return prev_step