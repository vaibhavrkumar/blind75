def twoSum(self, nums: List[int], target: int) -> List[int]:
        # create hashmap: num:index
        hashMap = {}
        # itr ovr nums
        for i,n in enumerate(nums):
            diff  = target - n
            if diff in hashMap:
                return [hashMap[diff], i]
            hashMap[n] = i #if no match, make an entry in hashMap
        return
        # wgit