class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        frequency = [[] for i in range(len(nums) + 1)] # array for 
        output = []

        # maps number element count in dictionary
        for n in nums:
            if n not in count:
                count[n] = 1
            else:
                count[n] += 1
        
        for n, c in count.items():
            frequency[c].append(n) # add value to frequency slot in array

        
        # loop backwards to find most frequent elements
        for i in range(len(frequency) - 1, 0, -1):
            for j in frequency[i]:
                output.append(j)
                if len(output) == k:
                    return output