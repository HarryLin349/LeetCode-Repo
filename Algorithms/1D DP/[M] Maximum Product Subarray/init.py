# similar to kadane's algorithm

class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        '''
        idea
        keep track of the current product
        if product ever hits 0, reset (will never change)
        if we hit 0 or an end, we divide each in the last reset to see if it improves
        '''
        cur = 1
        lastzero = 0
        maxproduct = nums[0]
        n = len(nums)
        for i in range(n):
            print (f"at {i}, cur {cur}, max {maxproduct}, nums[{i}] = {nums[i]}")
            if (nums[i] != 0):
                cur *= nums[i]
                maxproduct = max(maxproduct, cur)
            print(f"cur now {cur}, max: {maxproduct}")
            if nums[i] == 0 or i == n-1:
                print("backtracking")
                # we've reach an end, go back and check divides from the last zero
                stopping = i-1 if nums[i] == 0 else i
                for j in range(lastzero, stopping):
                    print(f"==checking to divide out {j}: {nums[j]}")
                    cur = cur // nums[j]
                    maxproduct = max(maxproduct, cur)
                # now we reset
                lastzero = i + 1
                cur = 1
                if nums[i] == 0:
                    maxproduct = max(maxproduct, 0)
                    continue

        return maxproduct