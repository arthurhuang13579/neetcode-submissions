class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        running_list = {}
        for i, num in enumerate(nums):
            if num in running_list:
                return [running_list[num], i]
            running_list[target - num] = i
        
        