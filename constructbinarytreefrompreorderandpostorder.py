class btree():
  def __init__(self, data, right = None, left = None):
    self.data = data
    self.right = right
    self.left = left

n = int(input())
postorder = list(map(int, input().split()))
preorder = list(map(int, input().split())) 
 

def treeform(preorder, psi, pei, postorder , ppsi, ppei):
  if(psi > pei):
    return None
  
  r = btree(preorder[psi])
  if (psi==pei):
    return r
   
  idx = ppsi
  while(postorder[idx]!=preorder[psi+1]):
    idx += 1
  
  tnel = idx - ppsi + 1
  
  
  r.left = treeform(preorder, psi+ 1, psi + tnel, postorder ,ppsi, idx)
  
  r.right = treeform(preorder, psi+ tnel +1, pei, postorder ,idx+1, ppei-1)
  
  return r

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
  

root = treeform(preorder, 0, n-1, postorder, 0, n-1)  

display(root)
