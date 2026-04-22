class Solution(object):
    def helper(self,nums,index,current,result):
        if index==len(nums):
            result.append(current[:])
            return
        self.helper(nums,index+1,current,result)
        current.append(nums[index])
        self.helper(nums,index+1,current,result)
        current.pop()


    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result=[]
        current=[]
        self.helper(nums,0,current,result)
        return result

        