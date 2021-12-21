import sys

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
a, b = map(int, input().split())



def btreeform(n, s, root):
  root = btree(int(n[0])) 
  p = pair(root,1)
  s.append(p)
  idx =0
  while(len(s)>0 and idx<len(n)-1):
    
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

result = None

def lca(node, a, b):
  global result
  if node == None:
    return False
    
  selfans = ((node.data == a) or (node.data==b))
 
  left = lca(node.left, a, b)
  if(result!=None):
    return True
    
  right = lca(node.right, a, b)
  if(result!=None):
    return True
    
  if((left and right) or (right and selfans) or(left and selfans)):
    result = node
    
  return selfans or left or right
  
lca(root, a, b)
if(result==None):
  print("null")
else:
  print(result.data)
  