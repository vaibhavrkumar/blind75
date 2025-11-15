class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        resultSet = set(nums)
        res = 0

        for n in nums:
            streak = 0
            # numPos = 0

            while (n-1) not in resultSet:
                streak += 1
                n += 1
                res = max(res, streak)

        return res


mySolution = Solution()
print(mySolution.longestConsecutive([100,4,200,1,3,2]))