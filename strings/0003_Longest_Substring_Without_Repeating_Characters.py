class Solution(object):
    def lengthOfLongestSubstring(self, s):
        best,left,unique=0,0,set()
        for i in range(len(s)):
            if s[i] not in unique:
                best=max(best,i-left+1)
                unique.add(s[i])
            else:
                while s[i] in unique:
                    unique.remove(s[left])
                    left+=1
                unique.add(s[i])
        return best