class Solution(object):
    def chalkReplacer(self, chalk, k):
        n = len(chalk)
        total = sum(chalk)
        mod = k % total
        for i in range(n):
            if chalk[i] > mod:
                return i
            mod -= chalk[i]
    
        


        """
        :type chalk: List[int]
        :type k: int
        :rtype: int
        """
        