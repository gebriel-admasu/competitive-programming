class Solution(object):
    def canChange(self, start, target):
        start_positions = [(i, char) for i, char in enumerate(start) if char != '_']
        target_positions = [(i, char) for i, char in enumerate(target) if char != '_']
        
        if len(start_positions) != len(target_positions):
            return False
        
        for (start_index, char_start), (target_index, char_target) in zip(start_positions, target_positions):
            if char_start != char_target:
                return False
            if char_start == 'L' and start_index < target_index:
                return False
            if char_start == 'R' and start_index > target_index:
                return False
        
        return True
