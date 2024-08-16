class Solution(object):
    def lemonadeChange(self, bills):
        d = {}
        d[5] = 0
        d[10] = 0
        d[15] = 0
        for bill in bills:
            if bill == 5:
                d[bill] += 1
            
            elif bill == 10:
                if d[5] == 0:
                    return False
                d[10] += 1
                d[5] -= 1

            elif bill == 20:
                if d[10] > 0 and d[5] > 0:
                    d[10] -= 1
                    d[5]  -= 1
                else:
                    if d[5] >= 3:
                        d[5] -= 3
                    else:
                        return False
        return True
