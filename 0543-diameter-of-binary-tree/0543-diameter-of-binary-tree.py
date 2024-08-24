# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        self.maxi = 0
        self.height(root,self.maxi)
        return self.maxi
        

    def height(self,root,maxi):
        if root is None:
            return 0
        
        lh = self.height(root.left,self.maxi)
        rh = self.height(root.right,self.maxi)
        self.maxi = max(self.maxi, lh + rh)

        return 1 + max(lh,rh)
        