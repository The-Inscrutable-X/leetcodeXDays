class Solution:
    def isPalindrome(self, x: int) -> bool:
        """Time: O(N) or O(Log(N))if taking N to the the number value.
        Space: constant"""
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        if x == 0:
            return True

        reversed: int = 0
        while x > reversed:
            reversed = reversed*10 + (x%10)
            x = x//10

        return reversed == x or reversed // 10 == x

    def OptimizedMoreIsPalindrome(self, x: int) -> bool:
        """Time: O(N) or O(Log(N))if taking N to the the number value.
        Space: constant"""
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

    def PreOptimalIsPalindrome(self, x: int) -> bool:
        """Time: O(N) or O(Log(N))if taking N to the the number value.
        Space: same as time"""
        if x < 0:
            return False
        storage = []
        temp: int
        while x/10 > 0:
            print(x)
            temp = x
            x = x//10
            storage.append(temp-x*10)
        for i in range(len(storage)//2):
            if storage[i] != storage[-i-1]:
                return False
        return True