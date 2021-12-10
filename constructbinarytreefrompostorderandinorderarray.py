class btree():
  def __init__(self, data, right = None, left = None):
    self.data = data
    self.right = right
    self.left = left

n = int(input())
postorder = list(map(int, input().split())) 
inorder = list(map(int, input().split())) 

def treeform(postorder, psi, pei, inorder , isi, iei):
  if(isi > iei):
    return None
  
  idx = isi
  while(inorder[idx]!=postorder[pei]):
    idx += 1
    
  tnel = idx - isi
  r = btree(postorder[pei]) 
  
  r.left = treeform(postorder, psi , psi + tnel- 1, inorder ,isi, idx - 1)
  
  r.right = treeform(postorder, psi+ tnel, pei-1,inorder ,idx+1, iei)
  
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
  

root = treeform(postorder, 0, n-1, inorder, 0, n-1)  

display(root)
