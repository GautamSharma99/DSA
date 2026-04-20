class Solution(object):
    def generateParenthesis(self,n):
        self.res=[]
        self.solve(0,0,"",n)
        return self.res
        

        """
        :type n: int
        :rtype: List[str]
        """

    def solve(self,open_,close_,output,n):
        if open_==n and close_==n:
            self.res.append(output)
            return

        if open_<n:
            self.solve(open_+1,close_,output+"(",n)
        
        if close_<open_:
            self.solve(open_,close_+1,output+")",n)

        

        