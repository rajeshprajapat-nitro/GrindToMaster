class Solution:
    def minOperations(self, nums):
        n = len(nums)

        if n == 1:
            return 0

        # Check increasing cyclic order
        inc = all(
            nums[(i + 1) % n] == (nums[i] + 1) % n
            for i in range(n)
        )

        if inc:
            k = nums.index(0)
            return min(k, n - k + 2)

        # Check decreasing cyclic order
        dec = all(
            nums[(i + 1) % n] == (nums[i] - 1) % n
            for i in range(n)
        )

        if dec:
            k = n - 1 - nums.index(0)
            return min(k, n - k) + 1

        return -1
