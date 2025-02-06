class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # for each elem, pick a random num from remaining
        result = []
        cur = []
        n = len(nums)

        def dfs(i):
            if (i >= n):
                # we've filled every spot
                result.append(cur.copy())
                return
            
            # for the current, add each remaining elem, and then return
            for j in range(n):
                if nums[j] not in cur:
                    cur.append(nums[j])
                    dfs(i+1)
                    cur.pop()
            return
        
        dfs(0)
        return result