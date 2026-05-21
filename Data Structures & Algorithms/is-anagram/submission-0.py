class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Hash map for string characters
        s_map = {}
        t_map = {}

        # Tracks frequencies of letters in string s
        for i in range(len(s)):
            key = s[i]
            if key in s_map:
                s_map[key] += 1
            else:
                s_map[key] = 1
        
        # Tracks frequencies of letters in string t
        for j in range(len(t)):
            key = t[j]
            if key in t_map:
                t_map[key] += 1
            else:
                t_map[key] = 1

        # Compares characters
        if s_map == t_map:
            return True

        return False