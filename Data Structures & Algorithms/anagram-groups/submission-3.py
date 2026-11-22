class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m = {}
        for i,v in enumerate(strs):
            letter_array = [0] * 26
            for ch in v:
                letter_array[ord(ch)-97] +=1
            tup = tuple(letter_array)
            if tup not in m:
                m[tup] = [v]
            else:
                m[tup].append(v)
        return list(m.values())