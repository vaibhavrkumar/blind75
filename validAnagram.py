def validAnagram(self, s: str, t: str) -> bool:
        # check if the length of 2 strings is the same
        if(len(s) != len(t)):
            return False
        # create a hashmap for each of the 2 strings
        hashS, hashT = {}, {}
        # run a for loop over s, if a char is not found assign 0
        # else increment key value by one
        for char in range(len(s)):
            hashS[s[char]] = hashS.get(s[char], 0) + 1
            hashT[t[char]] = hashT.get(t[char], 0) + 1
        # compare the 2 hashmaps
        for count in hashS:
            if hashS[count] != hashT.get(count, 0):
                return False     
        return 
        # wgit