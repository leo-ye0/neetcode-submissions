class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach = 0
        target = len(nums) - 1
        
        for i in range(len(nums)):
            if i > max_reach:
                return False
            max_reach = max(max_reach, i + nums[i])
            
            # Optimization: If we can already reach the end, we can exit early!
            if max_reach >= target:
                return True
                
        return max_reach >= target