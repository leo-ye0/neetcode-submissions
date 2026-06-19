class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums: return 0
        global_max=nums[0]
        local_max=nums[0]
        local_min=nums[0]
        for num in nums[1:]:
            if num<0:
                local_max,local_min=local_min,local_max
            local_max=max(num,local_max*num)
            local_min=min(num,local_min*num)
            global_max=max(global_max,local_max)
        return global_max