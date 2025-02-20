class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def process_string(a):
            stack = []

            for char in a:
                if char != "#":
                    stack.append(char)
                elif stack:
                    stack.pop()
                    
            return "".join(stack)
        
        return process_string(s) == process_string(t)
