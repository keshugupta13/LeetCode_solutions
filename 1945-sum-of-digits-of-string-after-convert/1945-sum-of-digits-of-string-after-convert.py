class Solution(object):
    def getLucky(self, s, k):
        str1 = ""
        n = len(s)
        for i in s:
            str1 += str(ord(i)-ord('a')+1)

        for i in range(k):
            count=0
            for j in range(len(str1)):
                count+=int(str1[j]) 
            str1 = str(count)    
        return int(str1)
