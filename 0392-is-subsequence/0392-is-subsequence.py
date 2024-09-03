class Solution(object):
    def isSubsequence(self, s, t):
        first = 0
        second = 0
        n = len(s)
        m = len(t)
        while first < n and second < m:
            if s[first] == t[second]:
                first += 1
            second += 1
        return first == n
        
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        