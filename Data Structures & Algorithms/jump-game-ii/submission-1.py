class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        current_end = 0
        farthest = 0
        
        # We iterate to len(nums) - 1 because we don't need to jump FROM the last index
        for i in range(len(nums) - 1):
            # Update the farthest we can reach from anywhere in the current window
            farthest = max(farthest, i + nums[i])
            
            # If we have reached the end of the current jump "level"
            if i == current_end:
                jumps += 1
                current_end = farthest
                
                # Optional early exit: if we can already reach the end
                if current_end >= len(nums) - 1:
                    break
                    
        return jumps