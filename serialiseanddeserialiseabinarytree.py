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
        
        
               
        

def serialise(root, ans):
  if(root ==None):
    ans.append("None")
    return 
  
  ans.append(str(root.data))
  
  serialise(root.left, ans)
  serialise(root.right, ans)
  
ans = []
serialise(root, ans)

idx = 0 


def deserialise(ans):
  global idx
  if(idx >= len(ans) or ans[idx]=="None"):
    idx += 1
    return None
  
  Node = btree(ans[idx])
  idx += 1
  Node.left = deserialise(ans)
  
  Node.right = deserialise(ans)
  
  return Node
  



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
   

r = deserialise(ans)
   
display(r)

 
  