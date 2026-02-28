class Solution(object):
    def buildArray(self, nums):
        an=[]
        for i in range(len(nums)):
            an.append(nums[nums[i]])
        return an
        