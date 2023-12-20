class Solution:
    def second_highest_element(self, nums: list[int]) -> int:
        largest = float("-inf")
        second_highest = float("-inf")
        # Big O of n
        # Sorting algorithm would be Big O of nlogn so it is more efficient
        for num in nums:
            if largest < num:
                second_highest = largest
                largest = num
        if nums.count(second_highest) > 1:
            return f"{second_highest}: {nums.count(second_highest)}"
        return second_highest