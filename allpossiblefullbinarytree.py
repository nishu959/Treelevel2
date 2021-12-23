# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        return self.helper(n) 
    def helper(self,n):   
        if(n==1):
            l = set() 
            l.add(TreeNode(0))
            return l
        
        result = set() 
        for i in range(1, n, 2):
            leftlist = self.helper(i)
            rightlist = self.helper(n-i-1)
    
            for a in leftlist:
                for b in rightlist:
                    root = TreeNode(0)
                    root.left = a
                    root.right = b
                    result.add(root)
        
        return result
