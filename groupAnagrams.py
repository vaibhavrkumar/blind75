# groupAnagrams - medium
from collections import defaultdict
class Solution:
res = defaultdict(list)
        # res = []

        for s in strs:
            count = [0] * 26

            for c in s:
                count[ord(c) - ord("a")] +=1

            res[tuple (count)].append(s)
    
        return list (res.values())