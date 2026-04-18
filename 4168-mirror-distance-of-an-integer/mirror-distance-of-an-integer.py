class Solution:
    def mirrorDistance(self, n):
        rev, x=0, n
        while x>0:
            x, r=divmod(x, 10)
            rev=10*rev+r
        return abs(rev-n)
        
        