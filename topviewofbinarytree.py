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
    

ans = [0,0]

def width(root, hl, ans):
  if( root == None):
    return 
  
  ans[0] = min(hl, ans[0])
  ans[1] = max(hl, ans[1])
  width(root.left, hl-1,ans)
  width(root.right, hl+1,ans)
  
  

width(root,0,ans) 
w = ans[1]-ans[0] + 1
l = []
idx = abs(ans[0]) 



class hl():
  def __init__(self, n, hl):
    self.n = n
    self.hl = hl
    
l.append(hl(root, idx)) 
ans = {}



flag = False

while(len(l)>0):
  if flag == True:
    break
  size = len(l)
  while(size>0):
    rn = l.pop(0)
    Node = rn.n
    if rn.hl not in ans:
      ans[rn.hl] = Node.data
    if len(ans)==w:
      flag = True
      break
    if Node.left!=None:
      l.append(hl(Node.left , rn.hl-1))
    if rn.n.right!=None:
      l.append(hl(Node.right, rn.hl+1))
    size -= 1

for i in range(len(ans)):
  print(ans[i], end=" ")
  
  
  
