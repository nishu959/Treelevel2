
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


class maxpathsum():
  def __init__(self, ntn=-sys.maxsize , ntntr=0):
    self.ntn = ntn
    self.ntntr = ntntr
    
    
    
m = int(input())
n = []
for i in range(m):
  n.append(int(input()))


def btreeform(n, s, root):
  
  root = btree(int(n[0]))
  
  
  p = pair(root,1)
  s.append(p)
  idx =0
  while(len(s)>0):
    top = s[-1]
    if(top.state == 1):
    
      idx+=1
      if(n[idx]!=-1):
        t = btree(int(n[idx])) 
        top.node.left = t
      
        p = pair(t, 1)
        s.append(p)
      else:
        top.node.left = None
      
      top.state += 1
    
    
    elif(top.state == 2):
      idx+=1
      if(n[idx]!=-1):
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


def mps(root):
  p = maxpathsum()
  
  if(root ==None):
    return p
  
  la = mps(root.left)
  ra = mps(root.right)
  
  p.ntntr = max(la.ntntr, ra.ntntr) + root.data
  
  p.ntn = max(root.data, la.ntn, ra.ntn, p.ntntr, la.ntntr + ra.ntntr +root.data)
  
  p.ntntr = max(p.ntntr, root.data)
  

  return p

print(mps(root).ntn)

