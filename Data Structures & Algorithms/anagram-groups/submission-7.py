class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        total = defaultdict(list)
        
        for s in strs:
            total[tuple(sorted(s))].append(s)
            
        return list(total.values())
        
