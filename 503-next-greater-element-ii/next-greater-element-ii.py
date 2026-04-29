class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        stack=[]
        n=len(nums)
        result=[0]*n
        for i in range(2*n-1,-1,-1):
            curr=nums[i%n]
            while stack and stack[-1]<=curr:
                stack.pop()
            if i < n:

                if stack:
                    result[i]=stack[-1]
                else:
                    result[i]=-1
            stack.append(curr)
        return result
        