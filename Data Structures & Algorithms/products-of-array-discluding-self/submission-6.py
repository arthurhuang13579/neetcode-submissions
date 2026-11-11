class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = math.prod(nums)
        final = []
        for i, num in enumerate(nums):
            if product == 0:
                if num == 0:
                    final.append(math.prod(nums[0:i] + nums[i+1:]))
                    continue
                final.append(0)
            elif product == 1 or product == -1:
                final.append(product * num)
                continue
            else:
                final.append(math.prod(nums[0:i] + nums[i+1:]))
            # if num == 0:
            #     final.append(math.prod(nums[0:i] + nums[i+1:]))
            #     continue
            # final.append(int(product / num))

        return final

        