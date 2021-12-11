
import sys

class btree():
  def __init__(self, data, right=None, left=None):
    self.data = data
    self.right = right
    self.left = left

n = int(input())
preorder = list(map(int, input().split()))

idx = 0

def bstform(preorder, lr, rr):
  global idx
  
  if(idx >= len(preorder) or preorder[idx]<lr or preorder[idx]>rr):
    return None
   
  root = btree(preorder[idx])
  idx += 1
  
 
  root.left = bstform(preorder, lr, root.data)
  
  root.right = bstform(preorder, root.data, rr)
  
  return root
  

root = bstform(preorder, -sys.maxsize , sys.maxsize)


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