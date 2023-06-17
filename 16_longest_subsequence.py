def lengthOfLIS2(self, nums: list[int]) -> int:
    """
    Thought Process:
    We generate a monotonic stack, which at any given time, should be a valid discrete subsequence.
    We keep track of the max size of the stack as it is built.
    When a number is added, the max size increases.
    When a number is deleted, this means that the current subsequence has reached its max size.
    A new sequence could subsequently start.
    We only update the max size when we add elements to monotonic.
    """
    monoTonic = [nums[0]]
    maxSequence = 1
    curSequence = 1
    i = 1
    while i < len(nums):
        print(curSequence, maxSequence, monoTonic)
        if len(monoTonic) == 0 or monoTonic[-1] < nums[i]:
            monoTonic.append(nums[i])
            curSequence += 1
            if maxSequence < curSequence:
                maxSequence = curSequence
            i += 1
        else:
            monoTonic.pop()
            curSequence -= 1
    return maxSequence


def lengthOfLIS1(self, nums: list[int]) -> int:
        maxSequence = 0
        curSequence = 0
        for i in range(1, len(nums)):
            print(nums[i], nums[i] > nums[i-1], curSequence, maxSequence)
            if nums[i] > nums[i-1]:
                curSequence += 1
            else:
                curSequence = 0
            if curSequence > maxSequence:
                maxSequence = curSequence
        return maxSequence

def lengthOfLIS(self, nums: list[int]) -> int:
    """
    Thought Process:
    Brute force it, by checking every valid substring. 
    """
    monoTonic = [nums[0]]
    maxSequence = 1
    curSequence = 1
    i = 1
    while i < len(nums):
        print(curSequence, maxSequence, monoTonic)
        if len(monoTonic) == 0 or monoTonic[-1] < nums[i]:
            monoTonic.append(nums[i])
            curSequence += 1
            if maxSequence < curSequence:
                maxSequence = curSequence
            i += 1
        else:
            monoTonic.pop()
            curSequence -= 1
    return maxSequence

ans = lengthOfLIS(None, [10,9,2,5,3,7,101,18])
print(ans)