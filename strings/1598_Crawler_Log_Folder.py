class Solution(object):
    def minOperations(self, logs):
        """
        :type logs: List[str]
        :rtype: int
        """
        cnt = 0
        for s in logs:
            if s[0] == '.':
                if s[1] == '.':
                    if cnt > 0:
                        cnt -= 1
            else:
                cnt += 1
        return cnt