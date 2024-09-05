class Solution(object):
    def missingRolls(self, rolls, mean, n):
        m = len(rolls)
        sum1 = mean * (n+m)
        for i in range(m):
            sum1 -= rolls[i]

        if sum1 < n or sum1 > 6 * n:
            return []

        avg = sum1//n
        rem = sum1 % n
        res = [1] * n
        for i in range(n):
            res[i] = avg
            if rem > 0:
                res[i] += 1
                rem -= 1
        return res
