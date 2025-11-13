class Solution:
    def decodeString(self, s: str) -> str:
        # s = 100 [leetcode]

        stack = []
        for i in range(len(s)):
            if s[i] != "]":
                stack.append(s[i])
            else:
                subStr = ""
                while stack[-1] != "[":
                    subStr = stack.pop() + subStr                
                stack.pop() #we have reached '[' -> so we pop [

                k = "" #extracting num
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k #1
                stack.append(int (k) * subStr)
        
        return "".join(stack)
                               