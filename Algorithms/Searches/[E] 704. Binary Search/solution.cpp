using namespace std;
#include <vector>


class Solution {
public:
    int search(vector<int>& nums, int target) {
        int left = 0;
        int right = nums.size() - 1;
        int mid = (left + right) / 2;
        while (nums.at(mid) != target) {
            if (left >= right) return -1;
            int val = nums.at(mid);
            if (target < val) {
                right = mid - 1;
            } else {
                left = mid + 1;
            }
            mid = (left + right) / 2;
        }
        return mid;
    }
};