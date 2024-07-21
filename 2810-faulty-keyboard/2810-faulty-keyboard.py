class Solution(object):
    def finalString(self, s):
        ans = ""
        for i in range(len(s)):
            if s[i] != "i":
                ans = ans + s[i]
            else:
                ans = ans[::-1]
        return ans
        """
        :type s: str
        :rtype: str
        """
        