class Solution(object):
    def minOperations(self, logs):
        level = 0
        for  log in logs:
            if log == "../":
                if level != 0 :
                    level -= 1
            elif log == "./":
                continue
            else:
                level += 1
        return level

        """
        :type logs: List[str]
        :rtype: int
        """
        