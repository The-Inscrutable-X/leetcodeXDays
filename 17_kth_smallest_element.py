def lengthOfLIS(self, matrix: List[int]) -> int:
    sortedL = []
    for row in matrix:
        for element in row:
            dex = bisect_left(sortedL, element)
            sortedL.insert(dex, element)
    return sortedL