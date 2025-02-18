class Solution:
    def calculate(self, s: str) -> int:
        if not s:
            return 0
        stack =[]
        curr_number = 0
        operation ='+'
        for i, char in enumerate(s):
            if char.isdigit():
                curr_number = curr_number * 10 + int(char)
            if (not char.isdigit() and not char.isspace()) or i == len(s) -1:
                if operation == '-':
                    stack.append(-curr_number)
                elif operation == '+':
                    stack.append(curr_number)
                elif operation == '*':
                    stack.append(stack.pop() * curr_number)
                elif operation == '/':
                    stack.append(int(stack.pop() / curr_number))
                operation = char
                curr_number = 0
        return sum(stack)