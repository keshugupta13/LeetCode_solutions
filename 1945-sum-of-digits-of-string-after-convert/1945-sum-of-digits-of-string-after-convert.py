class Solution(object):
    def getLucky(self, s, k):
        str1 = ""
        n = len(s)
        for i in s:
            str1 += str(ord(i)-ord('a')+1)

        while k > 0:
            temp = 0
            for x in str1:
                temp += int(x)
            str1 = str(temp)
            k -= 1
        return int(str1)
            

