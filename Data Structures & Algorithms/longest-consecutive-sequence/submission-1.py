class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ##use a set for lookups 
        numset = set(nums)
        longest = 0 

        ##find where start of sequence is by n-1 exists or not? if n-1 exists then not the start!

        for num in numset: 
            if num - 1 not in numset:
                length = 1
                while num + length in numset:
                    length += 1 

                longest = max(longest,length)

        
        return longest





