class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        length = len(flowerbed)

        if flowerbed[0] == 0:
            if length == 1 or flowerbed[1] == 0:
                flowerbed[0] = 1
                n -= 1

        if flowerbed[length - 1] == 0:
            if flowerbed[length - 2] == 0:
                flowerbed[length - 1] = 1
                n -= 1

        counter = 0
        for i in range(1, length - 1):
            if flowerbed[i] == 0:
                counter += 1
                if counter == 3:
                    flowerbed[i - 1] = 1
                    n -= 1
                    counter = 1
            else:
                counter = 0

        return n <= 0