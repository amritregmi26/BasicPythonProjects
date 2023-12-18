class Solution:
    def second_highest_element(self, nums: list[int]) -> int:
        highest = max(nums)
        nums.remove(highest)
        second_highest = max(nums)
        if nums.count(second_highest) > 1:
            return f"{second_highest}: {nums.count(second_highest)}"
        return second_highest