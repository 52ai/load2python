# !/usr/bin/env python2.7
# Problem 1:Two Sum

class Solution(object):
    def twosum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        for i in range(0, len(nums)):
            for j in range((i+1), len(nums)):
                if (nums[i] + nums[j]) == target: return [i, j]

solu = Solution()
nums = [3, 2, 4]
target = 6 
print solu.twosum(nums, target)


