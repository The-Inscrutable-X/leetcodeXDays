class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        from collections import deque
        repeat_indices = deque()
        curLength: int = 0
        bestLength: int = 0
        # i is starting index of window, j is current index
        for i in range(len(s)):
            for j in range(i+curLength, len(s)):
                print(repeat_indices, curLength, bestLength)
                if s[j] in repeat_indices:
                    repeat_indices.popleft()
                    curLength -= 1
                    break
                else:
                    repeat_indices.append(s[j])
                    curLength += 1
                    if curLength > bestLength:
                        bestLength = curLength
        return bestLength
    
    def lengthOfLongestSubstringOptimal(self, s: str) -> int:
        from collections import deque
        repeat_indices = dict()
        maxSize = 0
        # i is starting index of window, j is current index
        start: int = 0
        for end in range(len(s)):
            if s[end] in repeat_indices:
                start = repeat_indices[s[end]] + 1
            else:
                repeat_indices[s[end]] = end
                maxSize = max(maxSize, end - start)

        return maxSize

    

so = Solution()
res = so.lengthOfLongestSubstringOptimal("abcabb")
print(res)