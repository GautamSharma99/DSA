class Solution(object):
    def helper(self,start,k,target,current,result):
        if k==0 and target==0:
            result.append(current[:])
            return
        if k==0 or target<0:
            return
        for num in range(start,10):
            current.append(num)
            self.helper(num+1,k-1,target-num,current,result)
            current.pop()


    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        result=[]
        self.helper(1,k,n,[],result)
        return result
        