from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for token in tokens:
            if token in "+-*/":
                b = stack.pop()
                a = stack.pop()
                
                if token == "+":
                    stack.append(a + b)
                elif token == "-":
                    stack.append(a - b)
                elif token == "*":
                    stack.append(a * b)
                else:  # division
                    stack.append(int(a / b))  # truncate toward zero
            else:
                stack.append(int(token))
        
        return stack[0]