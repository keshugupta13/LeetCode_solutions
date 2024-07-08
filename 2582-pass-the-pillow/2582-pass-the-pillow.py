class Solution(object):
    def passThePillow(self, n, time):
        i = 1
        F = True
        while (time>0):
            if(F==True):
                i += 1
                time -= 1

                if (i == n):
                    F = False
            else:
                i -= 1
                time -= 1

                if (i==1):
                    F = True
        return i

        """
        :type n: int
        :type time: int
        :rtype: int
        """
        