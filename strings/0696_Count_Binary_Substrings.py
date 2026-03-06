class Solution(object):
    def countBinarySubstrings(self, s):
        ans = 0
        prev = 0
        cnt = 1
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                cnt += 1
            else:
                prev = cnt
                cnt = 1
            if cnt <= prev:
                ans += 1
        return ans