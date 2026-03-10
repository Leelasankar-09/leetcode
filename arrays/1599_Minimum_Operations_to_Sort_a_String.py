class Solution(object):
    def minOperations(self, s):
        n = len(s)
        ch = list(s)
        ch1 = list(s)
        ch1.sort()
        if ch == ch1:
            return 0
        if n == 2:
            return -1
        if n == 3:
            if ch[0] <= ch[1]:
                if ch[0] <= ch[2]:
                    return 1
                return 2
            if ch[1] <= ch[2]:
                if ch[0] <= ch[2]:
                    return 1
                return 2
            return 3
        from collections import Counter
        map = Counter(ch)
        small = ch1[0]
        big = ch1[n-1]
        if small == ch[0] or big == ch[n-1]:
            return 1
        if small == ch[n-1] and big == ch[0] and len(map) >= 3 and (map[ch[n-1]] == 1 and map[ch[0]] == 1):
            return 3
        return 2