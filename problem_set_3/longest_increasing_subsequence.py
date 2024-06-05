class LongestSubsequence:
    def __init__(self, nums):
        """
        Initialize the LongestSubsequence class with a list of numbers.
        """
        self.nums = nums
        self.longest_subsequence()

    def longest_subsequence(self):
        """
        Find the length of the longest increasing subsequence in the list of numbers.
        """
        # If the list is empty, print 0 and return
        if len(self.nums) == 0:
            print(0)
            return
        
        # Initialize the lis_lengths array where each element is 1 (minimum length of increasing subsequence)
        lis_lengths = [1] * len(self.nums)
        
        # Iterate through each element starting from the second element
        for i in range(1, len(self.nums)):
            # For each element, check all previous elements
            for j in range(0, i):
                # If the current element is greater than the previous element,
                # update the lis_lengths value to be the maximum of its current value and the lis_lengths value of the previous element plus one
                if self.nums[i] > self.nums[j]:
                    lis_lengths[i] = max(lis_lengths[i], lis_lengths[j] + 1)
        
        # Print the maximum value in the lis_lengths array which represents the length of the longest increasing subsequence
        print(max(lis_lengths))

# Create an instance of LongestSubsequence with a list of numbers
LongestSubsequence([10, 9, 2, 5, 3, 7, 101, 18])
