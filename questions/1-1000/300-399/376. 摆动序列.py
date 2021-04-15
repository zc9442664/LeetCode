# Date:       2020/12/12
# encode:      UTF-8
__author__ = "zcTresure"


class Solution:
    # 动态规划
    def wiggleMaxLength(self, nums: list) -> int:
        n = len(nums)
        if n < 2:
            return n
        up = [1] + [0] * (n - 1)
        down = [1] + [0] * (n - 1)
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                up[i] = max(up[i - 1], down[i - 1] + 1)
                down[i] = down[i - 1]
            elif nums[i] < nums[i - 1]:
                down[i] = max(down[i - 1], up[i - 1] + 1)
                up[i] = up[i - 1]
            else:
                up[i] = up[i - 1]
                down[i] = down[i - 1]
        return max(up[n - 1], down[n - 1])

    # 动态规划 + 空间优化
    def wiggleMaxLength(self, nums: list) -> int:
        n = len(nums)
        if n < 2:
            return n
        up = down = 1
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                up = max(up, down + 1)
            elif nums[i] < nums[i - 1]:
                down = max(down, up + 1)
        return max(up, down)

    # 贪心
    def wiggleMaxLength(self, nums: list) -> int:
        n = len(nums)
        if n < 2:
            return n
        prevdiff = nums[1] - nums[0]
        ret = (2 if prevdiff != 0 else 1)
        for i in range(2, n):
            diff = nums[i] - nums[i - 1]
            if (diff > 0 and prevdiff <= 0) or (diff < 0 and prevdiff >= 0):
                ret += 1
                prevdiff = diff

        return ret


nums = [1, 7, 4, 9, 2, 5]
test = Solution()
print(test.wiggleMaxLength(nums))
