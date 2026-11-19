class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxi = 0
        first = 0
        last = len(heights) - 1

        while first < last:
            area = (last - first) * min(heights[first], heights[last])
            maxi = max(area, maxi)
            if heights[first] < heights[last]:
                first += 1
            else:
                last -= 1

        return (maxi)

        