class Solution(object):
    def twoSum(self, nums, target):
        rem = {}
        for i in range(len(nums)):
            if nums[i] in rem:
                return [i, rem[nums[i]]]
            else:
                rem[target - nums[i]] = i