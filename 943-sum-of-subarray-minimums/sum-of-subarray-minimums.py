class Solution(object):
    def sumSubarrayMins(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n=len(arr)
        MOD=10**9+7
        left=[0]*n
        right=[0]*n
        stack=[]
        for i in range(n):
            while stack and arr[stack[-1]]>arr[i]:
                stack.pop()
            if not stack:
                left[i]=i+1
            else:
                left[i]=i-stack[-1]
            stack.append(i)
        stack=[]
        for i in range(n-1,-1,-1):
            while stack and arr[stack[-1]]>=arr[i]:
                stack.pop()
            if not stack:
                right[i]=n-i
            else:
                right[i]=stack[-1]-i
            stack.append(i)
        total=0
        for i in range(n):
            total+=arr[i]*left[i]*right[i]
            total%=MOD
        return total
        