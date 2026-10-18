class Solution:
    def numOfWays(self, nums):
        MOD = 10**9 + 7
        n = len(nums)

        comb = [[0] * (n + 1) for _ in range(n + 1)]

        for i in range(n + 1):
            comb[i][0] = 1
            for j in range(1, i + 1):
                if j == i:
                    comb[i][j] = 1
                else:
                    comb[i][j] = (
                        comb[i - 1][j - 1] +
                        comb[i - 1][j]
                    ) % MOD

        def solve(arr):
            if len(arr) <= 2:
                return 1

            root = arr[0]
            left = []
            right = []

            for x in arr[1:]:
                if x < root:
                    left.append(x)
                else:
                    right.append(x)

            l = len(left)
            r = len(right)

            ways = comb[l + r][l]
            ways = ways * solve(left) % MOD
            ways = ways * solve(right) % MOD

            return ways

        return (solve(nums) - 1) % MOD
