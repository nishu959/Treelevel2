class btree():
  def __init__(self, data, right = None, left = None):
    self.data = data
    self.right = right
    self.left = left
   
class pair():
  def __init__(self, node, state):
    self.node = node
    self.state = state


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
 
   

def diagonal(root):
  l = []
  ans = []
  l.append(root) 
  while(len(l)>0):
    size = len(l)
    smallans = []
    while(size>0):
      rn = l.pop(0)
      while(rn!=None):
        smallans.append(rn.data)
        if rn.left!=None:
          l.append(rn.left)
        rn = rn.right
    
      size -= 1
    
    ans.append(smallans)
  return ans
  
p = diagonal(root)

for i in range(len(p)):
  print(i, "->", *p[i])
 
