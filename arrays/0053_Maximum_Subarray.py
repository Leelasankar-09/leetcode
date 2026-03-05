class Solution:
    def maxSubArray(self, nums):
        max = float('-inf')
        sum = 0
        for i in range(len(nums)):
            sum += nums[i]
            max = max if max > sum else sum
            if sum < 0:
                sum = 0
        return max