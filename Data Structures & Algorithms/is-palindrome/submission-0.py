class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(c.lower() for c in s if c.isalnum())
        for i in range(len(s)):
            opposite = len(s) - i - 1 
            if s[i] == s[opposite]:
                continue
            else:
                return False

        return True