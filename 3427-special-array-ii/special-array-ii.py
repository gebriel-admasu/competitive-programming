class Solution:
    def isArraySpecial(self, nums, queries):
        n = len(nums)
        
        # Step 1: Preprocess the `valid` array
        valid = [0] * (n - 1)
        
        for i in range(n - 1):
            if (nums[i] % 2) != (nums[i + 1] % 2):  # Different parity
                valid[i] = 1
        
        # Step 2: Precompute the prefix sum array for fast range queries
        prefix = [0] * n
        for i in range(1, n):
            prefix[i] = prefix[i - 1] + valid[i - 1]
        
        # Step 3: Answer each query
        result = []
        for fromi, toi in queries:
            if prefix[toi] - prefix[fromi] == (toi - fromi):  # All pairs are valid
                result.append(True)
            else:
                result.append(False)
        
        return result
