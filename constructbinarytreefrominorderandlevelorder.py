class btree():
  def __init__(self, data, right = None, left = None):
    self.data = data
    self.right = right
    self.left = left

n = int(input()) 
inorder = list(map(int, input().split())) 
levelorder = list(map(int, input().split()))


def treeform(inorder, isi, iei, levelorder):
  if(isi > iei):
    return None   

  root = btree(levelorder[0]) 
  if(len(levelorder)==1):
    return root
  
  idx = isi
  s = set()
  while(inorder[idx] != levelorder[0]):
    s.add(inorder[idx])
    idx += 1
  
  lols = []
  lors = []
  for i in range(1,len(levelorder)):
    if levelorder[i] in s and len(s)!=0:
      s.remove(levelorder[i])
      lols.append(levelorder[i])
    
    else:
      lors.append(levelorder[i])
      
  root.left =treeform(inorder, isi, idx-1, lols)
    
  root.right =treeform(inorder, idx+1, iei, lors)
    
  return root
 

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
  

root = treeform(inorder, 0, n-1, levelorder)  

display(root)
