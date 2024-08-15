class Solution(object):
    def lemonadeChange(self, bills):
        d = {}
        d[5] = 0
        d[10] = 0
        d[20] = 0
        for b in bills:
            if b == 5:
                d[b] += 1
            elif b == 10:
                if d[5] == 0:
                    return False
                d[10] += 1
                d[5] -= 1
            elif b == 20:
                if d[10] > 0 and d[5] > 0:
                    d[10] -= 1
                    d[5] -= 1
                elif d[5] >= 3:
                    d[5] -= 3
                else:
                    return False

        return True
        