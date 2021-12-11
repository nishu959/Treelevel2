import sys

class btree():
  def __init__(self, data, right=None, left=None):
    self.data = data
    self.right = right
    self.left = left
    
class pair():
  def __init__(self, par, lb, rb):
    self.par = par
    self.lb = lb
    self.rb = rb

n = int(input())
levelorder = list(map(int, input().split()))

idx = 0
l = []
l.append(pair(None, -sys.maxsize , sys.maxsize))
root = None

while(len(l)!=0 and idx<len(levelorder)):
  a = l.pop(0)
  ele = levelorder[idx]
  if(ele < a.lb or ele > a.rb):
    continue
  
  node = btree(levelorder[idx])
  idx += 1
  if(a.par ==None):
    root = node
  else:
    par = a.par
    if(ele < par.data):
      par.left = node
    else:
      par.right = node
      
  l.append(pair(node, a.lb, ele))   
  l.append(pair(node, ele, a.rb))
    
  
  


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