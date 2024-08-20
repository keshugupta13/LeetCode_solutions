class Solution(object):
    def isNumber(self, s):
        num, exp, sign, dec = False, False, False, False
        for c in s:
            if '0' <= c <= '9': 
                num = True
            elif c == 'e' or c == 'E':
                if exp or not num: 
                    return False
                exp, num, sign, dec = True, False, False, False
            elif c == '+' or c == '-':
                if sign or num or dec: 
                    return False
                sign = True
            elif c == '.':
                if dec or exp: 
                    return False
                dec = True
            else: 
                return False
        return num