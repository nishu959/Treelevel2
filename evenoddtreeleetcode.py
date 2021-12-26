# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        
        flag = True
        l = []
        l.append(root)
        level = 0
        while(len(l)>0):
            if flag==False:
                break 
            size = len(l)
            mxm = sys.maxsize
            mnm = -sys.maxsize
            while(size>0):
                rem = l.pop(0)
                if level % 2==0:
                    if rem.val % 2==0:
                        flag = False
                        break
                    if rem.val <= mnm:
                        flag = False
                        break
                    mnm = rem.val
                            
                else:
                    if rem.val % 2!=0:
                        flag = False
                        break
                    if rem.val >= mxm:
                        flag = False
                        break
                    mxm = rem.val
                            
                    
                if rem.left != None:
                    l.append(rem.left)
                if rem.right != None:
                    l.append(rem.right)
                
                size -= 1
            
            level += 1
            
        return flag