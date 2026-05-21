class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Strips spaces and special characters from string
        cleanStr = "".join(char.lower() for char in s if char.isalnum())

        # Two pointers
        left = 0
        right = len(cleanStr) - 1

        # Compares string characters from beginning to end, moving inwards
        while left < right:
            if cleanStr[left] != cleanStr[right]:
                return False
            left += 1
            right -= 1

        return True