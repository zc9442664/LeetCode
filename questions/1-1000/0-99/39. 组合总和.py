class Solution:
    def combinationSum(self, candidates: list, target: int) -> list:
        ans = list()

        def backtrack(cur_nums: list, target: int, index: int):
            if index == len(candidates):
                return
            if target == 0:
                ans.append(cur_nums[:])
                return
            backtrack(cur_nums, target, index + 1)
            if target - candidates[index] >= 0:
                cur_nums.append(candidates[index])
                backtrack(cur_nums, target - candidates[index], index)
                cur_nums.pop()
        backtrack([], target, 0)
        return ans

    def combinationSum(self, candidates: list, target: int) -> list:
        ans = list()

        def backtrack(cur_nums: list, target: int, index: int):
            if target < 0:
                return
            elif target == 0:
                ans.append(cur_nums[:])
                return
            else:
                for i in range(index, len(candidates)):
                    cur_nums.append(candidates[i])
                    backtrack(cur_nums, target - candidates[i], i)
                    cur_nums.pop()
        backtrack([], target, 0)
        return ans


candidates = [2, 3, 6, 7]
target = 7
test = Solution()
print(test.combinationSum(candidates, target))
