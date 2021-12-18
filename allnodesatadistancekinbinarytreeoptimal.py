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
  
  
ele, k = map(int, input().split())
  
 
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
   
def kdown(r, k, block, ans):
  if(r==None or k<0 or block ==r):
    return 
  if(k==0):
    ans.append(r.data)
    return  
    
  kdown(r.left, k-1, block, ans) 
  kdown(r.right, k-1, block, ans)
  
def ntrpath(node, ele, ans, k):
  if node ==None:
    return -1
 
  if(node.data ==ele):
    kdown(node, k-0, None, ans)
    return 1
  
  la = ntrpath(node.left, ele, ans, k)
  ra = ntrpath(node.right, ele, ans, k)
  
  if(la != -1):
    kdown(node,k - la , node.left, ans)
    return la+1
  
  if( ra!=-1):
    kdown(node,k - ra, node.right,ans)
    return ra+1
  
  
  return -1
  
 

ans=[]
ntrpath(root, ele, ans, k)
for i in ans:
  print(i)