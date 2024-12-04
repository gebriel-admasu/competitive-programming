class Solution(object):
    def canMakeSubsequence(self, str1, str2):
       
        i, j = 0, 0
        n, m = len(str1), len(str2)
        
        while i < n and j < m:
            if str1[i] == str2[j]:
                j += 1
            elif (ord(str1[i]) - ord('a') + 1) % 26 + ord('a') == ord(str2[j]):
                j += 1
            i += 1
        
        return j == m
