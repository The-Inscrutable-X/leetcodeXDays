class Solution:
    def majorityElement1(self, nums) -> int:
        counts: dict = dict()
        for i in nums:
            if i in counts:
                counts[i] += 1
            else:
                counts[i] = 1
        myMax = 0
        myLetter = ""
        for j in counts:
            if counts[j] > myMax:
                myMax = counts[j]
                myLetter = j
        return myLetter


    def majorityElement(self, nums) -> int:
        counts: dict = dict()
        for i in nums:
            if i in counts:
                counts[i] += 1
            else:
                counts[i] = 1
        myMax = 0
        myLetter = ""
        for j in counts:
            if counts[j] > myMax:
                myMax = counts[j]
                myLetter = j
        return myLetter

sol = Solution()
ans = sol.majorityElement([])
print(ans)