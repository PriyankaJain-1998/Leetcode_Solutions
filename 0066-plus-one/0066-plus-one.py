class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        return list(map(int,list(str(int("".join(list(map(str, digits))))+1))))