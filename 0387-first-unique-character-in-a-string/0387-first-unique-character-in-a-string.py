class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = collections.Counter(s)

        for index, cha in enumerate(s):
            if count[cha] == 1:
                return index
        return -1