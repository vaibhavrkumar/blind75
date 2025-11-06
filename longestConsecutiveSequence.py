class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        resultSet = set(nums)
        longest = 0

        for n in resultSet:
            if (n-1) not in resultSet:
                length = 1
                while (n+length) in resultSet:
                    length +=1
                longest = max(longest, length)
        
        return longest