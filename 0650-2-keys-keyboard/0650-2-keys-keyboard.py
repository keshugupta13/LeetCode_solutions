class Solution(object):
    def minSteps(self, n):
        if n == 1:
            return 0

        count = 0
        factor = 2
        while n > 1:
            while n % factor == 0:
                count += factor
                n //= factor
            factor += 1
        return count
        
            

        """
        :type n: int
        :rtype: int
        """
        