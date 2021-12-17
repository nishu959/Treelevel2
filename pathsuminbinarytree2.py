

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
  
  
target= int(input())
  
 
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
 
def pathsum(root, target, ans, result):
  if(root ==None):
    return 
 
  if(root.left ==None and root.right==None):
    if target==root.data:
      ansnew = ans.copy()
      ansnew.append(root.data)
      result.append(ansnew)
    return 
     
  ans.append(root.data) 
  pathsum(root.left, target-root.data, ans, result) 
  pathsum(root.right, target-root.data, ans, result)
  ans.pop()
  

result = []
pathsum(root, target, [], result)
if(len(result)==0):
  print("")
else:
  for i in result:
    print(*i)
