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

    def palindrome_wc(self, s: str) -> str:
        palindrome: str = ""
        length = len(s)
        if length % 2 == 0:
            copy_of_s = s
            s = "|"
            for letter in copy_of_s:
                s += letter+"|"
        # print(s)
        for center in range(length):
            # print("!-center:", center)
            max_possible = min(length-center-1, center)
            # print("Max:", max_possible)
            for offset in range(max_possible+1):
                # print("Offset:", offset)
                # print("left n right:", s[center - offset], s[center + offset])
                if s[center + offset] == s[center - offset]:
                    candidate_palindrome = s[center - offset : center + offset + 1] 
                    # print("examining:", s[center - offset : center + offset + 1])
                    if len(candidate_palindrome) > len(palindrome):
                        # print("replace with:", s[center - offset : center + offset + 1])
                        palindrome = candidate_palindrome
        return palindrome
        ## his time we use a expanding window tactic on every element of s. (Is this essentially brute force?)

    def palindrome1(self, s: str) -> str:
        palindrome: str = ""
        length = len(s)
        is_even = False

        center = length//2
        for change in range(length):
            #This ensures we check from the center outwards
            if change % 2 == 0:
                center -= change
            else:
                center += change

            max_possible = min(length-center-1, center)
            for offset in range(max_possible+1):
                # print("left n right:", s[center - offset], s[center + offset])
                if s[center + offset] == s[center - offset]:
                    candidate_palindrome = s[center - offset : center + offset + 1] 
                    # print("examining:", s[center - offset : center + offset + 1])
                    if len(candidate_palindrome) > len(palindrome):
                        palindrome = candidate_palindrome
                else:
                    break
        
        copy_of_s = s
        s = "|"
        is_even = True
        for letter in copy_of_s:
            s += letter+"|"
        length = len(s)

        palindrome += "|" * (len(palindrome))
        # print(palindrome)
        
        for center in range(length):
            if center % 2 == 1:
                continue
            max_possible = min(length-center-1, center)
            for offset in range(1, max_possible+1, 2):
                # print("Even left n right:", center - offset, center + offset)
                if s[center + offset] == s[center - offset]:
                    candidate_palindrome = s[center - offset : center + offset + 1] 
                    # print("examining:", s[center - offset : center + offset + 1])
                    if len(candidate_palindrome) > len(palindrome):
                        palindrome = candidate_palindrome
                else:
                    break

        return palindrome.replace("|", "")
        ## his time we use a expanding window tactic on every element of s. (Is this essentially brute force?)
                
solu: Solution = Solution()
sol: str = solu.palindrome1("sbscc")
print(sol)


