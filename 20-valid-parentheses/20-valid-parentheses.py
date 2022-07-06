class Solution:
    def isValid(self, s: str) -> bool:
        my_stack = []
        for c in s:
            if c is '{' or c is '[' or c is '(':
                my_stack.append(c)
            else:
                if c is '}':
                    if not my_stack or my_stack.pop() != '{':
                        return False
                elif c is ']':
                    if not my_stack or my_stack.pop() != '[':
                        #print("hi")
                        return False
                else:
                    if not my_stack or my_stack.pop() != '(':
                        return False
        if my_stack:
            return False
        return True