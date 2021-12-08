class btree():
  def __init__(self, data, right = None, left = None):
    self.data = data
    self.right = right
    self.left = left
   
class pair():
  def __init__(self, node, state):
    self.node = node
    self.state = state


class robber():
  def __init__(self, withrob, withoutrob):
    self.withrob = withrob
    self.withoutrob = withoutrob
    
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
  
 

def houserobber(root):
  if(root ==None):
    return robber(0,0)
  a = houserobber(root.left)
  b = houserobber(root.right)
  rob = a.withoutrob + b.withoutrob + root.data
  notrob = max(a.withoutrob,a.withrob) + max(b.withrob,b.withoutrob)
  obj = robber(rob, notrob)
  return obj
  
ans = houserobber(root)
print(max(ans.withrob,ans.withoutrob))
