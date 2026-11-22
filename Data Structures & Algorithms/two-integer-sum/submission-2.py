class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = {}
        for i,v in enumerate(nums):
            if v not in m:
                m[target-v] = i
            else:
                return [m[v],i]