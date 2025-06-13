class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int insertPos = 0;

        // Step 1: Move all non-zero values forward
        for (int i = 0; i < nums.size(); ++i) {
            if (nums[i] != 0) {
                nums[insertPos++] = nums[i];
            }
        }

        // Step 2: Fill remaining slots with 0
        while (insertPos < nums.size()) {
            nums[insertPos++] = 0;
        }
    }
};