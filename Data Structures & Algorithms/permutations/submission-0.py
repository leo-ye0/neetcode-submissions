class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        used = set()
        def backtrack(curr):
            if len(curr) == len(nums):
                ans.append(curr[:])
                return

            for num in nums:
                if num not in used:
                    used.add(num)
                    curr.append(num)
                    
                    backtrack(curr)
                    
                    # Undo everything (Backtrack)
                    curr.pop()
                    used.remove(num)
        
        backtrack([])
        return ans