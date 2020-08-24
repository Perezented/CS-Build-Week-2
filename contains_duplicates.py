class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        key = {}
        for number in nums:
            if number not in key:
                key[number] = number
            elif number in key:
                return True
        return False
