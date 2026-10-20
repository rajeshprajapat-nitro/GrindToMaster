class Solution(object):
    def sortableIntegers(self, nums):
        n = len(nums)
        ans = 0

        for k in range(1, n + 1):
            if n % k != 0:
                continue

            valid = True
            prev_last = None

            for start in range(0, n, k):
                end = start + k
                desc = -1

                for i in range(start, end - 1):
                    if nums[i] > nums[i + 1]:
                        if desc != -1:
                            valid = False
                            break
                        desc = i

                if not valid:
                    break

                # Rotate after the descent, if one exists.
                if desc != -1:
                    if nums[end - 1] > nums[start]:
                        valid = False
                        break

                    first = nums[desc + 1]
                    last = nums[desc]
                else:
                    first = nums[start]
                    last = nums[end - 1]

                if prev_last is not None and prev_last > first:
                    valid = False
                    break

                prev_last = last

            if valid:
                ans += k

        return ans
