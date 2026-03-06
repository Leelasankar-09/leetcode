class Solution(object):
    def sortByBits(self, arr):
        n = len(arr)
        x = [[0, 0] for _ in range(n)]
        for i in range(n):
            x[i][0] = arr[i]
            y = arr[i]
            cnt = 0
            while y > 0:
                cnt += y & 1
                y >>= 1
            x[i][1] = cnt
        for i in range(n):
            for j in range(i + 1, n):
                y = x[i][1] - x[j][1]
                if y > 0 or (y == 0 and x[i][0] > x[j][0]):
                    temp = x[i]
                    x[i] = x[j]
                    x[j] = temp
        for i in range(n):
            arr[i] = x[i][0]
        return arr