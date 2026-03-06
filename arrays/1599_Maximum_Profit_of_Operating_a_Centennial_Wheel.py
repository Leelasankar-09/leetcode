class Solution(object):
    def minOperationsMaxProfit(self, customers, boardingCost, runningCost):
        n = len(customers)
        wait = 0
        pro = 0
        max = 0
        cnt = 1
        ans = -1
        arr = [0] * n
        for i in range(n):
            wait += customers[i]
            if wait <= 4:
                pro += boardingCost * wait
                wait = 0
            else:
                pro += boardingCost * 4
                wait -= 4
            pro -= runningCost
            if pro > max:
                max = pro
                ans = cnt
            cnt += 1
        while wait > 0:
            if wait <= 4:
                pro += boardingCost * wait
                wait = 0
            else:
                pro += boardingCost * 4
                wait -= 4
            pro -= runningCost
            if pro > max:
                max = pro
                ans = cnt
            cnt += 1
        return ans