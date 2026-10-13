class Solution:
    def maxAlternatingSum(self, nums):
        nums.sort(key=abs)

        n = len(nums)
        k = (n + 1) // 2
        ans = 0

        for i in range(n):
            square = nums[i] * nums[i]

            if i < n - k:
                ans -= square
            else:
                ans += square

        return ans
