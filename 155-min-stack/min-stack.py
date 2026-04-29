class MinStack(object):

    def __init__(self):
        self.st=[]
        self.mini=None
        

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        if not self.st:
            self.mini=val
            self.st.append(val)
            return
        if val>self.mini:
            self.st.append(val)
        else:
            self.st.append(2*val-self.mini)
            self.mini=val
        

    def pop(self):
        """
        :rtype: None
        """
        if not self.st:
            return
        x=self.st.pop()
        if x<self.mini:
            self.mini=2*self.mini-x

        

    def top(self):
        """
        :rtype: int
        """
        if not self.st:
            return -1
        x=self.st[-1]
        if self.mini<x:
            return x
        return self.mini
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.mini
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()