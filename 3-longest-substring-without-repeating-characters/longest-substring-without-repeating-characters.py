class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        hashMap = {}
        wstart = 0
        res = 0
        for wend in range(len(s)):
            if s[wend] in hashMap and wstart < hashMap[s[wend]]:
                wstart = hashMap[s[wend]]
            hashMap[s[wend]] = wend + 1
            res = max(res, wend-wstart+1)
        return res
                        


        