class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # idea: evaluate in order
        # keep a stack to track heights and their starting index
        max_area = -1
        cur_heights = []
        cur_heights.append((heights[0], 0))
        for i in range(1, len(heights)):
            starting_index = i
            # check if the previous is bottlenecked
            while cur_heights and cur_heights[-1][0] > heights[i]:
                # if bottlenecked, pop the stack and calculate its area
                prev_height, prev_ind = cur_heights.pop()
                cur_area = prev_height * (i - prev_ind)
                # print(f"height {prev_height} bottlenecked at {prev_ind}-{i} to {heights[i]}")
                # print(f"cur area {cur_area}")
                max_area = max(max_area, cur_area)
                starting_index = prev_ind
            # add the cur height to the stack
            cur_heights.append((heights[i], starting_index))
        final_ind = len(heights)
        while cur_heights:
            prev_height, prev_ind = cur_heights.pop()
            cur_area = prev_height * (final_ind - prev_ind)
            max_area = max(max_area, cur_area)
        return max_area
