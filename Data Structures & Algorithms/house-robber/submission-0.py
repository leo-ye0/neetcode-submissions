class Solution:
    def rob(self, nums: List[int]) -> int:
        #max money to rob ends at house i (i is index)
        if not nums:
            return 0
        if len(nums)==1:
            return nums[0]
        N = len(nums)
        opt= [0]*N
        opt[0]=nums[0]
        opt[1]=max(nums[0],nums[1])
        for i in range(2,N):
            opt[i]=max(opt[i-2]+nums[i],opt[i-1])
        return opt[N-1]