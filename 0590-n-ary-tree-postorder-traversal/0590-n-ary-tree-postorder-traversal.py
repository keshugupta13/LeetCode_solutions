"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def solvepostorder(self,root,ans):
        if root is None:
            return
        for child in root.children:
            self.solvepostorder(child,ans)
        ans.append(root.val)

    def postorder(self, root):
        ans = []
        self.solvepostorder(root,ans)
        return ans
        """
        :type root: Node
        :rtype: List[int]
        """
        