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

class BstIterator():
  cur = None
  def __init__(self, root):
    self.cur = root
    
  
  def getrightmost(self, ln, curnode):
    while(ln.right!=None and ln.right!=curnode):
      ln = ln.right
    return ln 
    
  def morristraversal(self):
    ans = None
    
    while(self.cur!=None):
      leftnode = self.cur.left
      if(leftnode==None):
        
        ans = self.cur
        self.cur = self.cur.right  
        break
      else:
        rightmostnode = self.getrightmost(leftnode, self.cur)
        if(rightmostnode.right ==None):
          rightmostnode.right = self.cur 
          self.cur = self.cur.left   
        else:
          ans = self.cur
          
          rightmostnode.right = None
          self.cur = self.cur.right
          break
    
    return ans
  
   
  def nextitr(self):
    res = self.morristraversal()
    return res.data
    
 
  def hasnext(self):
    return self.cur!=None
   
  
a = BstIterator(root)

while(a.hasnext()):
  print(a.nextitr())
 
