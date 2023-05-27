class Solution:
    def isPalindrome(self, x: int) -> bool:
        from math import log
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        if x == 0:
            return True
        flag = False #flag odd number
        if (int(log(x, 10))+1)%2 == 1:
            flag = True
        reversed: int = 0
        while x > reversed:
            reversed = reversed*10 + (x%10)
            x = x//10
        if flag:
            reversed = reversed //10
        return reversed == x