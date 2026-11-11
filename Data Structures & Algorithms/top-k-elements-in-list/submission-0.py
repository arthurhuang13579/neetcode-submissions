class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = defaultdict(int)

        for n in nums:
            res[n] += 1

        topnum = []
        for num, app in sorted(res.items(), key=lambda item:item[1], reverse=True):
            if k == 0:
                return topnum
            topnum.append(num)
            k-=1
        return topnum
            

    
        