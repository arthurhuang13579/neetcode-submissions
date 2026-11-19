class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ret = []
        
        for i, n in enumerate(nums):
            if i > 0 and n == nums[i-1]:
                continue
            target = -n
            first = i + 1
            last = len(nums) - 1

            while first < last:
                if nums[first] + nums[last] == target:
                    ret.append([n, nums[first], nums[last]])
                    first += 1
                    while first < last and nums[first] == nums[first - 1]:
                        first += 1
                if nums[first] + nums[last] > target:
                    last -= 1
                else:
                    first += 1

        return ret

