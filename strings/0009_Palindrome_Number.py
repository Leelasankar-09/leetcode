class Solution(object):
    def isPalindrome(self, x):
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        r_h = 0
        while x > r_h:
            r_h = r_h * 10 + x % 10
            x //= 10
        return x == r_h or x == r_h // 10
