class Solution(object):
    def minExtraChar(self, s, dictionary):
        diction = set(dictionary)
        n = len(s)
        dp = [0] * (n + 1)

        for i in range(1, n + 1):
            dp[i] = dp[i - 1] + 1
            for j in range(i - 1, -1, -1):
                if s[j: i] in diction:
                    dp[i] = min(dp[i], dp[j])

        return dp[n]
        """
        :type s: str
        :type dictionary: List[str]
        :rtype: int
        """
        