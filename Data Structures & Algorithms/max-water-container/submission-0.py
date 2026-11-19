class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxi = 0

        for i, h in enumerate(heights):
            last = len(heights) - 1

            while (heights[last] < h):
                area = (last - i) * heights[last]
                maxi = max(maxi, area)
                last -= 1
            area = (last - i) * h
            maxi = max(maxi, area)

        return (maxi)

        