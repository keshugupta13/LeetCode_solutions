class Solution(object):
    def construct2DArray(self, original, m, n):
        if m * n != len(original):
            return []
        
        res = [[0] * n for _ in range(m)]  
        for i in range(len(original)):
            res[i // n][i % n] = original[i]  
        
        return res
