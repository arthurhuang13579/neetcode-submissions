class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        check = set(nums)

        max = 0
        for n in nums:
            count = 0
            if n-1 not in check:
                count += 1
                i = n + 1
                while (i in check):
                    count += 1
                    i += 1
                if count > max:
                    max = count
        return max
            

                
        