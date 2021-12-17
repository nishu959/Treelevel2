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
  
ele =int(input())
 
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
 
  
  
def ntrpath(node, ele):
  if node ==None:
    return None
 
  if(node.data ==ele):
    ans = []
    ans.append(node.data)
    return ans
  
  ansleft = ntrpath(node.left, ele) 
  if(ansleft!=None):
    ansleft.append(node.data) 
    return ansleft
    
  ansright = ntrpath(node.right, ele)
  if(ansright!=None):
    ansright.append(node.data)
    return ansright
  
  return None
  

res = ntrpath(root, ele)
if(res==None):
  print("")
else:
  print(*res)