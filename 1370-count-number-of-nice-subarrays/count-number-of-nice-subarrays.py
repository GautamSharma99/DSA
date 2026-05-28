class Solution(object):
    def numberOfSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return self.atmost(nums,k)-self.atmost(nums,k-1)

    def atmost(self,nums,k):
        left=0
        res=0
        for right in range(len(nums)):
            if nums[right]%2!=0:
                k-=1
            while k<0:
                if nums[left]%2!=0:
                    k+=1
                left+=1
            res+=(right-left+1)
        return res
        