class Solution(object):
    def minimumPushes(self, word):
        arr = [0] * 26
        for i in word:
            arr[ord(i)-ord("a")] += 1
        
        arr.sort()
        count = 0
        minpress = 0
        for i in range(len(arr)-1,-1,-1):
            mul = 0
            if count<8:
                mul = 1
            elif count < 16:
                mul = 2
            elif count < 24:
                mul = 3
            else:
                mul = 4

            val = arr[i] * mul
            minpress += val
            count += 1
        return minpress
                
            





        """
        :type word: str
        :rtype: int
        """
        