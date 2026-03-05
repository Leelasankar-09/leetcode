class Solution(object):
    def singleNumber(self, nums):
        res = 0
        for i in range(32):
            cnt = 0
            for x in nums:
                if (x >> i) & 1:
                    cnt += 1
            if cnt % 3:
                res |= (1 << i)
        if res >= 2**31:
            res -= 2**32
        return res