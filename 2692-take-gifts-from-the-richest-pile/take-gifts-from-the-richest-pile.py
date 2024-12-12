import heapq

class Solution(object):
    def pickGifts(self, gifts, k):
        """
        :type gifts: List[int]
        :type k: int
        :rtype: int
        """
        # Convert the gifts array into a max heap by pushing negative values
        max_heap = [-g for g in gifts]
        heapq.heapify(max_heap)

        # Perform k operations
        for _ in range(k):
            # Extract the maximum element (note: it's stored as negative)
            max_gifts = -heapq.heappop(max_heap)
            # Calculate the gifts left behind
            remaining_gifts = int(max_gifts**0.5)
            # Push the remaining gifts back into the heap
            heapq.heappush(max_heap, -remaining_gifts)

        # Sum the remaining gifts in the heap and return (convert back to positive)
        return -sum(max_heap)
