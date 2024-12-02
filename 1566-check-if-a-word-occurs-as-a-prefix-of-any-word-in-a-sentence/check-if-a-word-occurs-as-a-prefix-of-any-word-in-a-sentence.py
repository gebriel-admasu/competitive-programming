class Solution(object):
    def isPrefixOfWord(self, sentence, searchWord):
        res = -1  
        count = 0
        
        for word in sentence.split():
            count += 1

            if word.startswith(searchWord):
                res = count
                break
        
        return res