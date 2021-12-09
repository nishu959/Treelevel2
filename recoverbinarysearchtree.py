
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
  a = None
  b = None
  cur = root
  prev = None
  while(cur!=None):
    leftnode = cur.left
    if(leftnode==None):
      if(prev!=None and prev.data > cur.data):
        if(a==None):
          a = prev
        b = cur
      prev = cur
      cur = cur.right  
    else:
      rightmostnode = getrightmost(leftnode, cur)
      if(rightmostnode.right ==None):
        rightmostnode.right = cur 
        cur = cur.left   
      else:
        rightmostnode.right = None
        if( prev.data > cur.data):
          if(a==None):
            a = prev
          b = cur 
        prev = cur
        cur = cur.right
      
  if(a!=None):
  
    temp = a.data
    a.data = b.data
    b.data = temp
  

morristraversal(root)


      
    


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
  

  
   
display(root)

  