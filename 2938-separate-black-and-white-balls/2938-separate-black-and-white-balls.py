class Solution(object):
    def minimumSteps(self, s):
        n = len(s)
        last = 0
        swap_count = 0
        for curr in range(n):
            if s[curr] == "0":
                diff = (curr - last)
                swap_count += diff
                last += 1
        return swap_count

        """
        :type s: str
        :rtype: int
        """
        