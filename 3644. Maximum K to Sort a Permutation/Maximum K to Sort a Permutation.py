class Solution(object):
    def sortPermutation(self, nums):
       
        ans = (1 << 31) - 1
        found = False

        for i, x in enumerate(nums):
            if i != x:
                ans &= x
                found = True

        return ans if found else 0
