class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ##zxyzxyz
        ##two pointer? 
        ##first start at z then x then y then z
        ##keep track of length being added
        ##when we see a repeat:
        ##longest = max(longest, current)
        ##start from the next letter
        ##keep track of repeating characters with a set()

        i = j = 0 
        longest = 0
        seen = set()
        while j < len(s):
            
            while s[j] in seen: 
                seen.discard(s[i])
                i += 1
            seen.add(s[j])
            j += 1
            
            longest = max(longest, len(seen))

        return longest
        
            




        