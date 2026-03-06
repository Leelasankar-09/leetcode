class Solution(object):
    def checkOnesSegment(self, s):
        yes = False
        cnt = 0
        for ch in s:
            if ch == '1' and yes:
                return False
            if ch == '1':
                cnt += 1
            elif cnt > 0:
                yes = True
                cnt = 0
        return True