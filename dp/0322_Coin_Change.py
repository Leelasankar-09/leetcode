class Solution(object):
    def coinChange(self, coins, amount):
        coins.sort()
        if amount == 0:
            return 0
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0
        for i in coins:
            for j in range(amount + 1):
                if j - i >= 0:
                    dp[j] = min(dp[j], 1 + dp[j - i])
        if dp[-1] == float("inf"):
            return -1
        print(dp)
        return dp[-1]