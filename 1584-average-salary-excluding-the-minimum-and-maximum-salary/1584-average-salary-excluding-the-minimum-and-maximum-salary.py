class Solution:
    def average(self, salary: List[int]) -> float:
        minsal, maxsal = min(salary), max(salary)
        return (sum(salary)-minsal-maxsal)/(len(salary)-2)