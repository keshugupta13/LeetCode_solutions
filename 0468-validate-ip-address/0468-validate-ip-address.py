class Solution(object):
    def validIPAddress(self, IP):
        if "." in IP:
            segments = IP.split(".")
            if len(segments) != 4:
                return "Neither"
            for i in segments:
                if not i.isdigit() or not 0 <= int(i) <= 255 or (i[0] == "0" and len(i) > 1):
                    return "Neither"
                
            return "IPv4"
        elif ":" in IP:
            segments = IP.split(":")
            if len(segments) != 8:
                return "Neither"
            for i in segments:
                if not i or len(i) > 4 or not all(c in string.hexdigits for c in i):
                    return "Neither"
            return "IPv6"
        return "Neither"



        


        """
        :type queryIP: str
        :rtype: str
        """
        