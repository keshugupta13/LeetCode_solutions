class Solution(object):
    def spiralOrder(self, matrix):
        n = len(matrix)
        m = len(matrix[0])
        ans = []
        top,bottom,left,right = 0,n-1,0,m-1
        while(top<=bottom and left<=right):
            ##traverse right
            for j in range(left,right+1):
                ans.append(matrix[top][j])
            top += 1
            
            #traverse down
            for j in range(top,bottom+1):
                ans.append(matrix[j][right])
            right -= 1
            
            
            ## traverse left
            if top<= bottom:
                
                for j in range(right,left-1,-1):
                    ans.append(matrix[bottom][j])
                bottom -= 1
                
            ## traverse up
            if left <= right:
                for j in range(bottom,top-1,-1):
                    ans.append(matrix[j][left])
                left += 1
            
        return ans
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        