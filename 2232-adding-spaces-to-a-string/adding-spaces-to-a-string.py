class Solution(object):
    def addSpaces(self, s, spaces):
        new_string = []
        space_index = 0
        n = len(spaces)
        for i,char in enumerate (s):
            if space_index < n  and i == spaces[space_index]:
                new_string.append(" ")
                space_index +=1

        
            new_string.append(char)

        return ''.join(new_string)