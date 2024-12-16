class Solution(object):
    def getFinalState(self, nums, k, multiplier):

        for _ in range(k):

            min_index = nums.index(min(nums))
        # Replace the minimum value with its product with the multiplier
            nums[min_index] *= multiplier
        return nums
        