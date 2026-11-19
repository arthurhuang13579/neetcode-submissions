class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_a = 0
        stack = []

        for i, height in enumerate(heights):
            ind = i
            while stack and height < stack[-1][1]:
                length = i - stack[-1][0]
                area = length * stack[-1][1]
                max_a = max(max_a, area)
                ind = stack[-1][0]
                stack.pop()
            stack.append((ind, height))

        #print(stack)

        while stack:
            i, height = stack.pop()

            length = len(heights) - i
            #print("Length: " + str(length))
            area = length * height
            #print(area)
            max_a = max(max_a, area)
            
            #print()
            
        return max_a

        