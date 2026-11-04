class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ###width = largest index difference
        ###height = second largest value 
        # 1 6 -> 1 * 7 = 7 
        # if i + 1 > i -> 7 6 -> 6* 6 36


        i = 0 
        j = len(heights)-1 
        result = (min(heights[i],heights[j])) * (j - i)

        while i != j: 
            
            if heights[i] < heights[j]:
                i += 1 
            else:
                j -= 1

            result = max(result,(min(heights[i],heights[j])) * (j - i))

        return result

