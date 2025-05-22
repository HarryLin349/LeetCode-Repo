class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        k %= len(nums)
        while k > 0:
            nums.insert(0, nums.pop(-1))
            k -= 1