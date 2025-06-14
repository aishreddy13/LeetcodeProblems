class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        res = "1"
        for _ in range(1, n):
            temp = ""
            count = 1
            for i in range(len(res)):
                if i + 1 < len(res) and res[i] == res[i+1]:
                    count +=1
                else:
                    temp += str(count) + res[i]
                    count = 1
            res = temp
        
        return res