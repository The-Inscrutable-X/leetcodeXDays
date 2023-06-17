import typing
from typing import Optional

#Must find case where target is after a non
#target(start), and case where target is after a non target(end)

class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        end, start, s, e = -1, -1, 0, len(nums) - 1
        while s <= e:
            mid = (s + e)//2
            print(mid, s, e)
            if mid == s:
                print("found")
                if nums[mid] == target:
                    start = mid; break
            elif (nums[mid - 1] != target and nums[mid] == target):
                start = mid; break
            if nums[mid] < target:
                s = mid + 1
            else:
                e = mid - 1
        # print("determined start:", start)
        s, e = 0, len(nums) - 1
        while s <= e:
            mid = (s + e)//2
            print(mid, s, e)
            if mid == e:
                print("found")
                if nums[mid] == target:
                    end = mid; break
            elif (nums[mid + 1] != target and nums[mid] == target):
                end = mid; break
            if nums[mid] < target:
                s = mid + 1
            else:
                e = mid - 1
        # print("determined end:", end)
        return start, end

sol = Solution()
ans = sol.searchRange([], 0)
print("assert -1,-1", ans)
ans = sol.searchRange([5,7,7,8,8,10], 8)
print("assert 3,4", ans)
ans = sol.searchRange([5,5,7,7,8,8,10], 5)
print("assert 0,1", ans)
ans = sol.searchRange([5,5,7,7,8,8,10], 10)
print("assert 6,6", ans)
ans = sol.searchRange([8,8,8,0,0,0], 8)
print("assert 0,2", ans)
ans = sol.searchRange([5,7,7,8,8,10], 6)
print("assert -1,-1", ans)
ans = sol.searchRange([5,5], 5)
print("assert 0,1", ans)