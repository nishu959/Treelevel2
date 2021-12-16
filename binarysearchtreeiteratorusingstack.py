class btree():
  def __init__(self, data, left=None, right=None):
    self.data = data
    self.right = right
    self.left = left
   
 
n = int(input())
l = list(map(int, input().split()))


def bsttree(a, start, end):
  while(start<=end):
    mid = (start +end)//2
    
    val = a[mid]
    lc = bsttree(a, start, mid - 1)
    
    rc = bsttree(a, mid +1, end)
    
    p = btree(val, lc, rc)
    
    return p

root = bsttree(l, 0, n-1)


class BSTItertor():
  st = []
  
  def __init__(self, node):
    self.node = node
    self.addall(node)
  
   
  def addall(self, node):
    while(node!=None):
      self.st.insert(0,node)
      node = node.left
    
  
  def nextitr(self):
    top = self.st.pop(0)
    self.addall(top.right)
    return top.data
    
  def hasnext(self):
    return len(self.st)!=0
  
   
  
  
a = BSTItertor(root)

while(a.hasnext()):
  print(a.nextitr())

