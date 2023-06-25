class Solution:
    def countBeautifulPairs(self, nums: List[int]) -> int:
        total = 0
        alreadyPairs = set()
        def computeGCD(x, y):
            while(y):
               x, y = y, x % y
            return abs(x)
        for j in range(len(nums)):
            for i in range(j):
                firstDig = int(str(nums[i])[0])
                lastDig = int(str(nums[j])[-1])
                if computeGCD(firstDig, lastDig) == 1:
                    # print(total,i,j,firstDig,lastDig)
                    # print(alreadyPairs)
                    if (i,j) in alreadyPairs or i == j:
                        pass
                    else:
                        total += 1
                        alreadyPairs.add((j,i))
        return total
    
class Solution:
    def numberOfGoodSubarraySplits(self, nums: List[int]) -> int:
        onePosition = 0
        total = 0
        for i in range(len(nums)):
            # print(onePosition, i, nums[i])
            if onePosition == 0 and nums[i] == 1:
                onePosition += 1
                total += 1
            elif onePosition != 0 and nums[i] != 1:
                onePosition += 1
            elif onePosition != 0 and nums[i] == 1:
                total *= onePosition
                onePosition = 1
        return total % (10**9 + 7)
                
## Unfinished
class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        iterations = 0
        while num1 > 0:
            subtractor = -1
            for i in range(0,60):
                # print(i)
                if num1 - (2**i + num2) >= 0:
                    subtractor = 2**i + num2 
            if subtractor == -1 or subtractor <= 0:
                return -1
            print(subtractor)
            num1 -= subtractor
            iterations += 1
        return iterations
    #Didn't have enough time tonight