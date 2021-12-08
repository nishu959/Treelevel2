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
   
  
cam = 0

def cameras(root):
  global cam
  if(root ==None):
    return 1
  lc = cameras(root.left)
  rc = cameras(root.right)
  
  if(lc==-1 or rc ==-1):
    cam += 1
    return 0
   
  if(lc==0 or rc ==0):
    return 1
    
  return -1
  
 
a = cameras(root)
if(a==-1):
  print(cam+1)
else:
  print(cam)
 
  