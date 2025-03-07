class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # do something with character counts?
        # keep a sliding window and keep track of char counts
        # max length is if
        # length <= num_most + k
        # else, shrink window and move on

        l,r = 0,0
        char_counts = [0] * 26 # faster with a 26 size array but that's not readable
        max_length = 1
        while (r < len(s)):
            # add the current character
            index = ord('A') - ord(s[r])
            char_counts[index] += 1
            length = r - l + 1
            max_count = max(char_counts)

            # check to see if the cur window is valid
            if length <= max_count + k:
                max_length = max(max_length, length)
            else:
                # pop to shrink the window and move on
                index = ord('A') - ord(s[l])
                char_counts[index] -= 1
                l += 1
            # add the next char
            r += 1
        return max_length