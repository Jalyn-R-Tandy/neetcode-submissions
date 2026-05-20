class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # hash table for integers
        int_map = {}

        for i in range(len(nums)):
            # sets number at index to key
            key = nums[i]

            # checks if key is not already in hash map
            if key not in int_map:
                int_map[key] = 1
            else:
                return True

        return False