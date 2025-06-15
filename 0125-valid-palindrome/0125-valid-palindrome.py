class Solution:
    def isPalindrome(self, s: str) -> bool:
        sc = "".join(char for char in s if char.isalnum()).lower()
        #print(cleaned_text)
        i, j = 0, len(sc)-1
        while i < j:
            if sc[i] != sc[j]:
                return False
            i += 1
            j -= 1
        return True