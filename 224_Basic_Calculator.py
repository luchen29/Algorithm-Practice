class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 
        result, number, operator, temp = 0, 0, 1, []
        for i in s:
            if i in "0123456789":
                number = number*10 + int(i)
            elif i == "+":
                result += operator * number
                operator, number = 1, 0 
            elif i == "-":
                result += operator * number
                operator, number = -1, 0 
            elif i == "(":
                temp.append(result)
                temp.append(operator)
                operator, result = 1, 0
            elif i == ")":
                result += operator * number
                operator = temp.pop()
                number = temp.pop()
                result = operator*result + number
                operator, number = 1, 0 
        result += operator * number
        return result
                
            
            
        