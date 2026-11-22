class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = {}
        for i in range(0, len(nums)):
            if nums[i] not in m:
                m[target - nums[i]] = i
            else:
                return [m[nums[i]],i]