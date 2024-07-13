class Solution(object):
    def findTheWinner(self, n, k):
        list1 = []
        for i in range(n):
            list1.append(i)

        index = 0  
        while len(list1) > 1:
            index = (index + (k - 1)) % len(list1)
            list1.pop(index)  
        return list1[0] +1


        """
        :type n: int
        :type k: int
        :rtype: int
        """
        