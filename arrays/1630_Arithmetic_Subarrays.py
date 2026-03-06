class Solution(object):
    def checkArithmeticSubarrays(self, nums, l, r):
        c = [True] * len(l)
        for i in range(len(l)):
            arr = nums[l[i]:r[i]+1]
            arr.sort()
            dif = arr[1] - arr[0]
            for j in range(1, len(arr)):
                if arr[j] - arr[j-1] != dif:
                    c[i] = False
                    break
        return c