class Solution:
    def survivedRobotsHealths(self, positions: list[int], healths: list[int], directions: str) -> list[int]:
        byPositions: list[tuple(list[int, int, str], int)] = []
        for i in range(len(positions)):
            byPositions.append(([positions[i], healths[i], directions[i]], i))
        byPositions.sort(key = lambda x: x[0][0])
        print(byPositions)
        # def someFunc(x):
        #     return x[0][0]
        out: list[tuple(list[int, int, str], int)] = []
        viableBots = []
        for j in range(len(byPositions)):
            direction = byPositions[j][0][2]
            if direction == "R":
                viableBots.append(byPositions[j])
            elif direction == "L":
                while byPositions[j][0][1] and viableBots:
                    if byPositions[j][0][1] == viableBots[-1][0][1]:
                        viableBots.pop()
                        byPositions[j][0][1] = 0
                        break
                    elif byPositions[j][0][1] < viableBots[-1][0][1]:
                        viableBots[-1][0][1] -= 1
                        break
                    elif byPositions[j][0][1] > viableBots[-1][0][1]:
                        byPositions[j][0][1] -= 1
                        viableBots.pop()
                if (not viableBots) and byPositions[j][0][1] != 0:
                    out.append(byPositions[j])
        for i in viableBots:
            out.append(i)
    
        out.sort(key = lambda x: x[1]) # sort according to original input order
        print(out)
        return [x[0][1] for x in out]

sol = Solution()
ans = sol.survivedRobotsHealths([5,4,3,2,1], [2,17,9,15,10], "RRRRR")
print("expect ", ans)
ans = sol.survivedRobotsHealths([3,5,2,6], [10,10,15,12], "RLRL")
print("expect ", ans)
ans = sol.survivedRobotsHealths([1,2,5,6], [10,10,11,11], "RLRL")
print("expect ", ans)
ans = sol.survivedRobotsHealths([1,2,5,6], [10,10,11,111], "RRRL")
print("expect ", ans)