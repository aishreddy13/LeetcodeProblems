class Solution:
    def calculate(self, s: str) -> int:
        if not s:
            return 0

        length = len(s)
        current_number = 0
        last_number = 0
        result = 0
        operation = '+'

        for i, char in enumerate(s):
            if char.isdigit():
                current_number = current_number * 10 + int(char)
            if (not char.isdigit() and not char.isspace()) or i == length - 1:
                if operation == '+' or operation == '-':
                    result += last_number
                    last_number = current_number if operation == '+' else -current_number
                elif operation == '*':
                    last_number = last_number * current_number
                elif operation == '/':
                    last_number = int(last_number / current_number)
                operation = char
                current_number = 0

        result += last_number
        return result