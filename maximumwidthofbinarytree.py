class btree():
  def __init__(self, data, right=None, left=None):
    self.data = data
    self.right = right
    self.left = left
   
  

class pair():
  def __init__(self, node, state):
    self.state = state
    self.node = node


n = list(map(str, input().split()))

def btreeform(n, s, root):
  
  root = btree(int(n[0]))
 
  p = pair(root,1)
  s.append(p)
  idx =0
  while(len(s)>0):
    top = s[-1]
    if(top.state == 1):
    
      idx+=1
      if(n[idx]!="null"):
        t = btree(int(n[idx])) 
        top.node.left = t
      
        p = pair(t, 1)
        s.append(p)
      else:
        top.node.left = None
      
      top.state += 1
    
    
    elif(top.state == 2):
      idx+=1
      if(n[idx]!="null"):
        t = btree(int(n[idx]) ,None, None)
        top.node.right = t
      
        p = pair(t, 1)
        s.append(p)
      else:
        top.node.right = None
      
      top.state += 1
     
    else:
      s.pop()


  return root
  
  
root = btreeform(n, [], None)

class width():
  def __init__(self, n, idx):
    self.n = n
    self.idx = idx
  

def levelorder(root):
  s = []
  maxwidth = 0
  s.append(width(root, 0))
  lm = 0
  rm = 0
  while(len(s)>0):
    it = len(s)
    for i in range(it):
      a = s.pop(0)
      if(a.n.left!=None):
        lm = 2 * a.idx + 1
        s.append(width(a.n.left, lm)) 
      if(a.n.right!=None): 
        rm = 2 * a.idx + 2
        s.append(width(a.n.right, rm))
    
    maxwidth = max(rm - lm +1,maxwidth)
  
  
  return maxwidth
  
  
    
  
print(levelorder(root)) 

