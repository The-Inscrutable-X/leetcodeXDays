class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        l = 1
        r = len(nums) - 1

        def lower(n):
            number = 0
            for i in nums:
                if i <= n:
                    number += 1
            return number

        while l < r:
            print(l,r)
            mid = (l + r) //2
            if lower(mid) <= mid:
                l = mid + 1
            else:
                r = mid
        return l
        

sol = Solution()
ans = sol.findDuplicate([1,1])
print("assert 2:", ans)
ans = sol.findDuplicate([3,1,3,4,2])
print("assert 3:", ans)