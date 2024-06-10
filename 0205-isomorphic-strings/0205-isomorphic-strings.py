class Solution(object):
    def isIsomorphic(self, str1, str2):
        has1={}
        has2={}
        if len(str1)!=len(str2):
            return False
        for i in range(len(str1)):
            c1 = str1[i]
            c2 = str2[i]
            
            if (c1 in has1 and has1[c1] != c2) or (c2 in has2 and has2[c2] != c1):
                return False
            
           
            has1[c1]=c2
            has2[c2]=c1
           
        return True


        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        