class btree():
  def __init__(self, data, right = None, left = None):
    self.data = data
    self.right = right
    self.left = left
   
class pair():
  def __init__(self, node, state):
    self.node = node
    self.state = state


class zigzag():
  def __init__(self, forwardslope=-1, backwardslope=-1, maxlen=0):
    self.forwardslope= forwardslope
    self.backwardslope = backwardslope
    self.maxlen = maxlen
    
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
  

def longestzigzag(root):
  if(root ==None):
    return zigzag()
    
  lefttree = longestzigzag(root.left)
  righttree = longestzigzag(root.right)
  z = zigzag() 
  z.maxlen = max(max(lefttree.maxlen, righttree.maxlen),max(lefttree.backwardslope, righttree.forwardslope) + 1) 
  
  z.forwardslope = lefttree.backwardslope + 1
  z.backwardslope =  righttree.forwardslope + 1
  
  
  return z
  

ans = longestzigzag(root)
print(ans.maxlen)
  
