class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l, total, res = 0, 0, 0
        count = collections.defaultdict(int) 

        for r in range(len(fruits)):
            fr = fruits[r]
            count[fr] += 1
            total += 1
            while len(count) > 2:
                fl = fruits[l]
                count[fl] -= 1                
                total -= 1
                l += 1                               
                if not count[fl]:
                    count.pop(fl)                 
            res = max(res, total)
        return res