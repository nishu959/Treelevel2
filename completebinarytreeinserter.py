# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class CBTInserter:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.nip = None
        self.l = [root]
    
        while True:
            self.nip = self.l.pop(0)
            
            if self.nip.left:
                self.l.append(self.nip.left)
            else:
                break
            
            if self.nip.right:
                self.l.append(self.nip.right)
            else:
                break
        

    def insert(self, val: int) -> int:
        cval = self.nip.val
        if self.nip.left == None:
            self.nip.left = TreeNode(val)
            self.l.append(self.nip.left)
        else:
            self.nip.right = TreeNode(val)
            self.l.append(self.nip.right)
            self.nip = self.l.pop(0)
            
        return cval
        

    def get_root(self) -> Optional[TreeNode]:
        return self.root
        


# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(val)
# param_2 = obj.get_root()