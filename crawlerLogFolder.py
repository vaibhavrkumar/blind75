class Solution:
    def minOperations(self, logs: List[str]) -> int:
        res = 0
        
        for l in logs:
            if l == "../":
                res = max(0, res - 1)
            elif l == "./":
                continue
            else:
                res += 1
        return res        