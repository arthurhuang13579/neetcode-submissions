class Solution:
    def trap(self, height: List[int]) -> int:
        prefix = [0] * len(height)
        suffix = [0] * len(height)
        max_water = [0] * len(height)

        for i, h in enumerate(height):
            if i == 0:
                prefix[i] = h
                continue
            prefix[i] = max(h, prefix[i-1])

        reverse = reversed(height)
        for i, h in enumerate(reverse):
            if i == 0:
                suffix[i] = h
                continue
            suffix[i] = max(h, suffix[i-1])
        suffix.reverse()

        for i, h in enumerate(max_water):
            max_water[i] = min(prefix[i], suffix[i]) - height[i]

        return sum(max_water)