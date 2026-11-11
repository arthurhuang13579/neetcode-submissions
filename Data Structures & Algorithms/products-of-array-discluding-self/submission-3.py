class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = math.prod(nums)
        print(product)
        final = []
        for i, num in enumerate(nums):
            # final.append(math.prod(nums[0:i] + nums[i+1:]))
            if num == 0:
                final.append(math.prod(nums[0:i] + nums[i+1:]))
                continue
            final.append(int(product / num))

        return final

        