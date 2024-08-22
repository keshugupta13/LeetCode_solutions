class Solution(object):
    def convertToTitle(self, n):
        string = ""
        while n > 0:
            remainder = n % 26
            if remainder == 0:
                string = 'Z' + string
                n = n // 26 - 1  
            else:
                string = chr(64 + remainder) + string
                n = n // 26
        return string

        