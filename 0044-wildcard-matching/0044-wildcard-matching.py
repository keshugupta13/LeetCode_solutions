class Solution(object):
    def isMatch(self, s, p):
        flag = False
        c1 = list(s)
        c2 = list(p)
        
        if c1 and c2[0] == "*":
            return True
            flag = True

        if len(c1) != len(c2) and c2[0] != "*":
            return False
            flag = True

        if not flag:
            for i in range(len(c1)):
                if c2[i] == "?":
                    continue
                if c1[i] != c2[i]:
                    return False
                    flag = False
                    break
            else:
                return True