# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def smallest(self,root,ans):
        if root is None:
            return
        self.smallest(root.left,ans)
        ans.append(root.val)
        self.smallest(root.right,ans)
    def kthSmallest(self, root, k):
        ans = []
        self.smallest(root,ans)
        n = len(ans)
        if k > n:
            return -1
        return ans[k-1]
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        