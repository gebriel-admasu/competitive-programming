from bisect import bisect_right

class Solution(object):
    def maxTwoEvents(self, events):
     
        events.sort(key=lambda x: x[1])
        n = len(events)
        
        end_times = [event[1] for event in events]
        
        
        max_values = [0] * n
        max_values[0] = events[0][2]
        
        for i in range(1, n):
            max_values[i] = max(max_values[i - 1], events[i][2])
        
        max_sum = 0
        for i in range(n):
            current_value = events[i][2]
            
          
            idx = bisect_right(end_times, events[i][0] - 1) - 1
            
          
            if idx >= 0:
                current_value += max_values[idx]
            
            max_sum = max(max_sum, current_value)
        
        return max_sum
