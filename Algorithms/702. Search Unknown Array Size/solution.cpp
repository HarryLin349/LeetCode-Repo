class Solution {
public:
    int search(const ArrayReader& reader, int target) {
        // find the max elem of the array
        int error = INT_MAX;
        int maxInd = 1;
        int start = -1;
        while (true){
            if (reader.get(start+ maxInd) != error && reader.get(start + maxInd + 1) == error) {
                break;
            }
            maxInd *= 2;
            if (reader.get(start + maxInd) == error){
                start += (maxInd / 2);
                maxInd = 1;
            }   
        }
        int left = 0;
        int right = maxInd + start;        
        int mid = (left + right) / 2;
        while (reader.get(mid) != target){
            if (left >= right) return -1;
            int val = reader.get(mid);
            if (target < val){
                right = mid - 1;
            } else {
                left = mid + 1;
            }
            mid = (left + right) / 2;
        }
        return mid;
    }
};