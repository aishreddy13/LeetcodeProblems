class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        longest_sub = ""
        while i < len(s):
            substring1 = ""
            j = i
            for j in range(i, len(s)):
                if s[j] not in substring1:
                    substring1 += (s[j])
                    print(j)
                else:
                    print(j)
                    break
            if len(longest_sub) < len(substring1):
                longest_sub = substring1
            i += 1
        return len(longest_sub)