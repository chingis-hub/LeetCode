def two_sum(nums, target):
    seen = {}
    for index, number in enumerate(nums):
        remainder = target - number
        if remainder in seen:
            return [seen[remainder], index]
        seen[number] = index
    return [-1, -1]
