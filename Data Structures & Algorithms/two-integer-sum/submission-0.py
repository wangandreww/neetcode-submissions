class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            counterpart = target-nums[i]
            if (counterpart in nums and (nums.index(counterpart) != i)):
                return [min(i,(nums.index(counterpart))),max(i,(nums.index(counterpart)))]

        return [0,0]