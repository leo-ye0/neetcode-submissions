class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = len(nums) # Start with n
        
        # XOR every index and every value together
        for i, num in enumerate(nums):
            res ^= i ^ num
            
        return res