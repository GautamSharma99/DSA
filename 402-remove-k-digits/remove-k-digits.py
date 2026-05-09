class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        stack=[]
        for i in num:
            while stack and k>0 and stack[-1]>i:
                stack.pop()
                k-=1
            stack.append(i)

        while k>0:
            stack.pop()
            k-=1
        result="".join(stack)
        result=result.lstrip('0')
        if result:
            return result
        else:
            return "0"
