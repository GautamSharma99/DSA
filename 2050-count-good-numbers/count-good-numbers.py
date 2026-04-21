class Solution(object):
    def countGoodNumbers(self, n):
        MOD = 10**9 + 7
        
        even = (n + 1) // 2
        odd = n // 2
        
        return (self.power(5, even, MOD) * self.power(4, odd, MOD)) % MOD
    
    def power(self, x, n, mod):
        if n == 0:
            return 1
        
        half = self.power(x, n // 2, mod)
        
        if n % 2 == 0:
            return (half * half) % mod
        else:
            return (x * half * half) % mod
            