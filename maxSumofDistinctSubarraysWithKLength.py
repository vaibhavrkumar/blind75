class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        res, sum, l = 0, 0, 0
        count = defaultdict(int)

        for r in range(len(nums)):
            count[nums[r]] += 1
            sum += nums[r]

            #checking if r - l + 1 > k
            if r - l + 1 > k:
                sum -= nums[l]
                count[nums[l]] -= 1
                if count[nums[l]] == 0:
                    count.pop(nums[l])            
                l += 1
            
            #checking for dups in count
            if len(count) == k and r - l + 1 == k:
                res = max(res, sum)

        return res