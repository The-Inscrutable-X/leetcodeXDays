class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        isNeg: bool = False
        numsIndex: int = 0
        nubs: str = ""
        # if len(s) != 0 and (not (s[0].isdigit() or s[0] in "+-")):
        #     return 0
        for i, x in enumerate(s):
            print(s,"|" , nubs,"|" , numsIndex,"|" , x, "|" , x.isdigit())
            if i == 0 and x in "+-":
                if x == "-":
                    isNeg = True
                numsIndex += 1
            if numsIndex <= i:
                if x.isdigit():
                    nubs += x
                else:
                    break
        if nubs == "":
            return 0
        if isNeg:
            nubs = "-" + nubs
        return max(-(2**31), min(2**31 - 1, int(nubs)))

myClass = Solution()
print(myClass.myAtoi("-7 with words -7"))