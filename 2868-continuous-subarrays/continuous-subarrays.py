from sortedcontainers import SortedList

class Solution(object):
    def continuousSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        start = 0
        total_count = 0
        window = SortedList()

        for end in range(n):
            # Add the current element to the window
            window.add(nums[end])

            # Ensure the window is valid
            while window[-1] - window[0] > 2:
                window.remove(nums[start])
                start += 1

            # All subarrays ending at `end` are valid
            total_count += (end - start + 1)

        return total_count
