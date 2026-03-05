class Solution:
    def makeLargestSpecial(self, s):
        cnt = 0
        list = []
        j = 0
        for i in range(len(s)):
            if s[i] == '1':
                cnt += 1
            else:
                cnt -= 1
            if cnt == 0:
                list.append('1' + self.makeLargestSpecial(s[j+1:i]) + '0')
                j = i + 1
        list.sort(reverse=True)
        return "".join(list)