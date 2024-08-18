class Solution(object):
    def nthUglyNumber(self, n):
        if n == 1:
            return 1  
        arr = []
        i = 1
        count = 1  
        arr.append(1)  

        while count < n:
            i += 1
            if i % 2 == 0 or i % 3 == 0 or i % 5 == 0:
                arr.append(i)
                count += 1

        return arr[-1]
    
        