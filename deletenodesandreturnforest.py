# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        s = set(to_delete)
        ans = []
        self.helper(root, s, ans)
        if root.val not in s:
            ans.append(root)
        return ans
        
    def helper(self, root, s, ans):
        if root == None:
            return None
        root.left = self.helper(root.left, s, ans)
        root.right = self.helper(root.right, s, ans)
        if root.val in s:
            if root.left!=None:
                ans.append(root.left)
            if root.right!=None:
                ans.append(root.right)
                
            return None
        return root