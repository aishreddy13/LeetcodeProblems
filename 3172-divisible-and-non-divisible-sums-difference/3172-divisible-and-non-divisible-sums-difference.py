class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        i = 1
        num1 = 0
        num2 = 0
        for i in range(n+1):
            if i % m != 0:
                num1 += i
            else:
                num2 += i
        
        return num1 - num2
        