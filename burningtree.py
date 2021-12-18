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
  
  
ele= int(input())
  
 
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
    
maxtime = 0
   
def kdown(r, block, time):
  global maxtime
  
  if(r==None or block ==r):
    return 
  
  maxtime = max(maxtime,time) 
  
  kdown(r.left, block,time+1) 
  kdown(r.right, block,time+1)
  
def ntrpath(node, ele):
  if node ==None:
    return -1
 
  if(node.data ==ele):
    kdown(node, None, 0)
    return 1
  
  la = ntrpath(node.left, ele)
  ra = ntrpath(node.right, ele)
  
  if(la != -1):
    kdown(node, node.left,la )
    return la+1
  
  if( ra!=-1):
    kdown(node, node.right, ra)
    return ra+1
  
  
  return -1
  

ntrpath(root, ele)
print(maxtime)