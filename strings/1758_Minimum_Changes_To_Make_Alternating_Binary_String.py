class Solution(object):
    def minOperations(self, s):
        cnt = 0
        yes = True
        for i in range(len(s)):
            if yes:
                if s[i] != '1':
                    cnt += 1
            else:
                if s[i] != '0':
                    cnt += 1
            yes = not yes
        minimum = cnt
        yes = True
        cnt = 0
        for i in range(len(s)):
            if yes:
                if s[i] == '1':
                    cnt += 1
            else:
                if s[i] == '0':
                    cnt += 1
            yes = not yes
        return min(cnt, minimum)