'''Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
'''


class Solution:
    def firstUniqChar(self, s: str) -> int:
        from collections import Counter
        
        count=Counter(s)
        for i in count.keys():
            if count[i]==1:
                return s.index(i)
        return -1
            
        
