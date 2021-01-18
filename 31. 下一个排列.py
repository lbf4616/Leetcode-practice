# https://leetcode-cn.com/problems/next-permutation/solution/xia-yi-ge-pai-lie-by-leetcode-solution/
# Date: 2021-01-05 20:35:14
class Solution:
    def nextPermutation(self, nums):
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        if i >= 0:
            j = len(nums) - 1
            while j >= 0 and nums[i] >= nums[j]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        
        left, right = i + 1, len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        return nums

if __name__ == "__main__":
    import datetime
    sample = [1,2,3]
    so = Solution()
    res = so.nextPermutation(sample)
    print(res)
    now_time = datetime.datetime.now()
    print(now_time.strftime('%Y-%m-%d %H:%M:%S'))