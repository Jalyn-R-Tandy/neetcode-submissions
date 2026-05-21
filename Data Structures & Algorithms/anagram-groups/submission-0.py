class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}

        # Checks for alphabetically sorted string as key
        for word in strs:
            newWord = "".join(sorted(word))
            
            # Adds string to value pair if contains same frequency of letters
            if newWord not in anagrams:
                anagrams[newWord] = [word]
            else:
                anagrams[newWord].append(word)
        
        # Lists values of key-value pairs of lists of anagrams
        return list(anagrams.values())