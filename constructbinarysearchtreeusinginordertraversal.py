class btree():
  def __init__(self, data, right=None, left=None):
    self.data = data
    self.right = right
    self.left = left

n = int(input())
inorder = list(map(int, input().split()))

def bstform(inorder, si, ei):
  if(si > ei):
    return None
  
  mid = (si + ei)//2
  
  root = btree(inorder[mid])
  
  root.left = bstform(inorder, si, mid-1)
  
  root.right = bstform(inorder, mid+1, ei)
  
  return root
  

root = bstform(inorder, 0, n-1)


def display(root):
  if(root == None):
    return 
  
  
  
  s = ""
  
  s += str(root.left.data) if (root.left!=None) else "."
  
  s += " -> " + str(root.data) + " <- "
  
  s += str(root.right.data) if (root.right!=None) else "."
  print(s)
  display(root.left)
  display(root.right)
 
 
 
display(root)