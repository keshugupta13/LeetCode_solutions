class Solution(object):
    def passThePillow(self, n, time):
        rounds = time // (n-1)
        remainder = time % (n-1)
        ans = 0
        if rounds%2==0:
            ans = 1 + remainder
        else:
            ans = n - remainder

        return ans


        """
        :type n: int
        :type time: int
        :rtype: int
        """
        