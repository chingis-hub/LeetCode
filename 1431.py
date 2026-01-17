class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxcandie = 0
        boollist = []
        for candie in candies:
            if maxcandie < candie:
                maxcandie = candie

        for candie in candies:
            if candie + extraCandies >= maxcandie:
                boollist.append(True)
            else:
                boollist.append(False)

        return boollist