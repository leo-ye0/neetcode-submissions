class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # m = len(nums)
        # L,R,ans = [0]*m, [0]*m, [0]*m
        # L[0]=1 # L[i] contains the product of all the elements to the left
        # for i in range(1,m):
        #     L[i]=L[i-1]*nums[i-1]
        # R[-1]=1
        # for i in range(m-2, -1, -1):
        #     R[i] = R[i+1]*nums[i+1]
        # for i in range(m):
        #     ans[i]=L[i]*R[i]
        # return ans
        m=len(nums)
        ans=[0]*m
        ans[0]=1
        for i in range(1,m):
            ans[i]=ans[i-1]*nums[i-1]
        R=1
        for i in range(m-1,-1,-1):
            ans[i]*=R
            R*=nums[i]
        return ans
