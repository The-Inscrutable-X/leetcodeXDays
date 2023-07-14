class Solution:
    def singleNumber(self, nums: list[int]) -> list[int]:
        """
        Xoring all elements will produce a value k which is the xor of the two single elements
        Since the two singles are not the same, k has at least 1 digit that is set.
        We use that digit to separate the nums into two separate lists each containing one 
        of the two singles. All numbers that are the same will go into the same partitioned list. 
        We then use the standard method: xor all elements of the partitions 
        and the result of the xor should be a single from each of the partitions. 
        """
        sumXor = 0
        for i in nums:
            # print(bin(i), bin(sumXor))
            sumXor = sumXor ^ i
        
        index = 0
        for i in range(abs(sumXor)):
            if ((1 << i) & sumXor) > 0:
                index = i
                break
        # print(index, "found at", bin(sumXor))
        # print([bin(i) for i in [-145417756,744132272]])
        # print(((1 << index) & -145417756),((1 << index) & 744132272))
        firstSum = 0
        secondSum = 0
        for b in nums:
            if ((1 << index) & b) > 0:
                firstSum = firstSum ^ b
                # print("first", bin(b), bin(firstSum))
            else:
                secondSum = secondSum ^ b
                # print("second", bin(b), bin(secondSum))
        return [firstSum, secondSum]

sol = Solution()
ans = sol.singleNumber([9,5,9,5,0,1,10,10])
print("expect 0, 1", ans)
ans = sol.singleNumber([9,5])
print("expect 9, 5", ans)
ans = sol.singleNumber([9,5,9,5,0,1,10,7,1,8,8,76,90,90,10,100,76,100])
print("expect 0, 7", ans)