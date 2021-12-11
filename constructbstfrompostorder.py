
import sys

class btree():
  def __init__(self, data, right=None, left=None):
    self.data = data
    self.right = right
    self.left = left

n = int(input())
postorder = list(map(int, input().split()))

idx = n - 1

def bstform(postorder, lr, rr):
  global idx
  
  if(idx < 0 or postorder[idx]<lr or postorder[idx]>rr):
    return None
   
  root = btree(postorder[idx])
  idx -= 1
  
  root.right = bstform(postorder, root.data, rr)
  root.left = bstform(postorder, lr, root.data)
   
  
  
  
  
  return root
  

root = bstform(postorder, -sys.maxsize , sys.maxsize)


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