# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def reverseOddLevels(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        if not root:
            return None
        
        # Initialize BFS queue
        queue = deque([root])
        
        # Perform level-order traversal
        level = 0
        while queue:
            level_size = len(queue)
            current_level_values = []
            nodes_at_level = []
            
            # Collect all nodes and their values at the current level
            for _ in range(level_size):
                node = queue.popleft()
                nodes_at_level.append(node)
                current_level_values.append(node.val)
                
                # Add child nodes to the queue for the next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            # If it's an odd level, reverse the values
            if level % 2 == 1:
                current_level_values.reverse()
                # Reassign the reversed values back to the nodes
                for i in range(len(nodes_at_level)):
                    nodes_at_level[i].val = current_level_values[i]
            
            # Move to the next level
            level += 1
        
        return root
