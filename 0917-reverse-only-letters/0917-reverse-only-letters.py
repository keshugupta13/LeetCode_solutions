class Solution(object):
    def reverseOnlyLetters(self, s):
        def is_alpha(c):
            return ('a' <= c <= 'z') or ('A' <= c <= 'Z')
        
        start = 0
        end = len(s) - 1
        s = list(s)
        
        while start < end:
            if is_alpha(s[start]) and is_alpha(s[end]):
                s[start], s[end] = s[end], s[start]
                start += 1
                end -= 1
            elif is_alpha(s[start]) and not is_alpha(s[end]):
                end -= 1
            elif not is_alpha(s[start]) and is_alpha(s[end]):
                start += 1
            else:
                start += 1
                end -= 1
        
        return "".join(s)

        
            


