class Solution:
    def reverseVowels(self, s: str) -> str:
        lst = list(s)
        vowels_list = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        left = 0
        right = len(lst) - 1

        while left < right:
            while left < right and lst[left] not in vowels_list:
                left += 1
            while left < right and lst[right] not in vowels_list:
                right -= 1

            lst[left], lst[right] = lst[right], lst[left]
            left += 1
            right -= 1

        return "".join(lst)
