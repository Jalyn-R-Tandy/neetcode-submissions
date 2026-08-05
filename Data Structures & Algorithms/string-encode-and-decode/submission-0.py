class Solution:

    def encode(self, strs: List[str]) -> str:
        # add num of char of next str to represent str len
        # add delimiter after num of char
        # conjoin the list of str
        encoded_str = ""

        for s in strs:
            encoded_str += str(len(s)) + "#" + s
        
        return encoded_str

    def decode(self, s: str) -> List[str]:
        # read num as len of next str
        # read 1 delimiter
        # add str to list based on num char
        decoded_strs = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            len_word = int(s[i:j])
            decoded_strs.append(s[j + 1: j + 1 + len_word])
            i = j + 1 + len_word
        return decoded_strs
            


