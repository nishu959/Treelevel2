class btree():
  def __init__(self, data, right = None, left = None):
    self.data = data
    self.right = right
    self.left = left

n = int(input())
preorder = list(map(int, input().split())) 
inorder = list(map(int, input().split())) 

def treeform(preorder, psi, pei, inorder , isi, iei):
  if(isi > iei):
    return None
  
  idx = isi
  while(inorder[idx]!=preorder[psi]):
    idx += 1
    
  tnel = idx - isi
  r = btree(preorder[psi]) 
  
  r.left = treeform(preorder, psi+ 1, psi + tnel, inorder ,isi, idx - 1)
  
  r.right = treeform(preorder, psi+ tnel +1, pei,inorder ,idx+1, iei)
  
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
  

root = treeform(preorder, 0, n-1, inorder, 0, n-1)  

display(root)
