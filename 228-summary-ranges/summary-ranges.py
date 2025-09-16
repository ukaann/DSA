class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        result = []
        right = 0

        while right < len(nums):
            start = nums[right]
            while right < len(nums)-1 and nums[right]+1 == nums[right+1]:
                right+=1
            if start != nums[right]:
                result.append(str(start) + '->' + str(nums[right]))
            else:
                result.append(str(nums[right]))
            right+=1
        return result

