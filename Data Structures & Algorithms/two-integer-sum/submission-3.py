class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Stores all seen complements and indices
        seen = {}
        # Stores indices to add up to target
        twoSum = []

        # Finds complement value of target to check against other values
        for i in range(len(nums)):
            complement = target - nums[i]

            if complement not in seen:
                seen[nums[i]] = i
            else:
                twoSum = [seen[complement], i]
                
        return twoSum