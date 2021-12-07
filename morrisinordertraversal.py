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
   
def getrightmost(ln, curnode):
  while(ln.right!=None and ln.right!=curnode):
    ln = ln.right
  
  return ln
    
  



def morristraversal(root):
  ans = []
  cur = root
  while(cur!=None):
    leftnode = cur.left
    if(leftnode==None):
      ans.append(str(cur.data)) 
      cur = cur.right  
    else:
      rightmostnode = getrightmost(leftnode, cur)
      if(rightmostnode.right ==None):
        rightmostnode.right = cur 
        cur = cur.left   
      else:
        rightmostnode.right = None
        ans.append(str(cur.data))
        cur = cur.right
      
  return ans
  

ans = morristraversal(root)
print(" ".join(ans))



      
      
      
    