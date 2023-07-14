class Solution:
    def linearTimeConstantSpace(self, nums):
        # print("case", nums)
        n = len(nums)
        # print(n * (n + 1)//2)
        expectation = (n * (n + 1)) // 2
        realSum = 0
        for i in nums:
            realSum += i
        # print(expectation, realSum)
        return expectation - realSum

    def missingNumberInplaceMem(self, nums: list[int]) -> int:
        nums.sort()
        center = len(nums)//2
        radius = center
        print(nums)
        while radius != 0:
            print("center index", center, "nums value", nums[center], "radius", radius)
            if radius < 1:
                if center < len(nums)-1:
                    if nums[center + 1] != center + 1:
                        return center + 1
                elif center == len(nums) - 1:
                    return len(nums)
                if center != 0:
                    if nums[center - 1] != center - 1:
                        return center - 1
                else:
                    return 0
            if nums[center] != center:
                center -= radius//2
            else:
                center += radius//2
            radius = radius//2



    def missingNumberLinearTime(self, nums: list[int]) -> int:
        existance = {i for i in range(len(nums)+1)}
        for j in nums:
            if j in existance:
                existance.remove(j)
        return existance.pop()

sol = Solution()
ans = sol.linearTimeConstantSpace([9,6,4,2,3,5,7,0,1])
print(ans)
ans = sol.linearTimeConstantSpace([3,0,1])
print(ans)
ans = sol.linearTimeConstantSpace([0,1])
print(ans)
ans = sol.linearTimeConstantSpace([1,2])
print(ans)