import java.util.Arrays;

class Solution {
    public boolean containsDuplicate(int[] nums) {
        Arrays.sort(nums);
        for (int i = 0; i < nums.length; i++){ 
            if (i > 0 && nums[i] == nums[i - 1]) {
                return true;
            }
        }
        return false;
    }
}