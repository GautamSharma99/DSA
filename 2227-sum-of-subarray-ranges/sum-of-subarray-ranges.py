class Solution(object):
    def miny(self,nums):
        stack=[]
        n=len(nums)
        left=[0]*n
        right=[0]*n
        for i in range(n):
            while stack and nums[stack[-1]]>nums[i]:
                stack.pop()
            if not stack:
                left[i]=i+1
            else:
                left[i]=i-stack[-1]
            stack.append(i)
        stack=[]
        for i in range(n-1,-1,-1):
            while stack and nums[stack[-1]]>=nums[i]:
                stack.pop()
            if not stack:
                right[i]=n-i
            else:
                right[i]=stack[-1]-i
            stack.append(i)
        total=0
        for i in range(n):
            total+=nums[i]*left[i]*right[i]
        return total

    def maxy(self,nums):
        n=len(nums)
        stack=[]
        left=[0]*n
        right=[0]*n
        for i in range(n):
            while stack and nums[stack[-1]]<nums[i]:
                stack.pop()
            if not stack:
                left[i]=i+1
            else:
                left[i]=i-stack[-1]
            stack.append(i)
        stack=[]
        for i in range(n-1,-1,-1):
            while stack and nums[stack[-1]]<=nums[i]:
                stack.pop()
            if not stack:
                right[i]=n-i
            else:
                right[i]=stack[-1]-i
            stack.append(i)
        total=0
        for i in range(n):
            total+=nums[i]*left[i]*right[i]
        return total

            

    def subArrayRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.maxy(nums)-self.miny(nums)
        