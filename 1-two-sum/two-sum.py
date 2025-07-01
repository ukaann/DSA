class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap = {}
        for i in range(len(nums)):
            compl = target - nums[i]
            if compl in hashmap:
                return [i, hashmap[compl]]
            hashmap[nums[i]] = i
        return []
            
        