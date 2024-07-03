class Solution(object):
    def threeConsecutiveOdds(self, arr):
        count = 0
        n=len(arr)
        for i in range(n):
            if arr[i]%2==0:
                count = 0
            elif arr[i]%2 != 0:
                count += 1
            
            if count == 3:
                return True
            else:
                False
        """
        :type arr: List[int]
        :rtype: bool
        """
        