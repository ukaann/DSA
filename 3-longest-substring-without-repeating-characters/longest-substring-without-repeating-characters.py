class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        myset = set()
        left = 0
        result = 0

        for right in range(len(s)):
            while s[right] in myset:
                myset.remove(s[left])
                left+=1
            myset.add(s[right])
            result = max(result, len(myset))
        return result
                


        