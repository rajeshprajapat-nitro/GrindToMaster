class Solution(object):
    def sortableIntegers(self, nums):
        n = len(nums)
        ans = 0

        for k in range(1, n + 1):
            if n % k != 0:
                continue

            valid = True

            for start in range(0, n, k):
                descents = 0

                for i in range(start, start + k - 1):
                    if nums[i] > nums[i + 1]:
                        descents += 1

                # Include the circular boundary
                if nums[start + k - 1] > nums[start]:
                    descents += 1

                if descents > 1:
                    valid = False
                    break

            if valid:
                # Verify the rotated blocks collectively form a sorted array
                rotated = []
                for start in range(0, n, k):
                    block = nums[start:start + k]
                    best = min(
                        block[i:] + block[:i] for i in range(k)
                    )
                    rotated.extend(best)

                if rotated == sorted(rotated):
                    ans += k

        return ans
