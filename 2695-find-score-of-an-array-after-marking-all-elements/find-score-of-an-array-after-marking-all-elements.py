class Solution(object):
    def findScore(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        score = 0
        marked = [False] * n
        
        # Create a list of tuples (value, index) and sort by value
        sorted_nums = sorted([(num, i) for i, num in enumerate(nums)], key=lambda x: x[0])
        
        for value, index in sorted_nums:
            if marked[index]:
                continue  # Skip if already marked
            
            # Add the value to the score
            score += value
            
            # Mark the current element and its neighbors
            marked[index] = True
            if index - 1 >= 0:
                marked[index - 1] = True
            if index + 1 < n:
                marked[index + 1] = True
        
        return score
