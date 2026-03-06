class Solution:
    def numSteps(self, s: str) -> int:
        ans = 0
        c = 0
        for i in range(len(s) - 1, 0, -1):
            if ((ord(s[i]) & 1) + c) == 1:
                ans += 2
                c = 1
            else:
                ans += 1
        return ans + c