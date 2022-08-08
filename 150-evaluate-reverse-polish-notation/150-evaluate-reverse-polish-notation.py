class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        mystack = []
        for i in tokens:
            if i != "+" and i != "-" and i != "*" and i != "/":
                mystack.append(int(i))
            else:
                operand1 = mystack.pop()
                operand2 = mystack.pop()
                if i == "+":
                    mystack.append(operand1 + operand2)
                elif i == "-":
                    mystack.append(operand2 - operand1)
                elif i == "*":
                    mystack.append(operand1 * operand2)
                else:
                    mystack.append(int(operand2 / operand1))
        return mystack[0]