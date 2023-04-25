from math import ceil


# The class contains a method that takes a string as input and returns a string where even-indexed
# characters are moved to the end of the string and odd-indexed characters are moved to the beginning
# of the string. Contrary to expectation, it does not return a palindrome.
class Solution:
    def evenUpOddDown(self, s: str) -> str:
        palindrome: str = ""
        for i in range(len(s)):
            if len(palindrome) == 0:
                palindrome += s[i]
            elif len(palindrome) % 2 == 1:
                palindrome = palindrome[:len(palindrome)//2] + s[i] +\
                    palindrome[-1*len(palindrome)//2:]
            elif len(palindrome) % 2 == 0:
                palindrome = palindrome[:len(palindrome)//2] + s[i] +\
                    palindrome[-1*len(palindrome)//2:]
        return palindrome

    def palindrome(self, s: str) -> str:
        palindrome: str = ""
        for i in range(len(s)):
            if len(palindrome) == 0:
                palindrome += s[i]
            elif len(palindrome) % 2 == 1:
                print(palindrome[len(palindrome)//2], len(s)-i-1)
                if palindrome[len(palindrome)//2] == s[len(s)-i]:
                    palindrome = palindrome[:len(palindrome)//2] + s[i] +\
                        palindrome[-1*len(palindrome)//2:]
            elif len(palindrome) % 2 == 0:
                palindrome = palindrome[:len(palindrome)//2] + s[i] +\
                    palindrome[-1*len(palindrome)//2:]
        return palindrome

    def palindrome1(self, s: str) -> str:
        palindrome: str = ""
        for i in range(len(s)):
            print(palindrome, i)
            if len(palindrome) == 0:
                palindrome += s[i]
            elif len(palindrome) % 2 == 1:
                # print(palindrome[len(palindrome)//2], s[len(s)-ceil(i//2)], i)
                if palindrome[len(palindrome)//2] == s[len(s)-i//2-1]:
                    palindrome = palindrome[:len(palindrome)//2] + s[len(s)-i] +\
                        palindrome[-1*len(palindrome)//2:]
            elif len(palindrome) % 2 == 0:
                palindrome = palindrome[:len(palindrome)//2] + s[len(s)-i] +\
                    palindrome[-1*len(palindrome)//2:]
        return palindrome

        ## his time we use a expanding window tactic on every element of s. (Is this essentially brute force?)
                
solu: Solution = Solution()
sol: str = solu.palindrome1("sannas")
print(sol)


