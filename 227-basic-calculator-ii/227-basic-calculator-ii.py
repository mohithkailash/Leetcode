class Solution:
    def calculate(self, s: str) -> int:
        stack, operator , num = [] , "+" , 0
        operators = {"+","-","*","/"}
        for i in range(len(s)):
            if s[i].isdigit():
                num = num * 10 + int(s[i])
            if s[i] in operators or i == len(s) - 1:
                if operator == "+":
                    stack.append(num)
                elif operator == "-":
                    stack.append(-num)
                elif operator == "*":
                    stack[-1] *= num 
                elif operator == "/":
                    stack[-1] = int(stack[-1] / num)
                num = 0
                operator=s[i]
        return sum(stack)