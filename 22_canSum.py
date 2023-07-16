class Solution:
    def canSum(self, x: int, nums: list[int], memo: dict = {-1:[]}) -> bool:
        """How sum implementation of CanSum"""
        if x < 0: return False
        if x == 0: return True
        if x in memo: return memo[x]
        for num in nums:
            isSummable = self.canSum(x-num, nums, memo)
            if isSummable:
                memo[-1].append(num)
                return True
        memo[x] = False
        return False


sol = Solution()
ans = sol.canSum(0, [2, 3])  # true
print(ans)
ans = sol.canSum(7, [])  # false
print(ans)
ans = sol.canSum(7, [2,4])  # false
print(ans)
ans = sol.canSum(8, [2,3,5])  # true
print(ans)
ans = sol.canSum(300, [7, 14])  # false
print(ans)
memoMe = {-1:[]}
ans = sol.canSum(8, [2,3,5], memoMe)  # true
print(ans, memoMe[-1])
