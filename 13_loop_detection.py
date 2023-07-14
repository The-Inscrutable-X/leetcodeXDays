class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = "".join([i for i in s if i in "abcdefghijklmnopqrstuvwxyz0123456789"])
        start = 0
        end = len(s) - 1
        while start < end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True