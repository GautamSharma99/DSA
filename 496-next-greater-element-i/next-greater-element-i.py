class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        stack=[]
        nge_map={}
        for i in range(len(nums2)-1,-1,-1):
            num=nums2[i]
            while stack and stack[-1] <=num:
                stack.pop()
            if stack:
                nge_map[num]=stack[-1]
            else:
                nge_map[num]=-1
            stack.append(num)
        result=[]
        for num in nums1:
            result.append(nge_map[num])
        return result