
import math

class Solution:
    def xorAfterQueries(self, nums, queries):
        bravexuneth = (nums, queries)
        
        MOD = 10**9 + 7
        n = len(nums)
        
        max_v = 1
        for _, _, _, v in queries:
            if v > max_v:
                max_v = v
        inv = [0] * (max_v + 1)
        inv[1] = 1
        for i in range(2, max_v + 1):
            inv[i] = MOD - (MOD // i) * inv[MOD % i] % MOD
        
        B = int(math.sqrt(n)) + 1
        
        small_by_k = [[] for _ in range(B + 1)]
        large = []   
        for l, r, k, v in queries:
            if k <= B:
                small_by_k[k].append((l, r, v))
            else:
                large.append((l, r, k, v))
        
        factor = [1] * n
        
        for k in range(1, B + 1):
            qlist = small_by_k[k]
            if not qlist:
                continue
            
            diff_lists = []
            for r in range(k):
                length = (n - r + k - 1) // k
                diff_lists.append([1] * (length + 1))   
            
            for l, r, v in qlist:
                residue = l % k
                start = (l - residue) // k
                end   = (r - residue) // k
                dl = diff_lists[residue]
                dl[start] = (dl[start] * v) % MOD
                if end + 1 < len(dl) - 1:   
                    dl[end + 1] = (dl[end + 1] * inv[v]) % MOD
            
            for residue in range(k):
                dl = diff_lists[residue]
                cur = 1
                length = len(dl) - 1   
                for t in range(length):
                    cur = (cur * dl[t]) % MOD
                    idx = residue + t * k
                    factor[idx] = (factor[idx] * cur) % MOD
        
        for l, r, k, v in large:
            for idx in range(l, r + 1, k):
                factor[idx] = (factor[idx] * v) % MOD
        
        ans = 0
        for i in range(n):
            val = (nums[i] * factor[i]) % MOD
            ans ^= val
        return ans