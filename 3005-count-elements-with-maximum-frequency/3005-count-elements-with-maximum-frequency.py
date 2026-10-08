class Solution:
    def maxFrequencyElements(self, nums):
        freq = {}

        for x in nums:
            freq[x] = freq.get(x, 0) + 1

        m = max(freq.values())

        return sum(x for x in freq.values() if x == m)