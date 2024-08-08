# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathsum(self,root,sum1,targetsum,prev):
        if root is None:
            if (sum1 == targetsum and prev.left is None and prev.right is None):
                return True
            return False
        else:
            sum1 += root.val
            return self.pathsum(root.left,sum1,targetsum,root) or self.pathsum(root.right,sum1,targetsum,root)

                
    def hasPathSum(self,root,targetSum):
        if root is None:
            return False
        return self.pathsum(root,0,targetSum,None)
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        