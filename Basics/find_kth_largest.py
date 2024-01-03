# Find the kth largest element from an array. The array may contain duplicates. If it contains duplicate return the first index of occurence.
class Solution:
    def kth_largest(self, nums: list[int], k: int) -> int:
        set_nums = set(nums)
        kth_largest = list(set_nums)[k*-1]
        
        if len(nums) != len(set_nums):
            count = nums.count(kth_largest)
            if count > 1:
                index = self.find_first_occurance(nums, kth_largest)
                return f"{k}th largest element is {kth_largest} and it is found in the index {index} for the first time."
            
        return f"{k}th largest element is {kth_largest} and doesn't occur twice or more in the array."

    def find_first_occurance(self, nums, kth_largest):
        for i, n in enumerate(nums):
            if n == kth_largest:
                return i
            
            
               
print(Solution().kth_largest([3,8,2,5,1,4,0,6,9,3,7,2,5,8,1,4,0,6,9,3,2,5,8], 4))