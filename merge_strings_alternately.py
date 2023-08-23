def mergeAlternately(word1, word2):
        """
        You are given two strings word1 and word2. 
        Merge the strings by adding letters in alternating order, starting with word1. 
        If a string is longer than the other, append the additional letters onto the end of the merged string.

        Eg: Input: word1 = "abc", word2 = "pqr"
            Output: "apbqcr"
            Explanation: The merged string will be merged as so:
            word1:  a   b   c
            word2:    p   q   r
            merged: a p b q c r
            
        """
        new_word = ''
        small = len(word1) if len(word1) < len(word2) else len(word2)

        for i in range(0,small):
            if i <= small:
                    new_word += word1[i]
                    new_word += word2[i]
                    
        if small == len(word1):
            new_word += word2[small:]
        elif small == len(word2):
            new_word += word1[small:]            

        return new_word
