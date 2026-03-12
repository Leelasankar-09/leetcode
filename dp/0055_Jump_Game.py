class Solution(object):
    def canJump(self, nums):
        dp=[False]*len(nums)
        dp[-1]=True
        n=len(nums)
        for i in range(n-2,-1,-1):
            for j in range(nums[i]+1):
                if i+j<n and dp[i]!=True:
                    dp[i]|=dp[i+j]
                else:
                    break
        return dp[0]