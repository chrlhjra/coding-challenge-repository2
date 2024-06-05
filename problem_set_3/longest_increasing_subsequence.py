class longestSubsequence():
    def __init__(self, nums):
        self.nums = nums
        self.longestSubsequence()

    def longestSubsequence(self):
        if len(self.nums) == 0:
            print(0)
        dp = [1] * len(self.nums)
        for i in range(1, len(self.nums)):
            for j in range(0, i):
                if self.nums[i] > self.nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        print(max(dp))

longestSubsequence([10, 9, 2, 5, 3, 7, 101, 18])

