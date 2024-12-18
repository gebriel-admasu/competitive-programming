class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.prefix =[]
        current = 0
        for n in nums:
            current +=n
            self.prefix.append(current)
        

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        rightsum = self.prefix[right]
        leftsum = self.prefix[left-1] if left >0 else 0
        return rightsum - leftsum

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)