class Solution:
    def average(self, salary: list) -> float:
        return (sum(salary) - max(salary) - min(salary)) / (len(salary) - 2)


salary = [4000, 3000, 1000, 2000]
test = Solution()
print(test.average(salary))
