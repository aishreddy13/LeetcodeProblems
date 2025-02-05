from collections import Counter 
class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        counter = Counter(arr)
        max_num = max(counter, key=counter.get) 
       
        return (max_num)
        