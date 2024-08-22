class Solution(object):
    def convertToTitle(self, n):
        string=""
        while n > 0:
            rem = n % 26
            if rem == 0:
                string = 'Z' + string
                n = n // 26 - 1
            else:
                string = chr(64 + rem) + string
                n = n // 26 

        return string
        