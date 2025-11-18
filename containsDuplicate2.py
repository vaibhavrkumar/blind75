class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        #sliding window
        l = 0
        duplicateSet = set() #hashmap to find duplicate

        for r in range(len(nums)):
            #checking abs(i-j) <= k
            if r - l > k:
                duplicateSet.remove(nums[l])
                l += 1

            #nums[i] == nums[j]
            if nums[r] in duplicateSet:
                return True
            
            duplicateSet.add(nums[r])
        return False
            
            
