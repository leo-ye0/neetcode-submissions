class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        def backtrack(remain, start, path):
            # Base Case 1: We hit the target exactly
            if remain == 0:
                res.append(list(path))
                return
            
            for i in range(start, len(nums)):
                # PRUNING: If the current number is already bigger than what we need
                if nums[i] > remain:
                    break
                
                # 1. Choose
                path.append(nums[i])
                
                # 2. Explore
                # Note: We pass 'i' (not i + 1) because we can reuse candidates[i]
                backtrack(remain - nums[i], i, path)
                path.pop()

        backtrack(target, 0, [])
        return res