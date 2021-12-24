class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        n = 1
        s = 1
        while(s<label):
            n = n * 2
            s += n
        ans = []
        ans.append(label)
        while(label!=1):
            com = 3 * n - label - 1
            result = com//2
            ans.append(result)
            label = result
            n = n//2
            
        return ans[::-1]
            
        