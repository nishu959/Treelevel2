
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
def width(root, hl ,ans):
  if root ==None:
    return None
  ans[0] = min(hl, ans[0])
  ans[1] = max(hl, ans[1])
  width(root.left, hl-1, ans)
  width(root.right, hl+1, ans)


width(root, 0 ,ans)
w = ans[1] - ans[0] + 1


result = [0]*(w)


def sumvertical(root, hl, result):
  if root == None:
    return None
 
  result[hl] += root.data
 
  sumvertical(root.left, hl-1, result)
  
  sumvertical(root.right, hl+1, result)


start = abs(ans[0])
sumvertical(root, start, result)


print(*result, sep="\n")