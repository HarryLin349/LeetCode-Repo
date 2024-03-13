class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # intution
        # looking for i, j where nums[i] + nums[j] = target
        # so given nums[i], if we know nums[target - nums[i]] = j  exists we have a sol
        # track a set where
        seen = {}
        for i in range(len(nums)):
            seen[nums[i]] = i
        for i in range(len(nums)):
            comp = target - nums[i]
            if comp in seen and i != seen[comp]:
                return [i, seen[comp]]
        