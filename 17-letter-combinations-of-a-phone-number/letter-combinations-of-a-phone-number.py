class Solution(object):
  
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        self.phone = {
            "2": "abc", "3": "def", "4": "ghi",
            "5": "jkl", "6": "mno", "7": "pqrs",
            "8": "tuv", "9": "wxyz"
        }
        self.digits=digits
        self.result=[]
        self.helper(0,"")
        return self.result

    def helper(self,index,current):
        if index==len(self.digits):
            self.result.append(current)
            return
        for ch in self.phone[self.digits[index]]:
            self.helper(index+1,current+ch)