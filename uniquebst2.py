# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        return self.helper(1,n)
        
    def helper(self, st, end):   
        if(st>end):
            l = set() 
            l.add(None)
            return l
        
        result = set() 
        for i in range(st, end+1):
            leftlist = self.helper(st, i-1)
            rightlist = self.helper(i+1, end)
    
            for a in leftlist:
                for b in rightlist:
                    root = TreeNode(i)
                    root.left = a
                    root.right = b
                    result.add(root)
        
        return result
