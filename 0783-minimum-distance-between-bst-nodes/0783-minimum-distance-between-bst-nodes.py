# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorder(self,root,res):
        if not root:
            return 
        self.inorder(root.left,res)
        res.append(root.val)
        self.inorder(root.right,res)
        
    def minDiffInBST(self, root):
        res =[]
        self.inorder(root,res)
        ans = 1000
        for i in range(1,len(res)):
            value = res[i] - res[i-1]
            ans = min(ans,value)
        return ans

        
