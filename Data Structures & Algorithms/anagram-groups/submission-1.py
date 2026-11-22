class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m = {}
        for i,v in enumerate(strs):
            if tuple(sorted(v)) in m:
                m[tuple(sorted(v))].append(v)
            else:
                m[tuple(sorted(v))] = [v]
        return list(m.values())