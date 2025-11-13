class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        numsLength = len(nums)
        res = [1]*numsLength

        prefix = 1
        for i in range(numsLength):
            res[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for j in range(numsLength-1, -1, -1):
            res[j] *= postfix
            postfix *= nums[j]
        
        return res

