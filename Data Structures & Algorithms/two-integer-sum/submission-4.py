class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = {}
        for i, v in enumerate(nums):
            if (target - v) not in m:
                m[v]=i
            else:
                return [m[target-v], i]
            