class Solution(object):
    def findTheWinner(self, n, k):
        def solve(n,k):
            if n == 1:
                return 0
            else:
                return (solve(n-1,k) + k) % n
        return solve(n,k) + 1
        



        """
        :type n: int
        :type k: int
        :rtype: int
        """
        