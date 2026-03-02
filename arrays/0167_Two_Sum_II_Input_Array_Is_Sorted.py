class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        rem={}
        for i in range(len(nums)):
            if  nums[i] in rem:
                return [i,rem[nums[i]]]
            else:
                rem[target-nums[i]]=i