class btree():
  def __init__(self, data, right = None, left = None):
    self.data = data
    self.right = right
    self.left = left
   
class pair():
  def __init__(self, node, state):
    self.node = node
    self.state = state
    
class hl():
  def __init__(self, n, hl):
    self.n = n 
    self.hl = hl

    
n = int(input())
a = []
for i in range(n):
  a.append(int(input()))
 
root = btree(a[0])
stack = []
stack.append(pair(root,1)) 

idx = 0

 
while(len(stack)>0):
  top = stack[-1]
  if(top.state ==1):
    idx += 1
    if(a[idx]!=-1):
      t = btree(a[idx])
      top.node.left = t
      p = pair(t, 1)
      stack.append(p)
    else:
      top.node.left = None
    
    top.state += 1
    
  elif(top.state == 2):
    idx += 1
    if(a[idx]!=-1):
      t = btree(a[idx])
      top.node.right = t
      p = pair(t, 1)
      stack.append(p)
    else:
      top.node.right = None
    
    top.state += 1
  
  
  else:
    stack.pop()
   
minlvl = 0
maxlvl = 0  

def verticalorder(root):
  global minlvl, maxlvl
  l = []
  l.append(hl(root, 0))
  ans = {}
  
  while(len(l)>0):
    size = len(l) 
    while(size>0):
      rn = l.pop(0)
      
      minlvl = min(rn.hl,minlvl)
      maxlvl = max(rn.hl,maxlvl)
      
      if rn.hl not in ans:
        ans[rn.hl] = [rn.n.data]
      else:
        p = ans[rn.hl]
        p.append(rn.n.data)
        ans[rn.hl] = p
        
      if(rn.n.left!=None):
        l.append(hl(rn.n.left,rn.hl-1))
      if(rn.n.right!=None):
        l.append(hl(rn.n.right,rn.hl+1)) 
      size-=1
  
  return ans
  

ans = verticalorder(root)

count = maxlvl - minlvl
for i in range(count+1):
  print(i,"->", *ans[minlvl]) 
  minlvl += 1


  
  
