class Solution(object):
    def maxCount(self, banned, n, maxSum):
        banned_set = set(banned)
        
        total_sum = 0
        count = 0
        
        for num in range(1, n + 1):
            if num in banned_set:
                continue
            
            if total_sum + num > maxSum:
                break
            
            total_sum += num
            count += 1
        
        return count
