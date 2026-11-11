class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        final = [1] * len(nums)

        prefix = 1 
        for i in range(len(nums)):
            final[i] = prefix
            prefix *= nums[i]

        final.reverse()
        nums.reverse()
        postfix = 1
        for i in range(len(nums)):
            final[i] *= postfix
            postfix *= nums[i]

        final.reverse() 
        return final


        #attempt 2: O(n^2)
        # product = math.prod(nums)
        # final = []
        # for i, num in enumerate(nums):
        #     if product == 0:
        #         if num == 0:
        #             final.append(math.prod(nums[0:i] + nums[i+1:]))
        #             continue
        #         final.append(0)
        #     elif product == 1 or product == -1:
        #         final.append(product * num)
        #         continue
        #     else:
        #         final.append(math.prod(nums[0:i] + nums[i+1:]))

            #attempt 1 - O(n) in best case, not worst case)
            # if num == 0:
            #     final.append(math.prod(nums[0:i] + nums[i+1:]))
            #     continue
            # final.append(int(product / num))

        return final

        