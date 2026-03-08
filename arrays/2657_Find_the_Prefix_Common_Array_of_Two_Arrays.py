class Solution(object):
    def findThePrefixCommonArray(self, A, B):
        n = len(A)
        count = [0] * (n + 1)
        prefixCommon = 0
        ans = [0] * n
        for i in range(n):
            count[A[i]] += 1
            if count[A[i]] == 2:
                prefixCommon += 1
            count[B[i]] += 1
            if count[B[i]] == 2:
                prefixCommon += 1
            ans[i] = prefixCommon
        return ans