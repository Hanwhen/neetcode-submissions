class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m = {}
        for i,v in enumerate(strs):
            key = tuple(sorted(v))
            if key in m:
                m[key].append(v)
            else:
                m[key] = [v]
        return list(m.values())